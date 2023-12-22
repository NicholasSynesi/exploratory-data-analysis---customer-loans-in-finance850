import pandas as pd
import numpy as np

class DataFrameInfo:
    
    @staticmethod
    def describe_df(df):
        """
        Describes the datatypes for each column.

        Parameters:
        - df: DataFrame

        Returns: dtypes of each column.
        """
        info = df.describe()
        return info
    
    @staticmethod
    def statistical_values(df):
        """
        Find the mean, median, and standard deviation for all columns in a DataFrame

        Parameters:
        - df: DataFrame

        Returns: DataFrame which contains the mean, median, and mode as columns.
        """
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        mean = df[numeric_columns].mean()
        median = df[numeric_columns].median()
        std = df[numeric_columns].std()

        result_df = pd.DataFrame({'Mean': mean, 'Median': median, 'Standard Deviation': std})

        return result_df
    
    @staticmethod
    def count_distinct_values(df):
        """
        Counts the distinct values in each column for a DataFrame.

        Parameters:
        - df: DataFrame

        Returns: A dictionary containing the column name and corresponding number of distinct values
        """
        distinct_values = {}

        for column in df.columns:
            unique_values = df[column].nunique()
            distinct_values[column] = unique_values
        
        return distinct_values
    
    @staticmethod
    def percentage_of_missing(df, threshold=None):
        """
        Describes the datatypes for each column.

        Parameters:
        - df: DataFrame
        - threshold: float, choose the minimum number of empty values. Common use case is to enter 0 to 
        ignore all columns with no missing values

        Returns: dtypes of each column.
        """
        percentage = df.isna().mean() * 100
        if threshold is not None:
            return percentage[percentage > threshold]
        else:
            return percentage

df = pd.read_csv('loan_payments_data.csv')

infomaker = DataFrameInfo()
result = infomaker.percentage_of_missing(df, 0)
print(result)