import urllib2
import os.path as path
import numpy as np
import csv

symbol_filename = 'nse_nifty50_symbols.txt'
dest_folder = "./data_nse/"

symfile = open(symbol_filename,'r');
symdata = symfile.readlines()

#data = np.genfromtxt('./data/ACC.txt',dtype=None,delimiter=',',names=True)
#print data['Adj_Close'] 

result_file = open('result.csv','wb')
writer = csv.writer(result_file,dialect='excel')

for line in symdata:
    line = line.strip()
    #print line
    
    #make a text file name
    filename = dest_folder + line + '.csv'
    print filename
    
    #if the data is already downloaded, do not download it again
    if path.exists(filename): 
        data = np.genfromtxt(filename,dtype=None,delimiter=',',names=True)
        writer.writerow(data['Close_Price'])

symfile.close()
result_file.close()