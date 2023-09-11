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

        result = session.query(Employee).filter(Employee.name=='abc').first()
        result.name = "Muhammad"
        session.commit()
        print(result)
    
        return func.HttpResponse("Hello this HTTP triggered function executed successfully.", status_code=201)
    
    except Exception as e:
        return func.HttpResponse(f"Hello, Unable to execute successfully.", status_code=500)
