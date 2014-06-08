#converts NIFTY ascending date data to descending order

import numpy as np

nifty_input = './data_nse/NIFTY3.csv'
nifty_output = './data_nse/NIFTY.csv'
store_fmt = '%s,%f,%f,%f,%f,%u,%f'
header_string = "Date, Open Price, High Price, Low Price, Close Price, Total Traded Quantity, Turnover (in Cr)\n"

actual_data = np.genfromtxt(nifty_input,dtype=None,delimiter=',',names=True)
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
