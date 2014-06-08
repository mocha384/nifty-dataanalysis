import urllib2
import os.path as path
import numpy as np
import csv

dest_folder = "./data/"

symfile = open('nifty50_symbols.txt','r');
symdata = symfile.readlines()

#data = np.genfromtxt('./data/ACC.txt',dtype=None,delimiter=',',names=True)
#print data['Adj_Close'] 

result_file = open('result.csv','wb')
writer = csv.writer(result_file,dialect='excel')

for line in symdata:
    line = line.strip()
    #print line
    
    #make a text file name
    parts = line.split('.')    
    filename = dest_folder + parts[0] + '.txt'
    print filename
    
    #if the data is already downloaded, do not download it again
    if path.exists(filename): 
        data = np.genfromtxt(filename,dtype=None,delimiter=',',names=True)
        writer.writerow(data['Adj_Close'])

symfile.close()
result_file.close()