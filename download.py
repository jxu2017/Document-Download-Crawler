#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:08:57 2021

@author: JXu
"""




import time
import csv
from csv import reader


import requests

urls = []
with   open('file_urls.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        urls.append(row[1])
print(urls[0])
#for line in  open('file_urls.csv', 'r'):
#    csv_row = line.split()
#    print(csv_row)
   # urls.append(csv_row[1])
   # reader = csv.reader(f, delimeter ="\t")
    

proxy = {
    "https": 'https://20.206.67.142:8888',
    "http": 'https://20.206.67.142:8888' 
}  
header ={"User-Agent":"University of XXXX at XXXX XXXX@XXXXX.edu", "Accept-Encoding":"gzip, deflate","Host":"www.sec.gov"}
#cnt = 500   
file_name_format = "./data17501_17800/file_{num}.xml" 
for i in range(17501, 17801):
    #if cnt > 0:
    #    break
    if i == 0:
        continue
    url = urls[i]
    #cnt = cnt+1
    time.sleep(3)

    file_name =file_name_format.format(num = i)
    r = requests.get(url, headers = header)
    #r = requests.get(new_url)
    with open(file_name,"wb") as f:
        f.write(r.content)