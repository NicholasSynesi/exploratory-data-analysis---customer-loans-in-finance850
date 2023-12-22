# exploratory-data-analysis---customer-loans-in-finance850

# Contents 

- Project Description
- Installation
- Usage
- File Structure
- License info

# Project Description

This project was to perform Exploratory Data Analysis on a large dataset related to customer loans in finance. This was a 3 step process. The first step was to extract information from the cloud by creating a class that connects to the database and extract the .csv file where the loan information was stored. 
Once the .csv file was obtained, I had to then fix any issues with the dataset. This included converting columns to the correct format, imputing missing values, transforming skewed columns, removing outliers, and dropping overly correlated columns. 
To perform these tasks I created two functions, one to plot data for visualizing the data, and one to then transform the columns. 

# Installation

To install, all .py files in the repository are essential. This is db_utils.py, data_imputer.py, data_info.py, data_transform.py. Additionally, all .ipynb files are needed, as these are where I talk through the process of EDA. Only one .csv file is needed, loan_payments_data.csv. The other files serve as a benchmark at the end of each .ipynb file where I save the word I've done, but they all naturally orginate from the inital file.
