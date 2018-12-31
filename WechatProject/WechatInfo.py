
# user = itchat.search_friends(name='可爱的小鹿鹿')
# userName=(user[0]['UserName'])
# itchat.send('hello',toUserName=userName)

import WechatProject.database
WechatProject.database.databaseconnection()
import pandas as pd
import numpy as np
import WechatProject.rawdata
import WechatProject.translatort
from pyecharts import Page
import WechatProject.datavisualization

mydatamap=WechatProject.rawdata.rawdata.raw_data().loc[:,['NickName','RemarkName','City','Province','Sex','UserName']]            #restructure my data
mydata = mydatamap.replace(r'', np.NaN)                         #repalce with nah
mydata['Province']=WechatProject.translator.translate((mydata['Province']))           #translate Chinese-> English
print('sucessful translate')
print(mydata.head())
area=pd.DataFrame(mydata.groupby('Province')['UserName'].count().sort_values(ascending=[False])) # count how many people in your area
area=area.reset_index(level=0)
province=area['Province'].head()
Username=area['UserName'].head()
pie=WechatProject.datavisualization.piechart(province,Username)             #pie chart

sex=pd.DataFrame(mydata.groupby('Sex')['UserName'].count())
sex.reset_index()

liquid=WechatProject.datavisualization.liquid_chart('Mars Percentage of total friends', sex.loc[0,'UserName'] / sex.UserName.sum())
liquid2=WechatProject.datavisualization.liquid_chart('Male Percentage of total friends', sex.loc[1, 'UserName'] / sex.UserName.sum())
liquid3=WechatProject.datavisualization.liquid_chart('Female Percentage of total friends', sex.loc[2, 'UserName'] / sex.UserName.sum())
page= Page()

page.add(pie)
page.add(liquid)
page.add(liquid2)
page.add(liquid3)
page.render()