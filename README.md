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

To install, clone the repo using the git clone https://github.com/NicholasSynesi/exploratory-data-analysis---customer-loans-in-finance850/tree/main .
To run, all .py files in the repository are essential. This is db_utils.py, data_imputer.py, data_info.py, data_transform.py. Additionally, all .ipynb files are needed, as these are where I talk through the process of EDA. Only one .csv file is needed, loan_payments_data.csv. The other files serve as a benchmark at the end of each .ipynb file where I save the word I've done, but they all naturally orginate from the inital file.

# Usage

To use this file, all that is needed is to run all cells in each .ipynb file. The first one is format_data.ipynb, and then the next file to go to is stated at the bottom of each of the .ipynb files. 

# File structure

All files are present in the same level in the repo

# License info 

MIT License

Copyright (c) [2023] [Nicholas Synesi]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
