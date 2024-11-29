import os

from dotenv import load_dotenv

load_dotenv()

from typing import Optional

from sqlmodel import Session, Field, SQLModel, create_engine, select

username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
hostname = os.getenv("POSTGRES_HOSTNAME")
port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DBNAME")


class Recipe3(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)


oracle_url = f"postgresql+psycopg://{username}:{password}@{hostname}:{port}/{db_name}"
engine = create_engine(oracle_url, echo=True)

SQLModel.metadata.create_all(engine)


def create_recipes():
    recipe1 = Recipe3(id=10, name="Tarta de queso")
    recipe2 = Recipe3(id=11, name="Tostada de trufa")

    with Session(engine) as session:
        session.add(recipe1)
        session.add(recipe2)

        session.commit()


def select_recipes():
    with Session(engine) as session:
        statement = select(Recipe2)
        results = session.exec(statement)
        for recipe in results:
            print(recipe)


create_recipes()
