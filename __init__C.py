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

        emp = Employee(Id=315, Name="Zaeem", Age=22)
        session.add(emp)

        emp2 = Employee(329, "Ali", 25)
        emp3 = Employee(345, "Fawad", 30)

        session.add_all([emp2, emp3])

        return func.HttpResponse("Record created successfully", status_code=201)
    
    except Exception as e:
        return func.HttpResponse(f"Hello, Unable to execute successfully.", status_code=500)