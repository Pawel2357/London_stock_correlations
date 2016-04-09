# Copyright (c) 2011, Mark Chenoweth
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted 
# provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following 
#   disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import urllib,time,datetime

class Quote(object):
  
  DATE_FMT = '%Y-%m-%d'
  TIME_FMT = '%H:%M:%S'
  
  def __init__(self):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))

  def append(self,dt,open_,high,low,close,volume):
    self.date.append(dt.date())
    self.time.append(dt.time())
    self.open_.append(float(open_))
    self.high.append(float(high))
    self.low.append(float(low))
    self.close.append(float(close))
    self.volume.append(int(volume))
      
  def to_csv(self):
    return ''.join(["{0},{1},{2},{3:.2f},{4:.2f},{5:.2f},{6:.2f},{7}\n".format(self.symbol,
              self.date[bar].strftime('%Y-%m-%d'),self.time[bar].strftime('%H:%M:%S'),
              self.open_[bar],self.high[bar],self.low[bar],self.close[bar],self.volume[bar]) 
              for bar in xrange(len(self.close))])
    
  def write_csv(self,filename):
    with open(filename,'w') as f:
      f.write(self.to_csv())
        
  def read_csv(self,filename):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
    for line in open(filename,'r'):
      symbol,ds,ts,open_,high,low,close,volume = line.rstrip().split(',')
      self.symbol = symbol
      dt = datetime.datetime.strptime(ds+' '+ts,self.DATE_FMT+' '+self.TIME_FMT)
      self.append(dt,open_,high,low,close,volume)
    return True

  def __repr__(self):
    return self.to_csv()

   
class GoogleQuote(Quote):
  ''' Daily quotes from Google. Date format='yyyy-mm-dd' '''
  def __init__(self,symbol,start_date,end_date=datetime.date.today().isoformat()):
    super(GoogleQuote,self).__init__()
    self.symbol = symbol.upper()
    start = datetime.date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]))
    end = datetime.date(int(end_date[0:4]),int(end_date[5:7]),int(end_date[8:10]))
    url_string = "http://www.google.com/finance/historical?q={0}".format(self.symbol)
    url_string += "&startdate={0}&enddate={1}&output=csv".format(
                      start.strftime('%b %d, %Y'),end.strftime('%b %d, %Y'))
    csv = urllib.urlopen(url_string).readlines()
    csv.reverse()
    for bar in xrange(0,len(csv)-1):
      ds,open_,high,low,close,volume = csv[bar].rstrip().split(',')
      open_,high,low,close = [float(x) for x in [open_,high,low,close]]
      dt = datetime.datetime.strptime(ds,'%d-%b-%y')
      self.append(dt,open_,high,low,close,volume)
 
 
#import pandas.io.data as web
#import datetime
#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2013, 1, 27)
#df=web.DataReader("BVMF:ABRE11", 'google', start, end)
#print df.head(10)
 
#OK ale nie zawsze
#gticker='INDEXFTSE:MCX'
#import pandas.io.data as web
#dfg = web.DataReader(gticker, 'google', '2013/1/1', '2014/3/1') 
#print dfg.head(10)

#TU znajde dane do metody importujacej dane
#http://pandas.pydata.org/pandas-docs/stable/remote_data.html
import pandas.io.data as web
from pandas import *
import numpy as np
import pylab as py

import datetime

start = datetime.datetime(1985, 1, 1)

end = datetime.datetime(2015, 4, 29)

'''
with open('/home/pawel/Documents/magisterka/Financial_historical_data/constituents_FTSE100') as f:
    lines = f.readlines()
'''

fig = py.figure()
#print lines[0].strip()
#f=web.DataReader(lines[0].strip(), 'yahoo', start, end)
x=[]
y=[]
i=0
'''
for line in lines:
    if len(line.strip())>1:
        try:
            f=web.DataReader(line.strip(), 'yahoo', start, end)
        except:
            raise
        else:
            y.append(f.index.date[0])            
            print f.index.date[0]

          
file = open("/home/pawel/Documents/magisterka/Financial_historical_data/data_FTSE100.txt", "w")
for i in y:
    file.write(i)
file.close()



py.xlabel('Data')
py.ylabel('liczba spolek')
py.title('FTSE100')

for i in y:
    j=0
    for k in y:
        if k<=i:
            j+=1
    x.append(j)

py.plot(y,x, 'ro')
py.show()
fig.savefig('/home/pawel/Documents/magisterka/Financial_historical_data/constituents100.jpg')
py.clf()


'''


with open('/home/pawel/Documents/magisterka/Financial_historical_data/constituents_FTSE250') as f:
    lines = f.readlines()

#print lines[0].strip()
#f=web.DataReader(lines[0].strip(), 'yahoo', start, end)
x=[]
y=[]
i=0

for line in lines:
    if len(line.strip())>1:
        try:
            f=web.DataReader(line.strip(), 'yahoo', start, end)
        except:
            raise
        else:
            y.append(f.index.date[0])            
            print f.index.date[0]
'''        
file = open("/home/pawel/Documents/magisterka/Financial_historical_data/data_FTSE250.txt", "w")
for i in y:
    file.write(i)
file.close()
'''


py.xlabel('Data wejscia')
py.ylabel('liczba spolek')
py.title('FTSE250')


for i in y:
    j=0
    for k in y:
        if k<=i:
            j+=1
    x.append(j)


py.plot(y,x, 'ro')
py.show()
fig.savefig('/home/pawel/Documents/magisterka/Financial_historical_data/constituents250.jpg')
py.clf()


#data z http://stackoverflow.com/questions/29224258/modify-pandas-dataframe-to-list-year-month-and-date

#print f.index.date[0]

#f.to_csv('/home/pawel/Documents/magisterka/Financial_historical_data/data.txt', index=False)
#print 'Done'

#print to_datetime(f)


#s = f[1:2][0:2]
#DataFrame.values(f)
#print type(f)
#print f.values
#print f.dtypes
#print s

#data = np.zeros((2,),dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
#print DataFrame(data)

#print g

#print f.ix['2013-01-04']
#print f[0]
 

#if __name__ == '__main__':
#  q = GoogleQuote('aapl','2011-01-01')              # download year to date Apple data
#  print q                                           # print it out
#  q = GoogleQuote('orcl','2011-11-01','2011-11-30') # download Oracle data for February 2011
#  q.write_csv('orcl.csv')                           # save it to disk
#  q = Quote()                                       # create a generic quote object
#  q.read_csv('orcl.csv')                            # populate it with our previously saved data
#  print q            
