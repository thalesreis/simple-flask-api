import con_mysql_db

def get_all_users():
    dbCon = con_mysql_db.con_db()
    mycursor = dbCon.cursor()
    mycursor.execute("select * from users")
    users = mycursor.fetchall()

    results = [{
        'id': user[0],
        'nome': user[1]
    } for user in users]    

    return users    
