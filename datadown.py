import urllib2
import os.path as path

dest_folder = "./data/"
url1 = 'http://ichart.finance.yahoo.com/table.csv?a=01&b=01&c=2013&d=24&e=05&f=2014&s='

symfile = open('nifty50_symbols.txt','r');

symdata = symfile.readlines()

for line in symdata:
    line = line.strip()
    fullurl = url1 + line
    #print line
    
    #make a text file name
    parts = line.split('.')    
    filename = dest_folder + parts[0] + '.txt'
    print filename
    
    #if the data is already downloaded, do not download it again
    if not path.exists(filename): 
        response = urllib2.urlopen(fullurl)
        savefile = open(filename,'wb')
        savefile.write(response.read())
        savefile.close()

symfile.close()