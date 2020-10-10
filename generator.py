# generator.py

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
        '''

        '''

        mean = datag['mean']
        stdev = datag['stdev']
        samples = datag['samples']
        decimals = datag['decimals']
        
        nn = datag['number_of_numerical_features']
        nc = datag['number_of_categorical_features']

        ncats = datag['number_of_categories']
        
        
        df = pd.DataFrame()

        numerical_feature_names = ["NumericFeature " + str(x) for x in range(1,nn+1)]
        categorical_feature_names = ["CategoricFeature " + str(x) for x in range(1,nc+1)]


        for i in range(nn):
            numerical_feature_name = numerical_feature_names[i]
            df[numerical_feature_name] = self.get_numeric_data(mean, stdev, samples, decimals)
        
        for i in range(nc):
            categorical_feature_name = categorical_feature_names[i]
            df[categorical_feature_name] = self.get_categorical_data(ncats, 
                                                                    categorical_feature_name,
                                                                    samples)


        return df
        
    def get_numeric_data(self, mean, stdev, samples, decimals):
        return np.round(np.random.normal(mean, stdev, samples), decimals)

    def get_categorical_data(self, ncats, feature_name, samples):

        distribution = np.random.dirichlet(np.ones(ncats), size=samples)
        cats = [feature_name + " Cateogry " + str(x) for x in range(1,ncats+1)]
        
        return np.random.choice(a=cats, size=samples, p=distribution[0])
