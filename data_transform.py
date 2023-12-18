import pandas as pd

# Takes the csv file and converts data 
class DataTransform:
    @staticmethod
    def convert_to_datetime(df, column_name):
        """ 
        Convert a column to datetime format.
        
        Parameters:
        - df: DataFrame
        - column_name: str, name of column to be converted.
        """
        df[column_name] = pd.to_datetime(df[column_name], format='%b-%Y')

    @staticmethod
    def convert_to_string(df, column_name):
        """ 
        Convert a column to a string.
        
        Parameters:
        - df: DataFrame
        - column_name: str, name of column to be converted.
        """
        df[column_name] = df[column_name].astype(str)

    @staticmethod
    def convert_to_float(df, column_name):
        """
        Convert a column to a float.

        Parameters:
        - df: DataFrame
        - column_name: str, name of column to be converted.
        """
        df[column_name] = df[column_name].astype(float)

    def employment_length_formatter(self, df, column_name):
        """
        Preprocess the 'employment_length' column.

        Parameters:
        - df: DataFrame
        - column_name: str, name of the column to be processed
        """
        def preprocess(value):
            # Replace '10+ years' with '10 years'
            df[column_name] = df[column_name].replace('10+ years', '10 years')
            
            # Replace '<1 year' with '0 years'
            df[column_name] = df[column_name].replace('<1 year', '0 years')
            
            # Remove the word 'years' from other entries
            df[column_name] = df[column_name].str.replace(' years', '', regex=False)
            
            # You can convert the column to numeric if needed
            #df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        
        return df
        
        df[column_name] = df[column_name].apply(preprocess)
        return df