# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:32:00 2022

@author: VincentTse
"""

import requests
import os
import pandas as pd
import numpy as np
import time
import re


##
df_py = pd.read_csv(r'F:\HKU\5\ECON4200\Project\links_py.csv', index_col =0)
df_nopy = pd.read_csv(r'F:\HKU\5\ECON4200\Project\links_nopy.csv', index_col =0)
links_py = list(df_py['0'])
links_nopy = list(df_nopy['0'])
 

#Start
def api (links):
    
    global df
    schoolName = [] 
    degreeName = []
    fieldName = []
    gradYear = []
    
    schoolName2 = [] 
    degreeName2= []
    fieldName2 = []
    gradYear2 = []
    
    numExp = []
    currentComp = []
    currentTitle = []  
    allComp = []  
    allTitle = [] 
    
    numCert = []
    allCert = []
    numVolun = []
    allVolun = []
    numConnect = [] 
    
    #API setting
    PROXYCURL_API_KEY = '4059c43e-8b34-4b6f-89fd-748d2d5b12ba'  # todo - fill this field up
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    
    #lists

    
    for link in links:
        
        params = {
        'url': link,
        'use_cache': 'if-recent',
        'skills': 'exclude',
        'inferred_salary': 'exclude',
        'extra': 'exclude'}
        
        try:
            response = requests.get(api_endpoint,
                                params=params,
                                headers=header_dic)
        
            profile = response.json()
            
            while len(profile) == 1:
                print ('api error, try again')
                time.sleep(2)
                try:
                    response = requests.get(api_endpoint,
                                    params=params,
                                    headers=header_dic)
                    profile = response.json()
                except:
                    break
                
                else:
                    continue
    
        except:
            continue


              
        if len(profile) == 3:
        
            print('error')
            print('link is ' + link)
            
            #Edu
            schoolName.append(np.nan) 
            degreeName.append(np.nan) 
            fieldName.append(np.nan) 
            gradYear.append(np.nan) 
            
            #Work
            numExp.append(np.nan) 
            currentComp.append(np.nan) 
            currentTitle.append(np.nan) 
            allComp.append([]) 
            allTitle.append([]) 
            
            #Others
            numCert.append(np.nan) 
            allCert.append([]) 
            numVolun.append(np.nan) 
            allVolun.append([]) 
            numConnect.append(np.nan) 
                
        else:
            if profile['education'] != [] and profile['education'][0]['degree_name'] != None:
                schoolName.append(profile['education'][0]['school'])
                degreeName.append(profile['education'][0]['degree_name'])
                fieldName.append(profile['education'][0]['field_of_study'])
                if profile['education'][0]['ends_at'] != None:
                    gradYear.append(profile['education'][0]['ends_at']['year'])
                else:
                    gradYear.append(np.nan)
                
                if any(x in profile['education'][0]['degree_name'].lower() for x in 
                       ['master','mba','postgraduate','pgde','硕士','m.sc.','mecon','m.a.','msc','m.sc']) and len(profile['education']) >= 2:
                    schoolName2.append(profile['education'][1]['school'])
                    degreeName2.append(profile['education'][1]['degree_name'])
                    fieldName2.append(profile['education'][1]['field_of_study'])
                    if profile['education'][1]['ends_at'] != None:
                        gradYear2.append(profile['education'][1]['ends_at']['year'])
                    else:
                        gradYear2.append(np.nan)
                    
                    
                else:
                    schoolName2.append(np.nan) 
                    degreeName2.append(np.nan) 
                    fieldName2.append(np.nan) 
                    gradYear2.append(np.nan)
                    
            else:
                schoolName.append(np.nan) 
                degreeName.append(np.nan) 
                fieldName.append(np.nan) 
                gradYear.append(np.nan) 
            
            
            #Exp
            if profile['experiences'] != []:
                numExp.append(len(profile['experiences']))
                allComp.append([profile['experiences'][i]['company'] 
                                for i in range(len(profile['experiences']))])
                allTitle.append([profile['experiences'][i]['title'] 
                                for i in range(len(profile['experiences']))])
            else:
                numExp.append(np.nan) 
                allComp.append([]) 
                allTitle.append([]) 
            
            if profile['occupation'] != None:
                try:
                    currentComp.append(profile['occupation'].split(" at ", 1)[1])
                    currentTitle.append(profile['occupation'].split(" at ", 1)[0])
                except:
                    currentComp.append(profile['occupation'])
                    currentTitle.append(profile['occupation'])
            else:
                currentComp.append(np.nan) 
                currentTitle.append(np.nan) 
            #Others
            numCert.append(len(profile['certifications']))
            allCert.append([profile['certifications'][i]['name'] 
                            for i in range(len(profile['certifications']))])
            numVolun.append(len(profile['volunteer_work']))
            allVolun.append([profile['volunteer_work'][i]['title'] 
                            for i in range(len(profile['volunteer_work']))])
            numConnect.append(profile['connections'])
        
    
    df = pd.DataFrame(list(zip(schoolName,
                                   degreeName,
                                   fieldName,
                                   gradYear,
                                   schoolName2,
                                   degreeName2,
                                   fieldName2,
                                   gradYear2,
                                   numExp,
                                   currentComp, 
                                   currentTitle,
                                   allComp,
                                   allTitle, 
                                   numCert,
                                   allCert,
                                   numVolun,
                                   allVolun,
                                   numConnect)), columns = ['schoolName',
                                                            'degreeName',
                                                            'fieldName',
                                                            'gradYear',
                                                            'schoolName2',
                                                            'degreeName2',
                                                            'fieldName2',
                                                            'gradYear2',
                                                            'num_Exp',
                                                            'currentComp',
                                                            'currentTitle',
                                                            'allComp',
                                                            'allTitle',
                                                            'num_Cert',
                                                            'allCert',
                                                            'num_Volunteering',
                                                            'allVolunteering',
                                                            'num_Connect'])   
                                                   
    return (df)



##### 
   



















