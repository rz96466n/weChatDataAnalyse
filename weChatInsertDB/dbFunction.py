
def insert(id, nickname, remarkname,city,province, sex, username):
    import weChatInsertDB.database

    cursor=weChatInsertDB.database.db.cursor()
    param=[]
    for i in range(0,len(id)):
        idDB =id[i]
        nicknameDB = nickname[i]
        remarknameDB = remarkname[i]
        cityDB = city[i]
        provinceDB = province[i]
        sexDB = sex[i]
        usernameDB = username[i]
        param.append([idDB,nicknameDB, remarknameDB, cityDB, provinceDB, sexDB, usernameDB])
    sql = "insert into wechatinfo(ID, nickName, remarkName, city,province, sex,userName) values (%s, %s, %s,%s,%s,%s, %s)"
    try:
        cursor.execute("SET NAMES 'utf8mb4'")
        cursor.execute("SET CHARACTER SET 'utf8mb4';")
        cursor.execute("SET character_set_connection='utf8mb4';")
        cursor.execute("SET character_set_client='utf8mb4';")
        cursor.execute("SET character_set_results='utf8mb4';")
        cursor.execute("ALTER DATABASE wechatDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        cursor.execute('ALTER TABLE wechatinfo CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ')
        cursor.executemany(sql, param)
        weChatInsertDB.database.db.commit()
        cursor.close()
        print('insert sucessful')
    except Exception as e:
        print(e)
        weChatInsertDB.database.db.rollback()

if __name__=='__main__':
    id=['1','2','3','4','5']
    nickname=['tim','tim1','tim','tim','tim0']
    remarkname=['ryan','ryan','ryan','ryan','ryan']
    city=['ny','ny','ny','ny','ny']
    province=['ny','ny','ny','ny','ny']
    sex=['female','female','female','female','female']
    username=['111','111','111','111','111']
    print(nickname[0:len(id)])
    insert(id,nickname,remarkname,city,province,sex,username)