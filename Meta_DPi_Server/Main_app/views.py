from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create your views here.



def home(request):
    return render(request,'Main_app/home.html',{'title':home} )

def Meta_DPI():
    # this is where we will do the RF/Logreg data and return the resulst to the results page 
    # as well as run the ROC and return the ROC figure 
    results = pd.DataFrame()
    results["col1"] = ["1","2",'3']
    results["col2"] = ["1","2",'3']
    tree = '/Users/evanedelstein/Desktop/Research_Evan/Raji_Summer2019_atom/Data_Files/CrossVal_logreg_RF/5foldCV/Crossvaltest47/Trees/Rftree_CV1.svg'
    return results,tree

    
def Results(request): 
    # takes the data frame and turns it into HTML and diplays it on teh resulst page. 
    # the to_html() also work son matplotlib figures so the ROC chart can be diplayed the same way
    results, tree = Meta_DPI()
    results = results.to_html(index=False)
    context = {'results' : results,
    'tree' : tree
    }

    return render(request,'Main_app/Results.html' ,context)
    
def About(request):
    return render(request,'Main_app/about.html')
    


