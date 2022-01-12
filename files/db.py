from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import os
# SQLALCHEMY_DB_URL = os.environ.get('DATABASE_URL', 'postgres://greekdb:qwerty@localhost:5432/greekdb')
# #'postgres://greekdb:qwerty@localhost:5432/greekdb')
#
# engine = create_engine(SQLALCHEMY_DB_URL, convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
#
# Base = declarative_base()