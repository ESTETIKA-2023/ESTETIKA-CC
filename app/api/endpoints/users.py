from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from app.schemas.default_schemas import DefaultResponse
from app.schemas.user import (
    RequestRegister,
    ResponseRegister,
    RequestLogin,
    ResponseLogin,
    GetUserData,
    CreateUserDetail,
    EditProfile,
    UpdatePassword
)
from firebase_admin import auth, storage
from app.deps.firebase import db
from datetime import datetime
from app.deps.encrypt import encrypt, decrypt
from app.deps.jwt_handler import sign_jwt
import os

router = APIRouter()

@router.post("/register", response_model=ResponseRegister, status_code=status.HTTP_201_CREATED)
async def register_user(
    request: RequestRegister
) -> JSONResponse:
    if request.password != request.confirmPassword:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password and Confirm Password are not the same",
        )
    try:
        user = auth.create_user(email=request.email, display_name=request.username, password=request.password)
        try:
            doc_ref = db.collection('users').document(user.uid)
            doc_ref.set({
                'id': user.uid,
                'email': user.email,
                'username': user.display_name,
                'password': encrypt(request.password),
                'registeredAt': datetime.now(),
            })

            return ResponseRegister(
                message="Register success",
                data=GetUserData(
                    user_id=user.uid,
                    username=user.display_name,
                    email=user.email
                ),

            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists, please do login instead",
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.post("/login", response_model=ResponseLogin, status_code=status.HTTP_200_OK)
async def login_user(
    request: RequestLogin,
) -> JSONResponse:
    try:
        user = auth.get_user_by_email(request.email)
        try:
            doc_ref = db.collection('users').document(user.uid)
            doc_snapshot = doc_ref.get()
            if doc_snapshot.exists:
                data = doc_snapshot.to_dict()
                if decrypt(data.get('password')) != request.password:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Password is incorrect",
                    )
                jwt_token = sign_jwt(user.uid)
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User not found",
                )

            return ResponseLogin(
                message="Login success",
                data=GetUserData(
                    user_id=user.uid,
                    username=user.display_name,
                    email=user.email
                ),
                access_token=jwt_token['access_token']
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )
    
    except auth.UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found",
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.post("/user/{user_uid}/detail", status_code=status.HTTP_200_OK)
async def create_user_detail(
    request: CreateUserDetail,
    user_uid: str
) -> JSONResponse:
    try:
        doc_ref = db.collection('users').document(user_uid)
        doc_snapshot = doc_ref.get()

        if not doc_snapshot.exists:
            try:
                user = auth.get_user(user_uid)
                doc_ref.set({
                    'id': user.uid,
                    'email': user.email,
                    'username': user.display_name,
                    'registeredAt': datetime.now(),
                })
                doc_ref = db.collection('users').document(user_uid)
                doc_snapshot = doc_ref.get()

            except auth.UserNotFoundError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User not found",
                )

        data = {
            'id': doc_snapshot.get('id'),
            'email': doc_snapshot.get('email'),
            'username': doc_snapshot.get('username'),
            'registeredAt': doc_snapshot.get('registeredAt'),
            'name': request.name,
            'imgUrl': "https://firebasestorage.googleapis.com/v0/b/estetika-capstone.appspot.com/o/blank-profile-picture.png?alt=media&token=5183f872-38e6-4d77-af79-eee63be0476b",
            'contactNumber': request.contactNumber,
            'age': request.age,
        }
        try:
            doc_ref.update(data)
            return DefaultResponse(
                message="User detail created",
                data=data
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
@router.put("/user/{user_uid}/edit", status_code=status.HTTP_200_OK)
async def edit_profile(
    request: EditProfile,
    user_uid: str
) -> JSONResponse:
    try:
        doc_ref = db.collection('users').document(user_uid)
        doc_snapshot = doc_ref.get()
        if not doc_snapshot.exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )
        data = doc_snapshot.to_dict()
        name = request.name or data.get('name')
        gender = request.gender or data.get('gender')
        contactNumber = request.contactNumber or data.get('contactNumber')
        age = request.age or data.get('age')

        try:
            edited_data = {
                'name': name,
                'gender': gender,
                'contactNumber': contactNumber,
                'age': age
            }

            doc_ref.update(edited_data)
            return DefaultResponse(
                message="User profile updated",
                data=edited_data   
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
@router.put("/user/{user_uid}/update-profile", status_code=status.HTTP_200_OK)
async def update_profile(user_uid: str, file: UploadFile = File(...)):
    try:
        doc_ref = db.collection('users').document(user_uid)
        doc_snapshot = doc_ref.get()
        if not doc_snapshot.exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )

        data = doc_snapshot.to_dict()
        username = data.get('username')

        filename, file_extension = os.path.splitext(file.filename)
        if file_extension.lower() not in {'.jpg', '.jpeg', '.png'}:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only JPG, JPEG and PNG files are allowed",
            )

        unique_filename = f"{username}-{filename}"
        renamed_filename = f"{unique_filename}{file_extension}"

        bucket = storage.bucket()

        blob = bucket.blob(renamed_filename)
        blob.upload_from_file(file.file, content_type=file.content_type)
        blob.make_public()

        image_url = blob.public_url

        doc_ref.update({
            'imgUrl': image_url
        })

        return {"image_url": image_url}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.put("/user/{user_uid}/update-password", status_code=status.HTTP_200_OK)
async def update_password(
    user_uid: str,
    request: UpdatePassword
) -> JSONResponse:
    if not request.newPassword == request.confirmNewPassword:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password and confirm new password does not match",
        )
        
    try:
        doc_ref = db.collection('users').document(user_uid)
        doc_snapshot = doc_ref.get()

        if not doc_snapshot.exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )

        data = doc_snapshot.to_dict()

        if not decrypt(data.get('password')) == request.oldPassword:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Old password is incorrect",
            )
        try:
            doc_ref.update({
                'password': encrypt(request.newPassword)
            })
            return {
                'message': 'Password updated'
            }
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )