from flask import request, jsonify
from App import app

@app.route('/ingrediente', methods=['GET', 'POST'])
def ingrediente():
    if request.method == 'POST':
        new = request.json
        print(new)
    else:
        return jsonify({
            "Ingredientes": [
                {
                    "Nome" : "Tomate"
                },
                {
                    "Nome" : "Batata"
                }
            ]
        })
