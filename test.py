
import pandas as pd
import numpy as np
import mechanize
import requests
import shutil
import os 
import time


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
# Results()

def Ispred_get(pdb,chain):
    proteinname = pdb+'.'+chain
    print(proteinname)
    protein_ids = {}
    br = mechanize.Browser()
    br.set_handle_redirect(mechanize.HTTPRedirectHandler)
    br.open("https://ispred4.biocomp.unibo.it/welcome/default/index")
    # print(br.forms)
    br.select_form(action="#")
    FILENAME='./Meta_DPI_Server/Temp/PDBs/{}_{}.pdb'.format(pdb, chain)
    br.form.add_file(open(FILENAME), 'text/plain', FILENAME)
    br.form.set_all_readonly(False)
    br['ispred_chain'] = chain
    req = br.submit()
    html = str(br.response().readlines())
    jobid = html.find('jobid')
    jobid= html[jobid+6:jobid+42]
    protein_ids[proteinname] = jobid
    # print(protein_ids)
    for key in protein_ids:
        url = "https://ispred4.biocomp.unibo.it/welcome/default/index"
        br.open("https://ispred4.biocomp.unibo.it/ispred/default/searchjob")
        br.select_form(action="#")
        br['jobuuid'] = protein_ids[key]
        br.submit(type='submit')
        target_url = 'https://ispred4.biocomp.unibo.it/ispred/default/display_results.html?jobid={}'.format(jobid)
        output_directory = './Meta_DPi_Server/Temp/Ispred' 
        # print(target_url)
        result = None
        while result is None:
            try:
                br.open(target_url)
                r = requests.get('https://ispred4.biocomp.unibo.it/ispred/default/downloadjob?jobid={}'.format(jobid), stream=True,headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open("{}/{}_{}.txt".format(output_directory,pdb,chain), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                        result = 1
                else:
                    result = 1
                    print(r.status_code)
            except:
                pass
       
    
Ispred_get('1A2Y','C')

def Predus_get(pdb,chain):
    proteinname = pdb+'.'+chain
    print(proteinname)
    protein_ids = {}
    br = mechanize.Browser()
    br.set_handle_redirect(mechanize.HTTPRedirectHandler)
    br.open("https://honiglab.c2b2.columbia.edu/PredUs/index_omega.html")
    # print(br.forms)
    br.select_form(name='pdbfile')
    FILENAME='./Meta_DPI_Server/Temp/PDBs/{}_{}.pdb'.format(pdb, chain)
    br.form.add_file(open(FILENAME), 'text/plain', FILENAME)
    br.form.set_all_readonly(False)
    br['ispred_chain'] = chain
    req = br.submit()
    html = str(br.response().readlines())
    jobid = html.find('jobid')
    jobid= html[jobid+6:jobid+42]
    protein_ids[proteinname] = jobid
    # print(protein_ids)
    for key in protein_ids:
        url = "https://ispred4.biocomp.unibo.it/welcome/default/index"
        br.open("https://ispred4.biocomp.unibo.it/ispred/default/searchjob")
        br.select_form(action="#")
        br['jobuuid'] = protein_ids[key]
        br.submit(type='submit')
        target_url = 'https://ispred4.biocomp.unibo.it/ispred/default/display_results.html?jobid={}'.format(jobid)
        output_directory = './Meta_DPi_Server/Temp/Ispred' 
        # print(target_url)
        result = None
        while result is None:
            try:
                br.open(target_url)
                r = requests.get('https://ispred4.biocomp.unibo.it/ispred/default/downloadjob?jobid={}'.format(jobid), stream=True,headers={'User-agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    with open("{}/{}_{}.txt".format(output_directory,pdb,chain), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                        result = 1
                else:
                    result = 1
                    print(r.status_code)
            except:
                pass








