import pandas as pd
import requests as res 
from bs4 import BeautifulSoup as bs 
import matplotlib.pyplot as plt 
import re 
%matplotlib inline
data=[] 
st1 = input("Enter first company code : ")
st2 = input("Enter senond company code : ")
#ix = input("Enter the value about plotting data")
req=res.get("https://www.nasdaq.com/symbol/"+st1+"/historical",headers={"User-Agent":"chrome/127.0.0.1"})

h=bs(req.content,"lxml")

table_body=h.find("tbody") 
rows = table_body.find_all('tr')

i=0 
i1=0

for tr in rows:
    df={}
    i=0 
    i1+=1 
    cols = tr.find_all('td')
    if(i1>5):
        for td in cols:
            if(i==0):
                df["date"]=td.text[38:48]
            if(i==1):
                df["open"]=(str(re.findall("\d+\.\d+",td.text)).strip("['']"))
            if(i==2):
                df["high"]=(str(re.findall("\d+\.\d+",td.text)).strip("['']"))
            if(i==3):
                df["low"]=(str(re.findall("\d+\.\d+",td.text)).strip("['']"))
            if(i==4):
                df["close"]=(str(re.findall("[0-9]+.[0-9]+",td.text)).strip("['']"))
            if(i==5):
                df["volume"]=(str(re.findall("[0-9,]+",td.text)).strip("['']"))
            i+=1
            data.append(df)
df1=pd.DataFrame(data)
df1 
df1.to_csv("data_"+st1+".csv",index=False)

data=[]


req=res.get("https://www.nasdaq.com/symbol/"+st2+"/historical",headers={"User-Agent":"chrome/127.0.0.1"})

h=bs(req.content,"lxml")

table_body=h.find("tbody")
rows = table_body.find_all('tr')

i=0
i1=0

for tr in rows:
    df={}
    i=0 
    i1+=1 
    cols = tr.find_all('td')

    if(i1>5):
        for td in cols:
            if(i==0):
                df["date"]=td.text[38:48]
            if(i==1):
                df["open"]=(str(re.findall("\d+\.\d+",td.text)).strip("['']"))
            if(i==2):
                df["high"]=(str(re.findall("\d+\.\d+",td.text)).strip("['']"))
            if(i==3):
                df["low"]=(str(re.findall("\d+\.\d+",td.text)).strip("['']"))
            if(i==4):
                df["close"]=(str(re.findall("[0-9]+.[0-9]+",td.text)).strip("['']"))
            if(i==5):
                df["volume"]=(str(re.findall("[0-9,]+",td.text)).strip("['']"))
            i+=1
            data.append(df)
df1=pd.DataFrame(data) 
df1 
df1.to_csv("data_"+st2+".csv",index=False)

csv_file1=pd.read_csv("data_"+st1+".csv",parse_dates=["date"],index_col="date")
#,converters={"close":float})
csv_file2=pd.read_csv("data_"+st2+".csv",parse_dates=["date"],index_col="date")
#,converters={"close":float})

csv_file1["2018"].close.plot()
csv_file1,csv_file2

print("CLOSE PRICES GRAPH:")
plt.plot(csv_file1["close"])
plt.plot(csv_file2["close"]) 
plt.legend([st1,st2]) 
plt.ylabel("value")
plt.xlabel("dates")
plt.show()

print("OPEN PRICES GRAPH:")
plt.plot(csv_file1["open"])
plt.plot(csv_file2["open"]) 
plt.legend([st1,st2]) 
plt.ylabel("value")
plt.xlabel("dates")
plt.show()

print("HIGH PRICES GRAPH:")
plt.plot(csv_file1["high"])
plt.plot(csv_file2["high"]) 
plt.legend([st1,st2]) 
plt.ylabel("value")
plt.xlabel("dates")
plt.show()

print("LOW PRICES GRAPH:-")
plt.plot(csv_file1["low"])
plt.plot(csv_file2["low"]) 
plt.legend([st1,st2]) 
plt.ylabel("value")
plt.xlabel("dates")
plt.show()
print(csv_file1)
print(csv_file2)


#csv_file2["2018"].high.plot()#,csv_file2["2018"].close.plot()