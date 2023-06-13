# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

# O Tema individual escolhido por mim foi o da série "Os Simpsons".

from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    username = credentials['username']
    password = credentials['password']
    
    authenticated = authenticate_user(username, password)
    
    if authenticated:
        return 'Login bem-sucedido!'
    else:
        return 'Falha na autenticação. Verifique suas credenciais.'

if __name__ == '__main__':
    app.run()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def authenticate_user(username, password):

    # Lista de usuários dos personagens da série "Os Simpsons"
    
    valid_users = [
        User('Homer Simpson', 'doh'),
        User('Marge Simpson', 'blue'),
        User('Bart Simpson', 'cowabunga'),
        User('Lisa Simpson', 'bigbrain'),
        User('Maggie Simpson', 'baby'),
        User('Ned flanders', 'christian'),
        User('Milhouse', 'ugly')

    ]
    
    for user in valid_users:
        if user.username == username and user.password == password:
            return True
    
    return False
