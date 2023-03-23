import os
import time
import boto3
import tabula
import datetime
# import schedule
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
from django.contrib import messages
import schedule





def download_files_by_lead(request):
    print("Hello1")
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        print("Hello2")
        bucket = 'digitizedfiles'
        lead_id = request.POST.get('id')
        s3 = boto3.resource('s3')
        objects_bank = s3.Bucket(bucket).objects.filter(Prefix=lead_id)
        result = ''
        for obj in objects_bank:
            try:
                # file = r'd:\bank\{}'.format(obj.key)
                file_name = obj.key
                #s3.Bucket(bucket).download_file(obj.key, r'D:\digitizedfiles\{}'.format(obj.key))  ###download file to bank folder
                s3.Bucket(bucket).download_file(obj.key, '/Users/Abhishek/Desktop/digitised/{}'.format(obj.key))

                s3.Object(bucket, obj.key).delete()  ### delete downloaded file from AWS
                result = 'Successfuly download files!'
                # with connection.cursor() as cursor:
                #      sql_query = "INSERT INTO a3_kit.downloaded_file_details(lead_id, file_name, date) VALUES(" + lead_id + ",'" + file_name + "'" + ", now() " + ");"
                #      cursor.execute(sql_query)
            except Exception as e:
                result = e

        # else:
        #     result = 'No Found, Please try again!'
        with connection.cursor() as cursor:
            sql_query = "SELECT COUNT(lead_id) AS count FROM a3_kit.downloaded_file_details  where lead_id=" + "'" + lead_id + "'" + ";"
            cursor.execute(sql_query)
            result_count = dictfetchall(cursor)

        return_data = addindatabasefromcsv(request)
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT dbs.lead_id, dbs.name,dbs.customer_id FROM a3_kit.los_did_cid_generation as dbs where dbs.lead_id=" + lead_id + ";")
            cust_details = dictfetchall(cursor)

    return JsonResponse(
        {"result": result, "count": result_count, "afterdownload": return_data, "cust_details": cust_details})


import pandas as pd
import glob
import numpy as np



def addindatabasefromcsv(request):
    lid = request.POST.get('id')
    #files = glob.glob(r'D:\digitizedfiles\\*')
    files = glob.glob('/Users/Abhishek/Desktop/digitised/*')
    list1 = []
    bank_updated_result = ''
    itr_updated_result = ''
    form16_challans_updated_result = ''
    form16_info_updated_result = ''
    form16_partb_updated_result = ''
    form16_quarters_updated_result = ''
    form26as_asseseedetails_updated_result = ''
    form26as_parta_updated_result = ''
    form26as_partb_updated_result = ''
    form26as_partc_updated_result = ''
    form26as_partd_updated_result = ''
    form26as_partg_updated_result = ''
    # print(files)
    for file in files:
        file2 = str(file).split('_')
        file1 = file2[len(file2) - 1][:1]

        if file1 == "b":
            reader = pd.read_csv(file)
            reader['Txn Date'] = pd.to_datetime(reader['Txn Date'], format="%d/%m/%Y")
            reader['Txn Date'] = reader['Txn Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            reader = reader.replace(np.nan, 'NA')
            reader['creation_time'] = datetime.datetime.now()

            reader['last_modification_time'] = datetime.datetime.now()
            reader['image_name'] = "asmfbejhb"
            reader['customer_id'] = 0
            reader['created_by_id'] = 1

            for i in range(len(reader)):
                row = reader.iloc[i]
                with connection.cursor() as cursor:
                    cursor.execute(
                        "insert into bank_bank(txn_date,description,cheque_number,debit,credit,balance,account_name,account_number,mode,entity,source_of_trans,sub_mode,transaction_type,bank_name,deal_id,creation_time,last_modification_time,image_name,customer_id,created_by_id) values(%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s,%s)",
                        row)
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT bank_name as sub_type,account_name as name,account_number as identifier from a3_kit.bank_bank as bk where deal_id=" + lid + " group by account_number;")
                bank_updated_result = dictfetchall(cursor)
            os.remove(file)
            continue;

       
    if len(bank_updated_result) > 0:
        for obj in bank_updated_result:
            obj["doc_type"] = "BANK"
            list1.append(obj)
    

    print(list1)
    return (list1)


schedule.every(1).minutes.do(addindatabasefromcsv)   ### frequency of code execution

while True:
    schedule.run_pending()
    time.sleep(1) 