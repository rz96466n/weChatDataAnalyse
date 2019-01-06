import weChatInsertDB.dbFunction
import weChatVisualization.dataconnection
weChatVisualization.dataconnection.databaseconnection()
import weChatVisualization.rawdata
import  numpy as np
import weChatVisualization.translator
import chardet
import pandas as pd
mydata= weChatVisualization.rawdata.raw_data().loc[:, ['NickName', 'RemarkName', 'City', 'Province', 'Sex', 'UserName']]            #restructure my data

print('start translate')
mydata.replace('', "None", inplace=True)
mydata['Province']=weChatVisualization.translator.translate((mydata['Province']))           #translate Chinese-> English
print(mydata.head())
# isinstance(mydata['NickName'], str)                       #test string code

weChatInsertDB.dbFunction.insert(mydata.index, mydata['NickName'], mydata['NickName'], mydata['City'], mydata['Province'], mydata['Sex'], mydata['UserName'])