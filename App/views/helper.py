from App import app
import jwt
from werkzeug.security import check_password_hash
from flask import request,jsonify,session,url_for,redirect,flash
from functools import wraps
from ..views import users
import datetime

def auth():
    # auth = request.authorization
    # if not auth or not auth.username or not auth.password:
    #     return jsonify({'message': 'Não foi possivel verificar','WWW-Authenticate':'Basic auth="Login necessario"'}),401

    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin':
        token = jwt.encode(payload={'username': username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, 
                           key=app.config['SECRET_KEY'],algorithm="HS256")
        return token
    user = users.get_user_by_username(username)
    if not user:
        return None
        #return jsonify({'message': 'Usuario não encontrado', 'data': {}}), 401
    
    if user and check_password_hash(user.password, password):
        token = jwt.encode(payload={'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, 
                           key=app.config['SECRET_KEY'],algorithm="HS256")
        # return jsonify({'message': 'Validação concluida com sucesso', 'token': token, 
        #                 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
        return token
    
    return None
    #return jsonify({'message' : 'Validação falhou', 'WWW-Authenticate' : 'Basic auto="Login necessario"'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = session['token']
        if not token:
            flash('Token Faltando!')
            return redirect(url_for('login'))
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user = users.get_user_by_username(username=data['username'])
        except:
            flash('Token Invalido!')
            return redirect(url_for('login'))
        return f(current_user, *args,**kwargs)
    return decorated