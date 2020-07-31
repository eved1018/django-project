from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .forms import PDBForm,FileForm
import os
from django.conf import settings


def handle_uploaded_file(datafile):
    pdbs= []
    with datafile.open('r') as f:
        lines = f.readlines()
        for line in lines:
            pdb = line.decode('utf8')
            pdbs.append(pdb)
        f.close()
    for pdb in pdbs:
        pdb = pdb.rstrip("\n")
        context = Parser(pdb)
    return context 
    

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
    return results, tree

def Parser(pdb):
    # parses pdb input will display error if _ or . isnt used or pdb is too big/ to short need to add lookup from RCBS 
    error_message= ""

    if len(pdb) == 4:
        
        chain = None
        results,tree = Meta_DPI_Setup(pdb,chain)
        context = {'results' : results,'tree' : tree}
        return context
    elif len(pdb) == 6:
        
        if "_" in pdb:
            
            pdb_chain = pdb.split("_")
            pdb = pdb_chain[0]
            chain = pdb_chain[1]
            results,tree = Meta_DPI_Setup(pdb,chain)
            context = {'results' : results,'tree' : tree}
            return context
            
        if "." in pdb:
            
            pdb_chain = pdb.split("_")
            pdb = pdb_chain[0]
            chain = pdb_chain[1]
            results,tree = Meta_DPI_Setup(pdb,chain)
            context = {'results' : results,'tree' : tree}
            return context
    else: 
        error_message = "PDb id is not known "
        results = ""
        context = {'results': results ,'error_message': error_message}
        return context



def home(request):
    form = PDBForm(request.POST)
    file_form = FileForm(request.POST)
    error_message = ""
    if request.method == "POST" and form.is_valid():
        pdb = form.cleaned_data['pdb']
        context = Parser(pdb)
        return render(request,'Main_app/Results.html' ,context)
    elif request.method == 'POST' and request.FILES:
        file_form = FileForm(request.POST, request.FILES)
        datafile = request.FILES['file']
        context  = handle_uploaded_file(datafile)
        return render(request,'Main_app/Results.html' ,context)
    
    form = PDBForm
    file_form = FileForm
    return render(request,'Main_app/home.html',{'title':home ,'form': form ,'form2':file_form, 'error_message': error_message  } )


    
def Results(request): 
    return render(request,'Main_app/Results.html')
    
    

def About(request):
    return render(request,'Main_app/about.html')
    


