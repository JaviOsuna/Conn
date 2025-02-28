import os

from dotenv import load_dotenv

load_dotenv()

from typing import Optional

from sqlmodel import Session, Field, SQLModel, create_engine, select

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")


class Recipe2(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)


oracle_url = f"oracle+oracledb://{username}:{password}@{hostname}/{sid}"
engine = create_engine(oracle_url, echo=True)

SQLModel.metadata.create_all(engine)


def create_recipes():
    recipe1 = Recipe2(id=10, name="Tarta de queso")
    recipe2 = Recipe2(id=11, name="Tostada de trufa")

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
