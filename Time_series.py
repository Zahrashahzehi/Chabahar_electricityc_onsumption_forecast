import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

data_Chabahar = pd.read_excel('FinalData.xlsx' , sheet_name='Chabahar')
data_Chabahar
data_Chabahar['Date'] = pd.to_datetime(data_Chabahar['Date'])
data_Chabahar.dtypes
