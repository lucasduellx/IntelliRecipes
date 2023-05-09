from flask import request, jsonify
from App import app

@app.route('/', methods=['GET'])
def recipes():
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

@app.route('/receita', methods=['GET'])
def recipe():
    name = request.args.get('name')
    print(name)
    if(name == 'Brownie'):
        return jsonify({
        "receita": [
            {
                "Nome" : "Brownie de Chocolate com Gengibre",
                "Rendimento":  "20 porções"
            },
            {
            "Ingredientes": [
                    "50 g farinha de milho fina",
                    "10 g de cacau em pó",
                    "250 g de chocolate meio amargo",
                    "200 g de manteiga sem sal cortada em cubos",
                    "20 ml de suco de gengibre",
                    "5 ovos",
                    "200 g de açúcar",
                    "1 colher (chá) de fermento em pó",
                    "100 g de nozes picadas grosseiramente",
                    " "
                ]
            },
            {
            "Modo de Preparo": [
                "1 - Coloque numa tigela a farinha de milho fina e o cacau em pó.",
                "2 - Misture e reserve.",
                "3 - Numa panela, em banho-maria, derreta o chocolate meio amargo picado com a manteiga sem sal cortada em cubos.",
                "4 - Retire do fogo.",
                "5 - Adicione o suco de gengibre e misture.",
                "6 - Acrescente a mistura de farinha com cacau em pó (reservada acima). Misture bem e reserve.",
                "7 - Numa batedeira, coloque os ovos e o açúcar. Bata bem até dobrar de volume.",
                "8 - Com a batedeira ainda ligada, adicione o fermento em pó e bata até misturar.",
                "9 - Desligue a batedeira. Acrescente a mistura de chocolate (reservada acima) e as nozes picadas. Misture.",
                "10 - Transfira a massa para uma assadeira retangular (18 cm X 30 cm) untada e forrada com papel manteiga.",
                "11 - Leve para assar em forno médio pré-aquecido a 180°C por +/- 40 minutos.",
                "12 - Retire do forno.",
                "13 - Cubra o brownie com papel manteiga.",
                "14 - Coloque outra assadeira do mesmo tamanho pressionando levemente o brownie para que fique mais compacto e úmido",
                "15 - Deixe por +/- 4 horas na geladeira.",
                "16 - Retire a assadeira de cima do brownie, desenforme, corte em quadrados e sirva em seguida.",
                " "
            ]
            }
        ]
        })
    else:
        return jsonify({"erro" : "Receita não encontrada"})

@app.route('/tipo',methods=['GET'])
def type():
    name = request.args.get('name')
    print(name)
    if(name == 'Sobremesa'):
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
    else:
        return jsonify({"erro" : "Receita não encontrada"})
