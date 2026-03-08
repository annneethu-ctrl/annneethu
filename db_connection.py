from sqlalchemy import create_engine
import pymysql

def get_connection():
    engine = create_engine("mysql+pymysql://root:mysql@localhost/phonepe")
    return engine







