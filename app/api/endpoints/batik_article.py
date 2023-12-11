import firebase_admin
from fastapi import FastAPI, HTTPException, Body, Path, APIRouter
from firebase_admin import initialize_app, credentials, firestore
import json
from app.schemas.batik_schema import BatikArticle 
import os

router = APIRouter()

db = firestore.client()

file_path = os.path.join(os.path.dirname(__file__), '..', 'data', "batik-article.json")

COLLECTION_ARTICLE = "batik_article_collection"

def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def create_collection_if_not_exists(db, collection_name):
    try:
        db.collection(collection_name).get()
    except Exception as e:
        db.create_collection(collection_name)

def get_collection_reference(collection_name):
    create_collection_if_not_exists(db, collection_name)
    return db.collection(collection_name)

@router.post("/push_data")
async def push_data():
    try:
        # Read data from the JSON file
        json_data = read_json_file(file_path)

        # Specify the Firestore collection
        collection_name = COLLECTION_ARTICLE
        create_collection_if_not_exists(db, collection_name)
        collection_ref = db.collection(collection_name)

        # Loop through each item in the JSON data and add to Firestore
        for item in json_data:
            document_id = item.get("document_id")
            if document_id:
                doc_ref = collection_ref.document(document_id)
                doc_ref.set(item)

        return {
            "status":{
                "code": 200,
                "message": "Data pushed successfully"
            }
        }
    except Exception as e:
        error_message = f"Error pushing data: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)
    
@router.get("/get-article")
async def get_article():
    try:
        article_collection = db.collection(COLLECTION_ARTICLE)
        documents = article_collection.stream()

        data = [{"id": doc.id, **doc.to_dict()} for doc in documents]

        return {
            "status":{
                "code": 200,
                "message": "Data fetched successfully"
            },
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/add-article")
async def add_article(article: BatikArticle):
    try:
        COLLECTION_ARTICLE = "batik_article_collection"
        create_collection_if_not_exists(db, COLLECTION_ARTICLE)
        collection_ref = db.collection(COLLECTION_ARTICLE)

        # Convert Pydantic model to dict
        article_dict = article.dict()

        # Add the new article to Firestore
        doc_ref = collection_ref.add(article_dict)

        return {
            "status": {
                "code": 201,
                "message": "Successfully added data"
            }
        }

    except Exception as e:
        error_message = f"Error adding article: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)
        
@router.delete("/delete-article/{document_id}")
async def delete_article(document_id: str = Path(..., title="The ID of the article to delete")):
    try:
        collection_name = COLLECTION_ARTICLE
        collection_ref = get_collection_reference(collection_name)

        doc_ref = collection_ref.document(document_id)
        doc_ref.delete()

        return {
            "status":{
                "code": 200,
                "message": f"Article with ID {document_id} deleted successfully"}
            }
    except Exception as e:
        error_message = f"Error deleting article: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)
    
@router.put("/update-article/{document_id}")
async def update_article(document_id: str = Path(..., title="The ID of the article to update"), updated_data: BatikArticle = Body(...)):
    try:
        collection_name = COLLECTION_ARTICLE
        collection_ref = get_collection_reference(collection_name)

        # Check if the document with the specified document_id exists
        doc_ref = collection_ref.document(document_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail=f"Article with ID {document_id} not found")

        # Convert Pydantic model to dict
        updated_data_dict = updated_data.dict()

        # Update the existing article with the new data
        doc_ref.update(updated_data_dict)
        return {
            "status": {
                "code": 200,
                "message": f"Article with ID {document_id} updated successfully"
            }
        }
    except Exception as e:
        error_message = f"Error updating article: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)