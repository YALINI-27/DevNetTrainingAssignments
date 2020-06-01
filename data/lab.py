import json
import xml.etree.ElementTree as ET
import yaml
import unittest

def json_file():
    print("######### JSON ############# ")
    with open('db.json','r') as data : 
        data_json = json.load(data) 
        print (data_json)

def yml_file():
    print("########### YAML ############")
    with open('db.yml','r') as ymldata : 
        data_yml = yaml.safe_load(ymldata) 
        print(data_yml ) 

def xml_file():
    print("########## XML ##############")
    with open('db.xml','r') as xmldata : 
       tree = ET.parse(xmldata)
       root = tree.getroot()
       for i in root: 
           print(i.tag, i.attrib)
           for j in i :
               print(j.tag,int(j.text))


json_file()
yml_file()
print(xml_file())

