from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import numpy as np
import pandas as pd
url='https://saras.cbse.gov.in/SARAS/AffiliatedList/ListOfSchdirReportNew?ID1=D'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
table=soup.find('table',class_='table table-bordered dataTable no-footer')

data=[]
for row in table.find_all('tr')[1:]:
    cols=row.find_all('td')
    data.append({
            'Sno': cols[0].text.strip(),
            'Aff no.': cols[1].text.strip(),
            'State': cols[2].text.strip(),
            'Status': cols[3].text.strip(),
            'School and head name': cols[4].text.strip(),
            'Address': cols[5].text.strip(),
            'Details': cols[6].text.strip(),
    })
df=pd.DataFrame(data)
print(df)

filtered_df=df[df["School and head name"=="Rajesh kumar"]]
print('school whose principal name is Rajesh kumar')
print(filtered_df)
x=len(df)
print("number of schools: ",x)

client=MongoClient("mongodb://localhost:27107/")
db=client['my_db']
collection=db['my_collection']

collection.insert_many(data)

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient

how_many_senior = collection.find({'Status': 'Senior Secondary Level'} or {'Status':'Secondary Level'})

print("number of schools found:",len(how_many_senior))

find_principal=collection.find({'School and head name'=='Amity International School'})
print(find_principal)
