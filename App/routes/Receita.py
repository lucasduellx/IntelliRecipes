from flask import request, jsonify, render_template, redirect, session, flash, url_for
from App import app
from ..views import users,helper


# Rotas de INTERFACE

@app.route('/receitas', methods=['GET','POST'])
@helper.token_required
def getrecipes(current_user):
    type = request.form['cafe']
    if type == 'cafe':
        recipes = [
                {
                    "Id": "1",
                    "Nome" : "Overnight oats energético",
                    "Rendimento":  "20 porções",
                    "Tempo": "5 minutos",
                    "Image": "static/images/overnight.png"
                }
            ]
    elif type == 'almoco':
        recipes = [
            {
                "Id": "2",
                "Nome" : "Filé mignon ao forno prático",
                "Rendimento":  "10 porções",
                "Tempo": "50 minutos",
                "Image": "static/images/file.png"
            }
        ]
    elif type == 'janta':
        recipes = [
            {
                "Id": "3",
                "Nome" : "Coleslaw",
                "Rendimento":  "8 porções",
                "Tempo": "15 minutos",
                "Image": "static/images/coleslaw.png"
            }
        ]
    else:
        recipes = [
            {
                "Id": "4",
                "Nome" : "Sanduíche natural de atum simples",
                "Rendimento":  "4 porções",
                "Tempo": "15 minutos",
                "Image": "static/images/sanduiche.png"
            }
        ]
    
    return render_template('receitas.html',recipes=recipes,back=True)

@app.route('/receita', methods=['GET','POST'])
@helper.token_required
def getrecipe(current_user):
    type = request.form['cafe']
    recipe = {}
    if type == '1':
            recipe = {
                    "Nome" : "Overnight oats energético",
                    "Image": "static/images/overnight.png",
                    "Rendimento":  "20 porções",
                    "Tempo": "5 minutos",
                    "Ingrediente": [
                        '1 xícara de chá de aveia em flocos',
                        '1 colher de sopa de sementes de chia',
                        '1/2 banana bem madura amassada',
                        '1 colher de sopa rasa de cacau em pó',
                        '1 colher de sopa de açúcar',
                        '1 colher de chá de essência de baunilha',
                        '1/2 xícara de chá de café passado ou instantâneo fraco'
                    ],
                    "Modo" : [
                        '1) Reúna todos os ingredientes',
                        '2) Em um recipiente de vidro amasse bem a banana',
                        '3) Adicione o restante dos ingredientes e misture bem até a chia absorver bem o líquido',
                        '4) Coloque o overnight oats em um recipiente, tampe o recipiente e leve para geladeira de um dia para o outro',
                        '5) Quando for consumir, retire da geladeira, misture um pouco novamente e acrescente os toppings que desejar',
                        '6) Sirva'
                    ]
            }
    elif type == '2':
            recipe = {
                    "Nome" : "Filé mignon ao forno prático",
                    "Image": "static/images/file.png",
                    "Rendimento":  "10 porções",
                    "Tempo": "50 minutos",
                    "Ingrediente": [
                        '1 peça de filé mignon (sem gordura)',
                        '1 colher de sopa de mostarda em pó',
                        '2 colheres de sopa de alho triturado',
                        '1 colher de chá de sal'
                    ],
                    "Modo" : [
                        '1) Reúna todos os ingredientes',
                        '2) Tempere o filé com sal, mostarda, o alho e esfregue bem, para a carne pegar bem o tempero',
                        '3) Embrulhe a carne no papel alumínio, disponha em uma assadeira e leve ao forno preaquecido a 180 ºC por cerca de 30 minutos',
                        '4) Retire do forno, desembrulhe o filé e volte ao forno por mais 10 minutos',
                        '5) Sirva'
                    ]
            }
    elif type == '3':
            recipe = {
                    "Nome" : "Coleslaw",
                    "Image": "static/images/coleslaw.png",
                    "Rendimento":  "8 porções",
                    "Tempo": "15 minutos",
                    "Ingrediente": [
                        '250 gramas de repolho verde picado',
                        '250 gramas de repolho roxo picado',
                        '150 gramas de cenoura ralada',
                        '1/4 xícara de chá de maionese (60 gramas)',
                        '3 colheres de chá de mostarda dijon',
                        '2 colheres de chá de vinagre de maçã ou de sidra',
                        '1 colher de chá de molho de pimenta',
                        'Sal e pimenta-preta a gosto'
                    ],
                    "Modo" : [
                        '1) Reúna todos os ingredientes',
                        '2) Em uma tigela, misture os repolhos picados e a cenoura ralada',
                        '3) Em outro recipiente, coloque a maionese, a mostarda, o vinagre e o molho de pimenta',
                        '4) Bata a mistura com um fouet até ficar homogênea',
                        '5) Despeje essa maionese sobre a salada, misture até que todos os vegetais estejam cobertos pelo molho e tempere com sal e pimenta-preta a gosto',
                        '6) Cubra a tigela com um plástico filme e leve à geladeira por cerca de 1 hora',
                        '7) Sirva'
                    ]
            }
    elif type == '4':
            recipe = {
                    "Nome" : "Sanduíche natural de atum simples",
                    "Image": "static/images/sanduiche.png",
                    "Rendimento":  "4 porções",
                    "Tempo": "15 minutos",
                    "Ingrediente": [
                        '1 lata de atum escorrida (atum em água)',
                        '1 cenoura pequena ralada',
                        '2 colheres de sopa de salsinha picada',
                        '1 colher de café de tempero completo (ou sal e pimenta)',
                        '1 colher de sopa de mostarda',
                        '4 colheres de sopa de maionese light',
                        '8 fatias de pão integral de grão',
                        'Folhas de alface a gosto'
                    ],
                    "Modo" : [
                        '1) Reúna todos os ingredientes',
                        '2) Em um recipiente, coloque todos os ingredientes (menos o pão e a alface) e misture tudo (caso queira o recheio mais cremoso, é só colocar mais maionese)',
                        '3) Separe as fatias de pão, forre cada com folhas de alface e acrescente o recheio',
                        '4) Feche os sanduíches',
                        '5) Sirva'
                    ]
            }
    
    return render_template('receita.html',recipe=recipe,back=True)


# Rotas de API

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
