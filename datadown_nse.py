import urllib2
from StringIO import StringIO
import gzip

req = urllib2.Request('http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=M%26M&fromDate=01-Jan-2013&toDate=25-May-2014&datePeriod=unselected&hiddDwnld=true')
#req = urllib2.Request('http://www.nseindia.com//content/indices/histdata/CNX%20NIFTY01-01-2013-25-05-2014.csv HTTP/1.1')
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

stockfile = open('nifty.csv','wb')
stockfile.write(uncompress_data.read())
stockfile.close()
