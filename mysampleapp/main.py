import time
import traceback
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+pg8000://admin:admin@database:5432/mydb", pool_pre_ping=True, echo_pool="debug")
Session = sessionmaker(bind=engine)

def some_func(session):
    try:
        session.scalar(select([1]))
        session.commit()
    except Exception as e:
        # raising the exception, crashes the app, makes it restart
        # and restarting the app solves the connection issue
        traceback.print_exception(*sys.exc_info())

def main():
    session = Session()
    
    while True:
        some_func(session)
        time.sleep(5)


if __name__ == "__main__":
    main()