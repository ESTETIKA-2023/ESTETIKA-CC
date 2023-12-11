from pydantic import BaseModel, Field, EmailStr, constr
from uuid import UUID
from fastapi import Query
from datetime import date
from typing import List, Optional

class GetUserData(BaseModel):
    user_id: constr(strip_whitespace=True)
    username: constr(strip_whitespace=True)
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "bRN3ZFjpfqZW231JLyLPSsSTzsIu",
                "username": "user",
                "email": "user@gmail.com",
            }
        }

class RequestRegister(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=20) = Field(
        ...,
        pattern="^[a-z]+$[a-z\s]{0,9}$",
    )
    email: EmailStr
    password: constr()
    confirmPassword: constr()

    class Config:
        json_schema_extra = {
            "example": {
                "username": "user",
                "email": "user@gmail.com",
                "password": "securepassword",
                "confirmPassword": "securepassword",
            }
        }

class ResponseRegister(BaseModel):
    message: constr()
    data: GetUserData

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Registration successful",
                "data": {
                    "user_id": "bRN3ZFjpfqZW231JLyLPSsSTzsIu",
                    "username": "user",
                    "email": "user@gmail.com",
                }
            }
        }

class RequestLogin(BaseModel):
    email: EmailStr
    password: constr()

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@gmail.com",
                "password": "securepassword",
            }
        }

class ResponseLogin(BaseModel):
    message: constr()
    data: GetUserData
    access_token: constr()

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Login successful",
                "data": {
                    "user_id": "bRN3ZFjpfqZW231JLyLPSsSTzsIu",
                    "username": "user",
                    "email": "user@gmail.com",
                },
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            }
        }

class CreateUserDetail(BaseModel):
    name: constr(pattern="^[A-Za-z][A-Za-z\s]{0,9}$")
    age: int
    gender: constr(pattern="^(Male|Female)$")
    contactNumber: constr(pattern="^628[1-9]{10}$")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "example_name",
                "age": 20,
                "gender": "Male",
                "contactNumber": "628123456789",
            }
        }

class EditProfile(BaseModel):
    name: constr(pattern="^[A-Za-z][A-Za-z\s]{0,9}$")
    gender: constr(pattern="^(Male|Female)$")
    contactNumber: constr(pattern="^628[1-9]{10}$")
    age: int

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "gender": "Male",
                "contactNumber": "6281234567890",
                "age": 25,
            }
        }

class UpdatePassword(BaseModel):
    oldPassword: constr()
    newPassword: constr()
    confirmNewPassword: constr()

    class Config:
        json_schema_extra = {
            "example": {
                "oldPassword": "currentpassword",
                "newPassword": "newsecurepassword",
                "confirmNewPassword": "newsecurepassword",
            }
        }
