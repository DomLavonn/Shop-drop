from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class databas:

    #creating engine
    engine = create_engine("sqlite:///storeDB.db", echo=True)

    #Executre commands on database with sessions (sessionmaker) and use sessionf for orm
    Session = sessionmaker(bind=engine) 
    session = Session()

    