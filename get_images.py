#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## run
## > python get_images.py file_containing_url_csv
import csv
import requests
import os
import sys
import time
def put_images(FILE_NAME, search_term):
    urls=[]
    with open(FILE_NAME,newline="") as csvfile:
        doc=csv.reader(csvfile,delimiter=",")
        for row in doc:
            if row[1].startswith("https"):
                urls.append(row[1])
    if not os.path.isdir('flowers/' + search_term + '/'):
        os.mkdir('flowers/' + search_term + '/')
    t0=time.time()
    for url in enumerate(urls):
        print("Starting download {} of ".format(url[0]+1),len(urls))
        try:
            resp=requests.get(url[1],stream=True)
            path_to_write=os.path.join(os.getcwd(),'flowers/' + search_term + '/',url[1].split("/")[-1])
            outfile=open(path_to_write,'wb')
            outfile.write(resp.content)
            outfile.close()
            print("Done downloading {} of {}".format(url[0]+1,len(urls)))
        except:
            print("Failed to download url number {}".format(url[0]))
    t1=time.time()
    print("Done with download, job took {} seconds".format(t1-t0))
def main():
    FILE_NAME=sys.argv[1]
    search_term=sys.argv[2]
    put_images(FILE_NAME, search_term)
if __name__=='__main__':
    main()
