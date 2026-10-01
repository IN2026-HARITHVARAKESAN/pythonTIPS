"""This file contains samples and finds z score for each samples"""
from sklearn.datasets import load_iris

import numpy as np

# Loading the Iris dataset

iris = load_iris()

data = iris.data

feature_names = iris.feature_names

def z_score(data_dictinary_list:list)-> None:
    mean = {
        feature : np.mean([sample[feature] for sample in data_dictinary_list]) for feature in feature_names
    }
    
    deviation = {
        feature : np.std([sample[feature] for sample in data_dictinary_list]) for feature in feature_names
    }

    return [
        {
            feature: (sample[feature] - mean[feature])/deviation[feature] if deviation[feature]!=0 else 0
            for feature in feature_names
        }
        for sample in data_dictinary_list
    ]

data_dictinary_list = [{feature_names[i]:sample[i] for i in range(len(sample))} for sample in data ]

print(z_score(data_dictinary_list))