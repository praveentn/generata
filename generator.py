# load libraries
import numpy as np
import pandas as pd

'''
var= np.round(np.random.normal(distribution mean, 
standard deviation, number of samples), 
number of digits after the decimal point)


# .5 is prob dist of 0 and 1
label = np.random.choice([0, 1], size=7000, p=[.5, .5]) 


'''

class Generator():
    def __init__(self):
        self.name = "gemerata"


    def get_dataframe(self, datag):

        mean = datag['mean']
        stdev = datag['stdev']
        samples = datag['samples']
        decimals = datag['decimals']
        
        nn = datag['number_of_numerical_features']
        nc = datag['number_of_categorical_features']

        df = pd.DataFrame()

        if not nc:
            for feature in range(nn):
                df[feature] = self.get_numeric_data(mean, stdev, samples, decimals)

        return df
        
    def get_numeric_data(self, mean, stdev, samples, decimals):
        return np.round(np.random.normal(mean, stdev, samples), decimals)
