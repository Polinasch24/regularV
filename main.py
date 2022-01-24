import re
from pprint import pprint

import csv
import pandas
import pandas as pd

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


Total_list=[]
for element in contacts_list:
    i=re.split(r'\W+', str(element[0:3]))
    i_1=i.pop(0)
    i_2=i.pop()
    if len(i)<3:
       i.append('')
    element[0]=i[0]
    element[1]=i[1]
    element[2]=i[2]


    phone_pattern = re.compile(
        r"([\+7|8)]+)\s*\(?(\d{3})\)?[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]"
        r"*(\d{2})\s*(\(?(\w+\.)\s*(\d+)\)?)*"
    )
    result = phone_pattern.sub(r"+7(\2)\3-\4-\5 \7 \8", element[5]).strip()
    element[5]=result


    Total_list.append(element)

Dict={}

lastname=[]
firstname=[]
surname=[]
organization=[]
position=[]
phone=[]
email=[]
Dict.setdefault(Total_list[0][0],lastname)
Dict.setdefault(Total_list[0][1],firstname)
Dict.setdefault(Total_list[0][2],surname)
Dict.setdefault(Total_list[0][3],organization)
Dict.setdefault(Total_list[0][4],position)
Dict.setdefault(Total_list[0][5],phone)
Dict.setdefault(Total_list[0][6],email)
for i in Total_list[1:]:

    lastname.append(i[0])
    firstname.append(i[1])
    surname.append(i[2])
    organization.append(i[3])
    position.append(i[4])
    phone.append(i[5])
    email.append(i[6])
df=pd.DataFrame(Dict)


grouped = df.groupby(['lastname','firstname' ])
x=grouped.groups
pprint(x)



with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(Total_list)