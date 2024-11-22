import os

from dotenv import load_dotenv
import oracledb

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

recipe1 = Recipe2(1, "Patatas")
recipe2 = Recipe2(2, "Huevos")



oracle_url = f"oracle+oracledb://{username}:{password}@{hostname}/{sid}"
engine = create_engine(oracle_url, echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(recipe1)
    statement = select(Recipe2).where(Recipe2.id == 1)
    session.add(recipe2)
    res = session.exec(statement)
    for result in res:
        print(result)

    session.commit()
