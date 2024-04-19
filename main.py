from sqlalchemy import create_engine, MetaData, Column, Integer, String, DateTime, Boolean, Table, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests

# from dbCredentialsModel import *
#
# if __name__ == '__main__':
#     dbCredentials = dbCred('sa', 'wkdm#63349D', '192.168.254.230\\HOMOLOGACAO:50066', 'YAMCOLNET')
#     engine = create_engine(
#         'mssql+pyodbc://{0}:{1}@{2}/{3}?driver=ODBC+Driver+17+for+SQL+Server'.format(dbCredentials.user, dbCredentials.password, dbCredentials.host, dbCredentials.table))
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     metadata = MetaData()
#     table = Table('varejonline_parametros', metadata, autoload_with=engine)
#     result = session.query(table).filter_by(id=1).first()
#     session.close()