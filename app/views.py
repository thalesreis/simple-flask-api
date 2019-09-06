from flask import Flask, make_response
from flask import jsonify
import json
import con_mysql_db
app = Flask(__name__)

# Por padrão, o flask aceita apenas o verbo GET

@app.route('/usuarios')
def get_users():
    mycursor = con_mysql_db.mydb.cursor()
    mycursor.execute("select * from usuarios")
    users = mycursor.fetchall()

    results = [{
        'id': user[0],
        'nome': user[1],
        'cidade': user[2]
    } for user in users]

    return make_response(jsonify(results), 200)


@app.route('/usuarios/<id>')
def get_users_id(id):
    mycursor = con_mysql_db.mydb.cursor()
    comando = "select * from usuarios where id = %s"
    values = (id, )
    mycursor.execute(comando, values)
    users = mycursor.fetchall()

    if len(users) == 0:
        return make_response(jsonify({'message':'user not found', 'id':id}), 404)

    results = []
    for user in users:
        x = {
            "id" : user[0],
            "nome" : user[1],
            "Cidade" : user[2]
        }
        results.append(x)

    return jsonify(results)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)