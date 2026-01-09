# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi import FastAPI

# app = FastAPI

# @app.post("/login")

# def login(
#     form : OAuth2PasswordRequestForm = Depends(),
#     sessions : Session = Depends(get_session)
# ):
#     user = session.exec(
#         select(User).where(User.email == form.username)
#     ).first()

#     if not user or not verify_pass(form.password, user.hashed_pass):
#         raise HTTPException(status_code = 401, detail = "Invalid Credntails")
    
#     token = create_access_token({"sub":user.email})
#     return {"access_token" : token, "token_taken" : "bearer"}

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import SQLModel, Field, Session, create_engine, select
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

# -------------------- CONFIG --------------------

SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE_URL = "sqlite:///users.db"

# -------------------- APP --------------------

app = FastAPI(title="JWT Login System")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# -------------------- DATABASE --------------------

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = True


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

# -------------------- PASSWORD HASHING --------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

# -------------------- JWT --------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# -------------------- SCHEMAS --------------------

class RegisterRequest(SQLModel):
    email: str
    password: str

# -------------------- ROUTES --------------------

@app.on_event("startup")
def on_startup():
    create_db()

# REGISTER
@app.post("/register")
def register(
    data: RegisterRequest,
    session: Session = Depends(get_session)
):
    user_exists = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    session.add(user)
    session.commit()
    return {"message": "User registered successfully"}

# LOGIN
@app.post("/login")
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.email == form.username)
    ).first()

    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({"sub": user.email})
    return {
        "access_token": token,
        "token_type": "bearer"
    }

# PROTECTED ROUTE
@app.get("/profile")
def profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_active": current_user.is_active
    }
