# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:08:38 2022

@author: VincentTse
"""


import pandas as pd
import bs4 as bs
from selenium import webdriver
import requests
import time
import concurrent.futures
import re

u = [  
       'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101409',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101444',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100990',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100189',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101475',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101423',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100784',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100773',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101407',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100564',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100115',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101465',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=100184',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101422',
        'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&facetFieldOfStudy=101001',
        
            'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101409',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101475',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101444',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101407',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100189',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101423',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100140',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100176',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100784',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101422',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100564',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100990',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100773',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=101465',
         'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&facetFieldOfStudy=100142',
         
        'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=101444',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=101409',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100189',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100784',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100990',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100351',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100176',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100360',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100693',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=101407',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=101422',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=101475',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100432',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100347',
       'https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&facetFieldOfStudy=100773',
       
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101409',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100140',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101475',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101444',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101407',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100143',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101423',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100773',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101422',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101460',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100990',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100189',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100115',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=100784',
        'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&facetFieldOfStudy=101465',
                 'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101409',
                 
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101475',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101444',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101423',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101422',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100990',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101407',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100773',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100456',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101465',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=101460',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100981',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100780',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100115',
         'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&facetFieldOfStudy=100582',
         
         'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100232',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100582',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100115',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100912',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100287',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100773',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100981',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100583',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100283',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100461',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100693',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=100179',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=101409',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=101150',
       'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&facetFieldOfStudy=101905',
       
                'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101409',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101475',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101407',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101423',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101115',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=100773',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101411',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101452',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=100351',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101422',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=100360',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101444',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=100176',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101451',
         'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&facetFieldOfStudy=101426',

       
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101409',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100990',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101444',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100564',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100189',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101407',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100784',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101426',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101475',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100773',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101001',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100115',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=100568',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101768',
       'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&facetFieldOfStudy=101465'
     ]

m = ['https://www.linkedin.com/school/hkust/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/the-chinese-university-of-hong-kong/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/universityofhongkong/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/hong-kong-polytechnic-university/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/cityu/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/the-hong-kong-institute-of-education/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/lingnan-university/people/?educationEndYear=2021&keywords=master',
     'https://www.linkedin.com/school/hong-kong-baptist-university/people/?educationEndYear=2021&keywords=master'
     ]

def scroll():

    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += 5
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position)) #scroll down slowly
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        print('finish scrolling')
        new_height = driver.execute_script("return document.body.scrollHeight") #calculate new height
    time.sleep(1)    
        
def scroll2():
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 5):
        
        driver.execute_script("window.scrollTo(0, {});".format(i))
        driver.implicitly_wait(5)
        
        
        
#driver
driver = webdriver.Chrome(r"C:\Users\VincentTse\Desktop\chromedriver.exe")

#login
driver.get('https://www.linkedin.com/uas/login')
driver.implicitly_wait(3)
file = open(r'C:\Users\VincentTse\config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
elementID = driver.find_element_by_id('username')
elementID.send_keys(username)
elementID = driver.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()


links = []
#start
for i in m:
    driver.get(i)
    time.sleep(3)
    scroll()
    
############################
    parent = driver.find_element_by_css_selector("div.scaffold-finite-scroll__content")
    
    for i in range(1,len(parent.find_elements_by_tag_name("li"))):
        prefixes = ["’19","’20","’21"]
        try:
            if driver.find_elements_by_css_selector("div.scaffold-finite-scroll__content li:nth-of-type({}) .truncate".format(i))[0].text.startswith(tuple(prefixes)):
                print(driver.find_elements_by_css_selector("div.scaffold-finite-scroll__content li:nth-of-type({}) .truncate".format(i))[0].text)
                links.append(driver.find_elements_by_css_selector("div.scaffold-finite-scroll__content li:nth-of-type({}) [href]".format(i))[0].get_attribute('href'))
        except:
            continue
    print('length is ' + str(len(links)))
###################################
#links
#second time #

df = pd.DataFrame(links)

df_py.to_csv('links_py.csv')
df_nopy.to_csv('links_nopy.csv')