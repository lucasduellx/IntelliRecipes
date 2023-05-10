from flask import request, jsonify
from App import app

@app.route('/dieta', methods=['GET', 'POST'])
def dieta():
    if request.method == 'POST':
        new = request.json
        print(new)
    else:
        print('Nova dieta')
        return jsonify({
            "receitas": [
                {
                    "Nome" : "Brownie de Chocolate com Gengibre",
                    "Rendimento":  "20 porções"
                },
                {
                    "Nome" : "Brownie de Chocolate com Gengibre 2",
                    "Rendimento":  "20 porções"
                }
            ]
        })
