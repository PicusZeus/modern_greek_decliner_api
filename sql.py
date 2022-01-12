

from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite://data.db')
metadata = MetaData()

Base = declarative_base(metadata=metadata)































Base.