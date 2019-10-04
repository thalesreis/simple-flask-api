from flask import Flask, make_response
from flask import jsonify
import json
import values
from motor_recomendacao import *

from dados import *

app = Flask(__name__)

# Por padrão, o flask aceita apenas o verbo GET

@app.route('/usuarios')
def get_users():
    results = values.get_all_users()

    return make_response(jsonify(results), 200)


# @app.route('/usuarios/<id>')
# def get_users_id(id):
#     mycursor = con_mysql_db.mydb.cursor()
#     comando = "select * from usuarios where id = %s"
#     values = (id, )
#     mycursor.execute(comando, values)
#     users = mycursor.fetchall()

#     if len(users) == 0:
#         return make_response(jsonify({'message':'user not found', 'id':id}), 404)

#     results = []
#     for user in users:
#         x = {
#             "id" : user[0],
#             "nome" : user[1],
#             "Cidade" : user[2]
#         }
#         results.append(x)

#     return jsonify(results)

# @app.route('/testes')
# def teste():
#     valor = notas_vinho_usuarios()
#     return jsonify(valor)

if __name__ == '__main__':
    # print(notas_usuario_vinhos())
    # print(notas_vinho_usuarios())
    # notas_users = notas_usuario_vinhos()
    # print(calculaItensSimilares(notas_users))
    app.run(host='127.0.0.1', port='5000', debug=True)