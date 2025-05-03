from flask import Flask, jsonify

app = Flask(__name__)

#Lista para mensagens
mensagens = [
    {
        'id':1,
        'Nome': 'Ziraldo',
        'Mensagem': 'Opa, tudo bem?'
    },
    {
        'id':2,
        'Nome': 'Antônio',
        'Mensagem': 'Olá, tudo bem?'
    },
    {
        'id':3,
        'Nome': 'Fernando',
        'Mensagem': 'Oii, tudo bem?'
    },
]

#Endpoint para READ - ALL
@app.route('/mensagens', methods=['GET'])
def read_all():
    return jsonify(mensagens)

app.run(debug=True)

    




