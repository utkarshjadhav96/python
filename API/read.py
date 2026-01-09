from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select

app = FastAPI(title="FastAPI + SQLModel Level 4")

# -------------------------------------------------
# Database
# -------------------------------------------------
DATABASE_URL = "sqlite:///heroes.db"
engine = create_engine(DATABASE_URL, echo=True)

# -------------------------------------------------
# Model
# -------------------------------------------------
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

# -------------------------------------------------
# Create tables
# -------------------------------------------------
SQLModel.metadata.create_all(engine)

# -------------------------------------------------
# Dependency
# -------------------------------------------------
def get_session():
    with Session(engine) as session:
        yield session

# -------------------------------------------------
# Create Hero
# -------------------------------------------------
@app.post("/heroes", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

# -------------------------------------------------
# Read Heroes
# -------------------------------------------------
@app.get("/heroes", response_model=list[Hero])
def get_heroes(session: Session = Depends(get_session)):
    return session.exec(select(Hero)).all()

# -------------------------------------------------
# Read Hero by ID
# -------------------------------------------------
@app.get("/heroes/{hero_id}", response_model=Hero)
def get_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# -------------------------------------------------
# Delete Hero
# -------------------------------------------------
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"message": "Hero deleted"}
