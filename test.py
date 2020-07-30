
import pandas as pd
import numpy as np

def Meta_DPI():
    # this is where we will do the RF/Logreg data and return the resulst to the results page 
    results1 = pd.DataFrame()
    results1["col1"] = ["1","2",'3']
    results1["col2"] = ["1","2",'3']
    results2 = pd.DataFrame()
    results2["col1"] = ["4","5",'6']
    results2["col2"] = ["4","5",'6']
    results = [results1,results2]
    return results

def Results():
    results = Meta_DPI()
    context = {}
    key = 0
    for data in results:
        key += 1
        data_total =[]
        for i in range(data.shape[0]):
            to_append = data.iloc[i]
            data_total.append(to_append)
        keyi = f"{key}"
        context[keyi] = data_total
    print(context)
Results()