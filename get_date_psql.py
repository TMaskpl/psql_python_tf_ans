#! /usr/bin/evn python3

from env import *

import psycopg2
import json
import os

### CONN TO PSQL
def get_connection():
    try:
        return psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
    except:
        return False

def get_customer(conn):
    curr = conn.cursor()
    curr.execute("SELECT id, nazwa FROM public.customer WHERE nazwa = 'TMaskPL';")
    data = curr.fetchall()

    list = []
    
    for row in data:
        id = row[0]
        nazwa = row[1]
        
        list.append({"id": id})
        list.append({"nazwa": nazwa})
    
    write_to_json(output_file, list)

    conn.close()


### JSON
def write_to_json(output_file, list):
    if os.path.exists(output_file):
        os.remove(output_file)
        
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(list, f, ensure_ascii=False, indent=4)

def get_json_data(output_file):
    with open(output_file) as json_data:
        data = json.load(json_data)
    print(data[1]["nazwa"])


### VARS
def get_customer_vars(conn, customer):
    curr = conn.cursor()
    curr.execute(f"SELECT id, nazwa FROM public.customer WHERE nazwa = {customer};")
    data = curr.fetchall()
    
    if os.path.exists(output_file_vars):
        os.remove(output_file_vars)

    list = []
    
    for row in data:
        id = row[0]
        nazwa = row[1]
        
        list.append(f"id: '{id}'\n")
        list.append(f"nazwa: '{nazwa}'\n")

    for l in list:
        with open(output_file_vars, 'a', encoding='utf-8') as f:
            f.write(l)
    
    conn.close()



### MAIN
if __name__=='__main__':
    conn = get_connection()
    # get_customer(conn)
    # get_json_data(output_file)
    get_customer_vars(conn, customer)
