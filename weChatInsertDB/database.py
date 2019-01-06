import MySQLdb
#db connection
try:
    db=MySQLdb.connect(host='127.0.0.1',user='root',password='root',db='wechatDB',use_unicode=True)
    db.set_character_set(charset='utf8mb4')
    db.ping(True)
    print('db conneciton sucessful')
except:
    print('db error')


