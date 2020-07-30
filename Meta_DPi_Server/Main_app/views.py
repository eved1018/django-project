from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .forms import PDBForm



def predition_score_get():
    # this is where we will get the three prediction scores and combine them into a dataframe with residue as index  
    pass
def Meta_DPI():
    # this will take in the dataframe of the three predictiors and perform the Logreg and RF 
    # I (evan) will do this 
    pass

def Meta_DPI_Setup(pdb,chain):
    # this is where we will do the RF/Logreg data and return the resulst to the results page 
    # as well as run the ROC and return the ROC figure 
    predition_score_get()
    Meta_DPI()
    results = pd.DataFrame()
    results["col1"] = ["1","2",'3']
    results["col2"] = ["1","2",'3']
    results = results.to_html(index=False)
    tree = '/Users/evanedelstein/Desktop/Research_Evan/Raji_Summer2019_atom/Data_Files/CrossVal_logreg_RF/5foldCV/Crossvaltest47/Trees/Rftree_CV1.svg'
    return results,tree



def home(request):
    
    req = request
    form = PDBForm(request.POST)
    error_message = ""
    if request.method == "POST" and form.is_valid():
        pdb = form.cleaned_data['pdb']
        if len(pdb) == 4:
            chain = None
            results,tree = Meta_DPI_Setup(pdb,chain)
            context = {'results' : results,'tree' : tree}
            return render(request,'Main_app/Results.html' ,context)
        elif len(pdb) == 6:
            if "_" in pdb:
                pdb_chain = pdb.split("_")
                pdb = pdb_chain[0]
                chain = pdb_chain[1]
                results,tree = Meta_DPI_Setup(pdb,chain)
                context = {'results' : results,'tree' : tree}
                return render(request,'Main_app/Results.html' ,context)
                
            if "." in pdb:
                pdb_chain = pdb.split("_")
                pdb = pdb_chain[0]
                chain = pdb_chain[1]
                results,tree = Meta_DPI_Setup(pdb,chain)
                context = {'results' : results,'tree' : tree}
                return render(request,'Main_app/Results.html' ,context)
        else: 
            error_message = "PDb id is not known "
    
    form = PDBForm
   
    return render(request,'Main_app/home.html',{'title':home ,'form': form , 'error_message': error_message  } )


    
def Results(request): 
    return render(request,'Main_app/Results.html')
    
    

def About(request):
    return render(request,'Main_app/about.html')
    


