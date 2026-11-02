
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dburl = "postgresql+psycopg2://postgres:1234@localhost:5432/fastapi_demo"   
engine = create_engine(dburl)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   