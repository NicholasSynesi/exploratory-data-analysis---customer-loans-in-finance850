import pandas as pd
from scipy.stats import normaltest
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

class Plotter:
    def __init__(self, data):
        self.data = data

    def plot_null_values(self, column=None):
        """
        Shows the null values in either the entire DataFrame, or specific column.

        Parameters:
        - column: str, If not none, shows the null values for the column inputted.
        """
        plt.figure(figsize=(10, 6))
        if column is None:
            # Plot nulls for entire dataframe
            sns.heatmap(self.data.isnull(), cbar=False, cmap='viridis')
        else:
            # Plot nulls for specified column
            sns.heatmap(self.data[[column]].isnull(), cbar=False)
        
        plt.title(f'Null Values for {column if column else "Entire DataFrame"}')
        plt.show()

    def check_skew(self):
        """
        Checks the skew of all columns in a DataFrame that are type: float.

        Returns:
        - skew info: DataFrame with column names and their skew
        """
        # Create empty list to store the skew values
        skew_info = []

        for column in self.data.select_dtypes(include='float').columns:
            skew_value = self.data[column].skew()
            skew_info.append({'Column': column, 'Skewness': skew_value})
        
        # Sort from highest skew
        skew_info = sorted(skew_info, key=lambda x: x['Skewness'], reverse=True)

        return skew_info
    
    def check_outliers(self, column, method=None):
        """
        Function which looks for outliers in a given column. Allows for a choice to be made 
        in which visualization method is used.

        Parameters:
        - column: The column in the dataset you want to pick outliers from.
        - method: Shows either a boxplot, histogram, scatter, or zscore.

        Returns: The corresponding graph to the one specified in method, or a dataframe of the zscores.
        """
        if method == 'boxplot':
            plt.figure(figsize=(8,6))
            sns.boxplot(data=self.data[column])
            plt.show()
        
        if method == 'histogram':
            plt.figure(figsize=(8,6))
            sns.histplot(self.data[column], bins=40, kde=False)
            plt.show()

        if method == 'scatter':
            plt.figure(figsize=(18,16))
            sns.scatterplot(self.data[column])
            plt.show()
        
        if method == 'zscore':
            data_points = self.data[column]

            mean = np.mean(data_points)
            std = np.std(data_points)

            zscores = (data_points - mean) / std
            
            self.data['zscore'] = zscores

            # Get the largest zscores to identify as potential outliers

            largest_indices = np.argsort(np.abs(zscores))[-30:]
            largest_zscores = zscores[largest_indices]
            #largest_datapoints = data_points.iloc[largest_indices]
            return largest_zscores#, largest_datapoints


df = pd.read_csv('loan_payments_data.csv')

#nulls = Plotter(df)
#nulls.plot_null_values('last_payment_date')

class DataFrameTransform:
    def __init__(self, data):
        self.data = data

    def check_null_values(self):
        """
        Looks for null values in a DataFrame.

        Returns: The total number of null entries.
        """
        return self.data.isnull().sum()
    
    def drop_columns(self, columns_to_drop):
        """
        Drops a column from a DataFrame.

        Parameters:
        - columns_to_drop: str, the column that will be dropped from the DataFrame.
        """
        self.data = self.data.drop(columns=columns_to_drop, axis=1)
    
    def impute_missing_values(self, column_to_impute , method=None):
        """
        Imputes missing values in a column via a specified method.

        Parameters:
        - column_to_impute: str, the chosen column that will be imputed.
        - method: str, allows a method for imputation, either imputing by the median, mean, or mode.
        """

        if method == 'median':
            self.data[column_to_impute] = self.data[column_to_impute].fillna(self.data[column_to_impute].median())
        elif method == 'mean':
            self.data[column_to_impute] = self.data[column_to_impute].fillna(self.data[column_to_impute].mean())
        elif method == 'mode':
            self.data[column_to_impute] = self.data[column_to_impute].fillna(self.data[column_to_impute].mode())
        else:
            # Raise a value error if no valid method was specified
            raise ValueError("Please enter 'median', 'mean', or 'mode'")
    
    def correct_skew(self, column_to_correct, method=None, show_graph=False):
        """
        Corrects the skew of a column based on a chosen method.

        Parameters:
        - column_to_correct: str, the chosen column that will have the skew corrected.
        - method: str, the chosen method to correct skew. Can be log, boxcox, or yeojohnson
        - show_graph: bool, allows the graph to be shown of the corrected column, if desired.
        """
        if method == 'log':
            self.data[column_to_correct] = self.data[column_to_correct].map(lambda i: np.log(i) if i > 0 else 0)
            if show_graph == True:
                t = sns.histplot(self.data[column_to_correct], label="Skewness: %.2f"%(self.data[column_to_correct].skew()) )
                t.legend()

        elif method == 'boxcox':
            boxcox_plot = self.data[column_to_correct]
            boxcox_plot = stats.boxcox(boxcox_plot)
            boxcox_plot = pd.Series(boxcox_plot[0])
            if show_graph == True:
                t = sns.histplot(boxcox_plot,label="Skewness: %.2f"%(boxcox_plot.skew()) )
                t.legend()

        elif method == 'yeojohnson':
            yeojohnson_plot, _ = stats.yeojohnson(self.data[column_to_correct])
            self.data[column_to_correct] = pd.Series(yeojohnson_plot)
            if show_graph == True:
                t=sns.histplot(yeojohnson_plot,label="Skewness: %.2f"%(yeojohnson_plot.skew()) )
                t.legend()

