from fastapi import APIRouter, File, UploadFile, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from keras.models import load_model
from dotenv import load_dotenv
import os
import numpy as np
import os
import jwt
from PIL import Image
from app.deps.jwt_bearer import JWTBearer
from app.deps.jwt_handler import decode_jwt
from app.deps.firebase import db

router = APIRouter()

load_dotenv()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'images')

model_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Model_ML_Batik_5.0.h5')
batik_model = load_model(model_path, compile=False)

label_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'label.txt')
with open(label_file_path, "r") as file:
    batik_labels = file.read().splitlines()

def allowed_file(filename):
    return "." in filename and filename.split(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_filename(filename):
    return os.path.basename(filename)

def get_firestore_data(collection, field, value):
    query = collection.where(field, '==', value)
    documents = query.stream()
    return [{"id": str(doc.id), **doc.to_dict()} for doc in documents]

@router.post("/predict", tags=["Predict"])
async def predict(
    file: UploadFile = File(...),
    token: str = Depends(JWTBearer()),
):
    try:
        payload = decode_jwt(token)
        user_id = payload.get("user_id")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(UPLOADS_DIR, filename)

            with open(image_path, "wb") as img_file:
                img_file.write(file.file.read())

            # Preprocess input image for batik detection
            img = Image.open(image_path).convert("RGB")
            img = img.resize((224, 224))

            img_array = np.asarray(img)
            img_array = np.expand_dims(img_array, axis=0)
            normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            data[0] = normalized_image_array

            # Perform batik detection
            batik_prediction = batik_model.predict(data)
            batik_index = np.argmax(batik_prediction)
            batik_class_names = batik_labels[batik_index]
            batik_confidence_score = float(batik_prediction[0][batik_index])

            # Ensure batik_class_names is a string
            batik_class_names = str(batik_class_names)

            # Get Firestore data from batik_article_collection
            article_collection = db.collection('batik_article_collection')
            article_data = get_firestore_data(article_collection, 'document_id', batik_class_names)

            if article_data:
                asal_value = article_data[0].get('asal')
                if asal_value:
                    attraction_collection = db.collection('batik_tourist_attractions')
                    attraction_data = get_firestore_data(attraction_collection, 'Province', asal_value)
                else:
                    attraction_data = []
            else:
                attraction_data = []

            # Batik shop recommendation
            batik_shop_recommendation = []
            doc_ref = db.collection('batik_shop').document('jenis_batik').collection(batik_class_names).stream()
            for doc in doc_ref:
                batik_shop_data = doc.to_dict()
                batik_shop_data["id"] = doc.id
                reordered_shop_data = {"id": batik_shop_data.pop("id")}
                reordered_shop_data.update(batik_shop_data)
                batik_shop_recommendation.append(reordered_shop_data)
                batik_shop_recommendation = sorted(batik_shop_recommendation, key=lambda x: int(x["id"].split("_")[1]))

            # Delete image file after prediction
            os.remove(image_path)

            return {
                "status": {
                    "code": 200,
                    "message": "Success detecting batik and fetching data"
                },
                "data": {
                    "user_id": user_id,
                    "batik_types_prediction": batik_class_names,
                    "batik_confidence": batik_confidence_score,
                    "firestore_article_data": article_data,
                    "firestore_batik_tourist_attraction_data": attraction_data,
                    "firestore_batik_shop_recommendation_data": batik_shop_recommendation,
                },
            }
        else:
            raise HTTPException(
                status_code=400,
                detail="Client side error"
            )

    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired",
        )
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Invalid signature in JWT",
        )
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=f"An error occurred: {str(e)}",
        )