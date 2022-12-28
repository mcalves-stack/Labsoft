from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


<<<<<<< HEAD
DATABASE_URL = "postgresql://postgres:246581@localhost/Labsoft"
=======
DATABASE_URL = "postgresql://dmucwcexjohaqw:6e7d6359d44c0f9c1c20fc81962726b244e6d6fd72841b2c237d48c0ed89086c@ec2-34-231-63-30.compute-1.amazonaws.com:5432/dev6fhb4o8n6l6"
>>>>>>> b60084d4a13e07c6ed1d9bc6f238e38da8d0ad60


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

