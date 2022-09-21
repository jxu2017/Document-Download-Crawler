
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:14:36 2021

@author: JXu
"""
import xml.etree.ElementTree as ET
import csv


def toCSV(xml_file,csv_file,passcnt,fields, abs_ee_file, not_abs_ee):
    cnt =0
    tree = ET.parse(xml_file)
    root = tree.getroot()
    #print(root.attrib)
    all_assets = []
    name_of_file_arr = xml_file.split('/')
    name_of_file = name_of_file_arr[len(name_of_file_arr)-1]
    for child in root:
        #if child.find("obligorCreditScore") is None:
           # break
        asset ={}
        asset["xmlfilename"] = name_of_file
        for c in child:
            tagarr = []
            try:
                tagarr = c.tag.split("}")
            except:
                break
            if len(tagarr) < 2:
                break
                
            tag = c.tag.split("}")[1]
            
            #print(tag)
            #print(c.text())
            if tag in asset:
                content = asset[tag] + "#" + c.text
                asset[tag] = content
            else:
                asset[tag] = c.text
        if "obligorCreditScore" in asset and "vehicleModelName" in asset:
            all_assets.append(asset)
            cnt = cnt+ 1
    cur_fields =["file_name"] 
    cur_file_name = {}
    cur_file_name["file_name"] =name_of_file
        
    if cnt > 0:
        with open(abs_ee_file,'a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames = cur_fields,lineterminator = '\n')
            writer.writerow(cur_file_name)
    else:
        with open(not_abs_ee,'a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames = cur_fields,lineterminator = '\n')
            writer.writerow(cur_file_name)
        
            
            
        
    with open(csv_file, 'a') as csvfile:
        
      
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields,lineterminator = '\n')
      
       # writing headers (fields)
        if passcnt == 0:
            writer.writeheader()
            
          
        # writing data rows
        writer.writerows(all_assets)
    print(name_of_file+" end")
 
        
abs_ee_file = "target_files.csv"
not_abs_ee = "other_files.csv"

field_file = open('fields_name1.txt', 'r')
FLines = field_file.readlines()
fields = [];
for l in FLines:
    fields.append(l.strip())
print(fields)
file_name_format = "./data17501_17800/file_{num}.xml" 
csv_name = "result_17501_17800.csv"
curcnt =0
for i in range(17501,17801):
    file_name = file_name_format.format(num = i)
    toCSV(file_name, csv_name,curcnt,fields,abs_ee_file,not_abs_ee)
    curcnt =curcnt+1
    
    
    