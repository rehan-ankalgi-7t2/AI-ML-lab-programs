import numpy as np
import pandas as pd
from pprint import pprint

data = pd.read_csv("Weather.csv")
data_size = len(data)
treenodes = []
tree = {
    "ROOT": data
}

def total_entropy(data, col):
    mydict = {}
    for elem in data[col]:
        if elem in mydict.keys():
            mydict[elem] += 1
        else:
            mydict[elem] = 1
    total = sum(mydict.values())
    E = 0
    for key in mydict.keys():
        E += entropy(mydict[key], total)
    return E

def entropy(num, denom):
    return -(num/denom)*np.log2(num/denom)

def get_stored_data(data, column):
    sort = {}
    for column_name in get_attributes(data, column):
        sort[column_name] = data.loc[data[column] == column_name]
    return sort

def get_attributes(data, column):
    return data[column].unique().tolist()

def info_gain(total_entropy, sorted_data, entropy_by_attribute):
    length = data_size
    total = 0
    for col, df in sorted_data.items():
        total += (len(df)/length)*entropy_by_attribute[col]
    return total_entropy - total

def get_entropy_by_attribute(sorted_data):
    entropies ={}
    for key, df in sorted_data.items():
        entropies[key] = total_entropy(df, 'Decision')
    return entropies

def drop_node(data, column):
    return data.drop(column, axis = 1)