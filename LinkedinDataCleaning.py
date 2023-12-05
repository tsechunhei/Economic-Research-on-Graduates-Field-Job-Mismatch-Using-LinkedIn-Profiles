# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:25:06 2022

@author: VincentTse
"""

import requests
import os
import pandas as pd
import numpy as np
import time
import re



#fill na
df = df.fillna(value = np.nan)
df['fieldName'] = df['fieldName'].fillna(df['degreeName'])
df['fieldName2'] = df['fieldName2'].fillna(df['degreeName2'])

#drop nan rows
df = df[df['schoolName'].notna()]
df = df.dropna(subset=['degreeName','fieldName'], how= 'all')
df = df.dropna(subset=['currentComp','currentTitle'], how= 'all')
df = df.dropna(subset=['gradYear'])

#remove doctor
df = df[df['degreeName'].str.contains('doctor|PHD|博士|Ph.D|pgd|diploma|Associate|institute|Life Coaching|Classroom|certificate|Award|Executive Education', flags=re.IGNORECASE, regex=True) == False]

#Switch
df.loc[df.gradYear2 > df.gradYear,['schoolName','schoolName2']] = df.loc[df.gradYear2 > df.gradYear, ['schoolName2','schoolName']].values
df.loc[df.gradYear2 > df.gradYear,['degreeName','degreeName2']] = df.loc[df.gradYear2 > df.gradYear, ['degreeName2','degreeName']].values
df.loc[df.gradYear2 > df.gradYear,['fieldName','fieldName2']] = df.loc[df.gradYear2 > df.gradYear, ['fieldName2','fieldName']].values
df.loc[df.gradYear2 > df.gradYear,['gradYear','gradYear2']] = df.loc[df.gradYear2 > df.gradYear, ['gradYear2','gradYear']].values

#filter bachelors and masters
df.insert(loc = 0, column = 'is_Master', 
   value = list(df['degreeName'].str.contains('master|MBA|postgraduate|pgde|硕士|M.Sc.|MEcon|M.A.|MSc|研究生|碩士|mastor|mater|pcll|m.sc|post graduate|m.s.sc|M.Ed', flags=re.IGNORECASE, regex=True)
                .map({True: 1, False: 0})))

#clean non-master's pre-education
df.loc[df.is_Master ==0, ['schoolName2','degreeName2','fieldName2', 'gradYear2']] = np.nan


#filter out grad years
df = df[(df['gradYear'] == 2019) | (df['gradYear'] == 2020) | (df['gradYear'] == 2021)]
#############




#filter schools
schoolNameDict = {'Hkust':['香港科技大學', '香港科技大学','香港科大商學院', '香港科大商学院', 'technology', 'HKUST'],
                  'Hku':['The University of Hong Kong', '香港大學', '香港大学', 'hku', 'University of Hong Kong'],
                  'Cuhk':['香港中文大學','香港中文大学','The Chinese University of Hong Kong', 'CUHK', 'Chinese'],
                  'Cityu':['香港城市大學', '香港城市大学', 'city', 'City University of Hong Kong'],
                  'Polyu':['香港理工大學', '香港理工大学', 'The Hong Kong Polytechnic University', 'poly', 'Polytechnic'],
                  'Hkbu':['香港浸会大学','香港浸會大學', 'Hong Kong Baptist University', 'Baptist', 'bu', 'hkbu'],
                  'Lingu':['岭南大学', '嶺南大學','Lingnan University', 'lingnan','lingu'],
                  'Edu':['香港教育大學','香港教育大学','The Education University of Hong Kong', 'education','The educational University of Hong Kong']}


for key in schoolNameDict.keys():
    df.loc[df['schoolName'].str.contains(r"\b({})\b".format('|'.join(schoolNameDict[key])), case = False), 'schoolName'] = key
for key in schoolNameDict.keys():
    df.loc[df['schoolName2'].str.contains(r"\b({})\b".format('|'.join(schoolNameDict[key])), case = False,  na=False), 'schoolName2'] = key
    
df = df.loc[df['schoolName'].isin(schoolNameDict.keys())]




#filter sector
sectorDict = {'BusinessAdministration':['BBA', 'Human Resource', 'marketing', 'business','Logistics','Hotel', 'Supply Chain', 'Business Administration','Administration',
                                        'Meeting and Event Planning', 'Tourism and Events Management', 'Aviation Management','EMBA', 'Global Management','Global Operations',
                                        'Tourism Management','Entrepreneurship','Hospitality','人力資源管理','Advertising','Tourism','HRM','health and social services',
                                        'E-commerce','Global food safety management and risk analysis','商业和数据分析','Organizational Management','Administración y gestión de empresas, general',
                                        'Real Estate','Housing Management','市场','房地产','工商','MBA','Health Services','市場','Operation Management'],
              'Accounting/Economics/Finance':['economics', 'bank', 'finance', 'financial', 'fin', 'account', 'investment', 'asset', 'fintech',
                                              '经济学','金融工程','會計學系','会计及金融','金融', 'Financial Engineering','Wealth Management','Fianance','Accoutancy','Insurance',
                                              'Compliance','投资','MEcon'],
              'IT/Computer':['information', 'fintech', 'software', 'computing', 'computer science', 'System', 'programming','計算機科學系',
                             'technology', 'Networks', 'Information Engineering', 'Information Technology', 'computer engineering','Computering','系统','科技','Computer Scie'],
              'Statistics/DataScience':['Operation Research','data science', 'statistics','Analytics','Risk Management', 'Data', 'Actuarial','fintech', 'AI', 'Risk and Insurance',
                                        'Insurance','统计学','数据分析','精算','数量分析','Deep Learning'],
              'Art':['english', 'chinese', 'china', 'literature','Communication', 'Speech-Language', 'Liberal Arts', 'piano', 
                     'Linguistics','History','Human and organizational development','Organizational Leadership and International Development','Humanities',
                     'cultural','Translation', 'French', 'German','Art','語言學','Anthropology','翻譯學系','Creative','music','Child and family','Buddhist','Philosophy','语言学',
                     'Language'],
              'Public/SocialScience':['Psychology', 'politic', 'public','社會科學','Criminology','Policy','Social science', 'Sociology',
                                      'Governance','Government','International/Global Studies','Sports and Leisure Management','大中华','Social Work',
                                      'PR and Advertising','Geography','Psyhcology','Architecture','Surveying','社会学','Sports coaching','Counselling','health and social services',
                                      'Real Estate','Urban Planning','Behavioral Health','Urban','Environment'],
              'Engineering':['engineering','電機工程學系','Engineer','電子及計算機工程學系','電子工程學系','電子計算學系','機械工程'],
              'Education':['education','Teaching','General Studies','教育學系','教育'],
              'Media/Design':['media','journalism','Fashion', 'design', 'Visual','Video','Digital','Creative','film','国际新闻','Meida'],
              'Science':['math', 'chem', 'bio', 'physics','biotech', 'life science', 'nutrition', 'Biochemistry', 'Geosciences' , 'Bachelor of Science','生物学','数学',
                         'Atmospheric Envirionmental Science','Cognitive Neuroscience','Construction','Geomatics'],
              'Medical':['nurse', 'nursing','medical', 'dental','Medicine','Pharma','生物医学'],
              'Law':['law','Legal','LLB','PCLL','Arbitration and Dispute Resolution','Human Rights','Arbitration & Dispute Resolution','MCL']
               }



pos = 4
for key in sectorDict.keys():
    pos += 1
    df.insert(loc = pos, column = 'is_' + key, 
      value = list(df['fieldName'].str.contains(('|'.join(sectorDict[key])), case = False)
                   .map({True: 1, False: 0})))
    
df.insert(loc = pos +1, column = 'num_Field', value = list(df.iloc[:,5] + df.iloc[:,6] + df.iloc[:,7] + df.iloc[:,8] + df.iloc[:,9] + df.iloc[:,10]
                                                            + df.iloc[:,11] + df.iloc[:,12] + df.iloc[:,13] + df.iloc[:,14] + df.iloc[:,15]
                                                            + df.iloc[:,16]))
############



df.to_csv('data.csv')
df.to_excel('data.xlsx')
df.to_excel('1.xlsx')



























####
demo = pd.read_excel(r'C:\Users\VincentTse\Desktop\demo.xlsx')


###Secotor
demo.dtypes
pos = 4
for key in sectorDict.keys():
    pos += 1
    demo.insert(loc = pos, column = 'is_' + key, 
      value = list(demo['fieldName'].str.contains(('|'.join(sectorDict[key])), case = False)
                   .map({True: 1, False: 0})))
    



#######

    
#check
schoolName 
degreeName 
fieldName 
gradYear 

numExp 
currentComp 
currentTitle
allComp 
allTitle  

numCert 
allCert 
numVolun 
allVolun 
numConnect 

print(
len(schoolName),   
len(degreeName),
len(fieldName),
len(gradYear),
len(numExp),
len(currentComp),
len(currentTitle),
len(allComp),
len(allTitle),
len(numCert),
len(allCert),
len(numVolun),
len(allVolun),
len(numConnect)
)
