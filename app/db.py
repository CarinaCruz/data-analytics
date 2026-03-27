import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")  # e.g. mysql+mysqlconnector://user:pass@host:3306/dbname
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. See .env.example")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def execute_query(sql: str, limit: int = 100):
    # Executes a read-only query and returns rows and column names
    try:
        # pandas will use the SQLAlchemy connection under the hood
        df = pd.read_sql_query(text(sql), con=engine)
        if limit:
            df = df.head(limit)
        return df.to_dict(orient="records"), list(df.columns)
    except SQLAlchemyError as e:
        raise RuntimeError(f"Query execution failed: {e}")
