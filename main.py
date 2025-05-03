from flask import Flask, jsonify, request

app = Flask(__name__)

#Lista para mensagens
mensagens = [
    {
        'id': 1,
        'Nome': 'Rosangela',
        'Mensagem': 'Opa, tudo bem?'
    },
    {
        'id': 2,
        'Nome': 'Maria',
        'Mensagem': 'Ola, tudo bem?'
    },
    {
        'id': 3,
        'Nome': 'Sophia',
        'Mensagem': 'Oii, tudo bem?'
    },
]

#Endpoint para READ - ALL
@app.route('/mensagens', methods=['GET'])
def read_all():
    return jsonify(mensagens)

#Endpoint para READ - ONE
@app.route('/mensagens/<int:id>', methods=['GET'])
def read_one(id):
    for mensagem in mensagens:
        if mensagem.get('id') == id:
            return jsonify(mensagem)

#Endpoint para UPDATE
@app.route('/mensagens/<int:id>', methods=['PUT'])
def update_mensagem(id):
    mensagem_atualizada = request.get_json()
    for indice, mensagem in enumerate(mensagens):
        if mensagem.get('id') == id:
            mensagens[indice].update(mensagem_atualizada)
            return jsonify(mensagens[indice])

#Endpoint para CREATE
@app.route('/mensagens', methods=['POST'])
def create_mensagem():
    nova_mensagem = request.get_json()
    mensagens.append(nova_mensagem)

    return jsonify(mensagens)

#Endpoint para DELETE
@app.route('/mensagens/<int:id>', methods=['DELETE'])
def delete_mensagem(id):
    for indice, mensagem in enumerate(mensagens):
        if mensagem.get('id') == id:
            del mensagens[indice]
            return jsonify(mensagens)

app.run(debug=True)

