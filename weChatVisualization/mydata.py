
import pandas as pd
import numpy as np
import weChatVisualization.rawdata
mydatamap= weChatVisualization.rawdata.raw_data().loc[:, ['NickName', 'RemarkName', 'City', 'Province', 'Sex', 'UserName']]
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
mydata = mydatamap.replace(r'', np.NaN)
