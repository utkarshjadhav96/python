from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas, security, auth
from app.db import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# --------------------------------------------------
# REGISTER USER
# --------------------------------------------------
@router.post("/register", response_model=schemas.UserInBase)
def register_user(
    user: schemas.UserIn,
    db: Session = Depends(get_db)
):
    # Check username
    if auth.get_user(db, username=user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    # Check email
    if db.query(models.User).filter(
        models.User.email == user.email
    ).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash password
    hashed_password = security.get_password_hash(user.password)

    # Create user model
    db_user = models.User(
        username=user.username,
        email=user.email,
        age=user.age,
        level=user.level,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# --------------------------------------------------
# LOGIN USER (JWT TOKEN)
# --------------------------------------------------
@router.post("/token", response_model=schemas.token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = auth.get_user(db, username=form_data.username)

    if not user or not security.verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    access_token = security.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
