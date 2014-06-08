import urllib2
from StringIO import StringIO
import os
import gzip

#configuratin
symbol_filename = 'nse_nifty50_symbols.txt'
dest_folder = "./data_nse/"
start_date = '01-Jan-2013'
end_date = '25-May-2014'

url1 = 'http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='
url2 = '&fromDate='+ start_date +'&toDate=' + end_date + '&datePeriod=unselected&hiddDwnld=true'

#read symbols
symfile = open(symbol_filename,'r');
symdata = symfile.readlines()

#for each symbol download the historical data in the range of above date
for line in symdata:
    line = line.strip()
    if line != 'NIFTY':
        
        #print line
            
        #make a text file name
        if line == 'M&M':
            fullurl = url1 + 'M%26M' + url2
        else:
            fullurl = url1 + line + url2
        
        filename = dest_folder + line + '.csv'
        print filename
        
        #if the data is already downloaded, do not download it again
        if not os.path.exists(filename): 
            req = urllib2.Request(fullurl)
            req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0')
            req.add_header('Accept','*/*')
            req.add_header('Accept-Language','en-US,en;q=0.5')
            req.add_header('Accept-Encoding','gzip, deflate')
            req.add_header('X-Requested-With','XMLHttpRequest')
            req.add_header('Connection','keep-alive')

            #get the response
            response = urllib2.urlopen(req)

            #convert into string IO buffer
            buff = StringIO(response.read())
            #uncompress the data using gzip
            uncompress_data = gzip.GzipFile(fileobj = buff)

            stockfile = open(filename,'wb')
            stockfile.write(uncompress_data.read())
            stockfile.close()
symfile.close()





