from flask import request, jsonify, render_template, redirect, session, flash, url_for
from app import app
from ..views import users,helper

# ROTAS API

@app.route('/user', methods=['POST','PUT'])
def user():
    if request.method == 'POST':
        if users.post_user() == 'OK':
            flash('Cadastro realizado com sucesso')
            return redirect(url_for('login'))
        else:
            flash('Erro ao realizar cadastro')
            return redirect(url_for('register'))
    elif request.method == 'PUT':
        msg = users.update_user()
        if msg == 'OK':
            flash('Senha alterada com sucesso','message')
            return redirect(url_for('login'))
        else:
            flash(msg)
            return render_template('recover.html',user=None)
        

@app.route('/auth', methods=['POST'])
def auth():
    res = helper.auth()
    
    if res is None:
        flash('Acesso negado, digite novamente!','error')
        return redirect(url_for('login'))
    else:
        session['token'] = res
        return redirect(url_for('home'))


@app.route('/autenticado',methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify({'message': f'Ola Mundo, Ola {current_user.name}'})


@app.route('/recoveruser',methods=['POST'])
def recoveruser():
    username = request.form['username']
    getuser = users.get_user_by_username(username)
    return render_template('recover.html',user=getuser)

@app.route('/alteruser', methods=['POST'])
def alteruser():
    if request.method == 'POST':
        msg = users.update_user()
        if msg == 'OK':
            flash('Senha alterada com sucesso','message')
            return redirect(url_for('login'))
        else:
            flash(msg)
            return render_template('recover.html',user=None)
        

# ROTAS DAS PAGINAS

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/home',methods=['GET'])
@helper.token_required
def home(current_user):
    return render_template('home.html')

@app.route('/logout',methods=['GET'])
@helper.token_required
def logout(current_user):
    session['token'] = None
    flash('Volte sempre,'+current_user.name,'message')
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')


@app.route('/recover',methods=['GET','POST'])
def recover():
    return render_template('recover.html',user=None)