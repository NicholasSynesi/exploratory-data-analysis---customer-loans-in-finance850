import yaml
from sqlalchemy import create_engine
import pandas as pd

def load_yaml():
    with open('credentials.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_engine()
    
    def create_engine(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")
        return engine

    def extract_data(self):
        query = "SELECT * FROM loan_payments"
        df = pd.read_sql(query, self.engine)
        return df
    
    def save_to_csv(self, df, filename):
        df.to_csv(filename, index=False)

credentials = load_yaml()
rds_connector = RDSDatabaseConnector(credentials)
data = rds_connector.extract_data()
rds_connector.save_to_csv(data, 'loan_payments_data.csv')
        
        

