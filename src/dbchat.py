#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

hd = {
    "content-type":"application/json"
}

def db_update():
    ### Update data by method PUT ###
    return "PUT"

def db_insert(data_in):
    ### Insert data by method POST ###
    #rp = requests.post("http://10.17.2.210:5984/db-chat", headers=hd, data=json.dumps(data_in,ensure_ascii=False).encode('utf8')) 
    rp = requests.post("http://10.17.2.210:5984/db-chat", headers=hd, data=json.dumps(data_in)) 
    ## json.dumps(u"ทดสอบ", ensure_ascii=False).encode('utf8')
    return rp.status_code

def db_select(db_name, key_name):
    ### Select data by method GET ###
    rg = requests.get("http://10.17.2.210:5984/" + db_name + "/" + key_name)
    return rg.json()

def db_delete(self):
    ### Delete data by method DELETE ###
    return "DELETE"
