#
# allows to download only nifty index data from nse
#
import urllib2
from StringIO import StringIO
import gzip
import numpy as np

nifty_filename_temp = './data_nse/NIFTY_temp.csv'
nifty_filename_temp2 = './data_nse/NIFTY_temp2.csv'
nifty_filename_perm = './data_nse/NIFTY.csv'

def datadown_nse():
    #req = urllib2.Request('http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=M%26M&fromDate=01-Jan-2013&toDate=25-May-2014&datePeriod=unselected&hiddDwnld=true')
    req = urllib2.Request('http://www.nseindia.com//content/indices/histdata/CNX%20NIFTY01-01-2014-19-06-2014.csv')
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0')
    req.add_header('Accept','*/*')
    req.add_header('Accept-Language','en-US,en;q=0.5')
    req.add_header('Accept-Encoding','gzip, deflate')
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('Connection','keep-alive')

    #get the response
    response = urllib2.urlopen(req)

    #the following data has double quotes for all individual data
    #this file must be opened in xml and saved as NIFTY_temp2.csv
    fw = open(nifty_filename_temp,'w')
    fw.write(response.read())
    fw.close()

##    #convert into string IO buffer
##    buff = StringIO(response.read())
##    #uncompress the data using gzip
##    uncompress_data = gzip.GzipFile(fileobj = buff)
##
##    stockfile = open(nifty_filename_temp,'wb')
##    stockfile.write(uncompress_data.read())
##    stockfile.close()

def refine_nse_data():
    nifty_input = nifty_filename_temp2
    nifty_output = nifty_filename_perm
    store_fmt = '%s,%f,%f,%f,%f,%u,%f'
    header_string = "Date, Open Price, High Price, Low Price, Close Price, Total Traded Quantity, Turnover (in Cr)\n"
    #read data from text
    actual_data = np.genfromtxt(nifty_input,dtype=None,delimiter=',',names=True)
    #reverse data
    reverse_data = actual_data[::-1]

    #print reverse_data
    print 'writing data'
    np.savetxt(nifty_output,reverse_data,fmt=store_fmt,delimiter=',')

    #reopen the file again
    file = open(nifty_output,'r')
    content = file.read()
    file.close()

    #overwrite the content
    file = open(nifty_output,'w')
    file.write(header_string)
    file.write(content)
    file.close()
    

if __name__ == '__main__':
    datadown_nse()
#    refine_nse_data()
