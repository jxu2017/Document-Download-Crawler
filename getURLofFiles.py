#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:08:57 2021

@author: JXu
"""



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from sys import platform
from tqdm import tqdm
import json
import getopt
import sys
import time
import pandas as pd
from threading import Thread
from datetime import datetime
import time
import csv
from csv import reader
import requests
from fake_useragent import UserAgent


def openChromeDriver():
    # Open chromedriver
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    
    
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument("blink-settings=imagesEnabled=false")
    ua = UserAgent()
    chrome_options.add_argument("user-agent={}".format(ua.random))

    if platform == "linux":
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    return driver


def getHtml(cur_html):
    driver = openChromeDriver()
    driver.get(cur_html)
    # #str_keyWords = [placename, address]
    # #KEYWORDS = ''
    # #cur_html = "https://www.sec.gov/cgi-bin/srch-edgar?text=form-type%3Dabs-ee+and+filing-date%3D202101*&first=2021&last=2021"
    
    # #dic = []
    # dic_page = []
    # dic_page.append(cur_html)
    
    # page_links = driver.find_elements_by_xpath("/html/body/div/center[1]/a")
    # for l in page_links:
    #     dic_page.append(l.get_attribute("href"))
       
    # driver.close()    
    # dic_page.pop(len(dic_page)-1)
    
    
    # for ll in dic_page:
        
       # Cdriver = openChromeDriver()
       #Cdriver.get(ll)
    #continue_links = driver.find_elements(By.XPATH, '//a')
    #//*[@id="formDiv"]/div/table/tbody/tr[3]/td[3]/a
    #//*[@id="formDiv"]/div/table/tbody/tr[4]/td[3]/a
    #//*[@id="formDiv"]/div/table/tbody/tr[2]/td[3]/a
    #//*[@id="formDiv"]/div/table/tbody/tr[5]/td[3]/a
    continue_link1 = driver.find_element_by_xpath("//*[@id='formDiv']/div/table/tbody/tr[3]/td[3]/a")
    continue_link2 = driver.find_element_by_xpath("//*[@id='formDiv']/div/table/tbody/tr[4]/td[3]/a")
    continue_link3 = driver.find_element_by_xpath("//*[@id='formDiv']/div/table/tbody/tr[2]/td[3]/a")
    continue_link4 = driver.find_element_by_xpath("//*[@id='formDiv']/div/table/tbody/tr[5]/td[3]/a")
    continue_link = ""
    if "xml" in continue_link1 and "102" in continue_link1:
        continue_link = continue_link1
    if "xml" in continue_link2 and "102" in continue_link2:
        continue_link = continue_link2
    if "xml" in continue_link3 and "102" in continue_link3:
        continue_link = continue_link3
    if "xml" in continue_link4 and "102" in continue_link4:
        continue_link = continue_link4
    if continue_link == "":
        return cur_html, cur_html
    url = continue_link.get_attribute("href")
    print(url)
    #cnt =0
    # for link in continue_links:
        
    #     cnt = cnt + 1
    #     if cnt < 81:
            
    #         dic.append(link.get_attribute("href"))
    #       #cnt = cnt + 1
    # print("page" +str(page) + "has"+str(cnt) + "files")
    # print("len is" + str(len(dic)))
    
    driver.close()
    file_name_arr = url.split("/")
    file_name=file_name_arr[len(file_name_arr)-1]
    return url, file_name
    
    #print(len(dic))

# company = ""  
# try:
#     searchbox = driver.find_element_by_css_selector("input#company")
#     searchbox.send_keys(company_name)   
# except:
#     time.sleep(3)
#     try:
#         searchbox = driver.find_element_by_css_selector("input#searchboxinput")
#         searchbox.send_keys(company_name) 
#     except:
    
#        # errorCase(placename, Store_ID, address,"searchboxinput")
#         driver.close()
#         return
    

# try:
#    searchbutton = driver.find_element_by_css_selector("button#search_button")
#    driver.execute_script("arguments[0].click()",searchbutton)
# except:
#     #errorCase(placename, Store_ID, address,"searchbox-searchbutton")
#     driver.close()
#     return 
# time.sleep(2)
#html = "https://www.sec.gov/cgi-bin/srch-edgar?text=form-type%3Dabs-ee+and+filing-date%3D{year}{month}*&first={year}&last={year}"
#html = "https://www.sec.gov/Archives/edgar/data/1699462/000105640419003967/0001056404-19-003967-index.htm"
#months = ["01","02","03","04","05","06","07","08","09","10","11","12"]


# dic = []
# #dicx = ["aaa","bbb"]
# for i in range(0,231):
    
#     num = i*80 + 1
        
#     new_html = html.format(number = num)
# new_url,cur_name = getHtml(html)
    
# driver = openChromeDriver()
# url = "https://www.sec.gov/Archives/edgar/data/1347185/000134718520000038/exh103loanv2.xml"
# r = requests.get(url)
# #r = requests.get(new_url)
# with open("hhx.xml","wb") as f:
#     f.write(r.content)
dic = []
with   open('target_urls_final2.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        url = row[0]
        file_url,file_name = getHtml(row[0])
        cur = {}
        cur["page_url"] = url
        cur["file_url"] = file_url
        cur["file_name"] = file_name
        dic.append(cur)
        
fields =["page_url","file_url","file_name"]
with open("test3.csv", 'w') as csvfile:
    
  
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)
  
   
    writer.writeheader()
       
      
    # writing data rows
    writer.writerows(dic)
    

