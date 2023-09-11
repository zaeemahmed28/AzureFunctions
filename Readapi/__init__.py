from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import azure.functions as func
from ..Models.models import Employee


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        Server = 'localhost'
        Database = 'AdventureWorks2022'
        Driver = 'ODBC Driver 17 for SQL Server'
        conn_string = f'mssql://@{Server}/{Database}?driver={Driver}'
        engine = create_engine(conn_string)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = session.query(Employee).all()
        for r in result:
            print(r.id, r.name, r.age)
        #result = [f"ID: {item.id}, Name: {item.name}, Age: {item.age}" for item in result]
        return func.HttpResponse(f'result:{result}')

    except Exception as e:
        return func.HttpResponse(f"Hello, Unable to execute successfully.", status_code=500)


    

    
