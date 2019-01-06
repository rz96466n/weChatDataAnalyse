import json

import requests

# 翻译函数，word 需要翻译的内容
def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    list = []
    for i in word:

            key = {
                'type': "ZH_CN2EN",
                'i': i,
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "ue": "UTF-8",
                "action": "FY_BY_CLICKBUTTON",
                "typoResult": "true"
            }
            # key 这个字典为发送给有道词典服务器的内容
            response = requests.post(url, data=key)
            # 判断服务器是否相应成功
            if response.status_code == 200:
                # 然后相应的结果
                # print(response.text)
                result=json.loads(response.text)
                # print(response.text)
                result = result['translateResult'][0][0]['tgt'].capitalize()
                list.append(result)

            else:
                print("有道词典调用失败")
            # 相应失败就返回空
                break
    # print(list)
    return list



if __name__=='__main__':
    a=['中国','河北','China']
    translate(a)