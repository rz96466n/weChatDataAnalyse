
# user = itchat.search_friends(name='可爱的小鹿鹿')
# userName=(user[0]['UserName'])
# itchat.send('hello',toUserName=userName)

import weChatVisualization.dataconnection
weChatVisualization.dataconnection.databaseconnection()
import pandas as pd
import numpy as np
import weChatVisualization.rawdata
import weChatVisualization.translator
from pyecharts import Page
import weChatVisualization.datavisualization

mydatamap= weChatVisualization.rawdata.raw_data().loc[:, ['NickName', 'RemarkName', 'City', 'Province', 'Sex', 'UserName']]            #restructure my data
mydata = mydatamap.replace(r'', np.NaN)                         #repalce with nah
print('start translate')
mydata['Province']=weChatVisualization.translator.translate((mydata['Province']))           #translate Chinese-> English
print(mydata.head())
area=pd.DataFrame(mydata.groupby('Province')['UserName'].count().sort_values(ascending=[False])) # count how many people in your area
area=area.reset_index(level=0)
province=area['Province'].head()
Username=area['UserName'].head()
pie=weChatVisualization.datavisualization.piechart(province, Username)             #pie chart

sex=pd.DataFrame(mydata.groupby('Sex')['UserName'].count())
sex.reset_index()

liquid=weChatVisualization.datavisualization.liquid_chart('Male Friends are: ', sex.loc[1, 'UserName'] / sex.UserName.sum())
liquid2=weChatVisualization.datavisualization.liquid_chart('Female Friends are:', sex.loc[2, 'UserName'] / sex.UserName.sum())
liquid3=weChatVisualization.datavisualization.liquid_chart('People with no identity(Mars): ', sex.loc[0, 'UserName'] / sex.UserName.sum())
bar=weChatVisualization.datavisualization.bar_chart(area.loc[1:8,['Province']].values.tolist(),area.loc[1:8,['UserName']].values.tolist())

page= Page()

page.add(pie)
page.add(liquid)
page.add(liquid2)
page.add(liquid3)
page.add(bar)
page.render(path='yourFinalContractInfo.html')