from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from confy.settings import DATABASES

engine_host = DATABASES['default']['HOST']
engine_port = str(3306)
engine_user = DATABASES['default']['USER']
engine_password = DATABASES['default']['PASSWORD']
engine_type = 'mysql'
engine_db = DATABASES['default']['NAME']
engine_data = engine_type + '://' + engine_user + ':' + engine_password + '@' + engine_host + ':' + engine_port + '/' + engine_db
engine = create_engine(engine_data, echo=True)
session = scoped_session(sessionmaker(bind=engine))
metadata = MetaData()
Base = declarative_base(metadata=metadata)
Base.query = session.query_property()

