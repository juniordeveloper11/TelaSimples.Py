from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Página inicial com formulário de cadastro
@app.route('/')
def index():
    return render_template('cadastro.html')

# Rota para lidar com o envio do formulário
@app.route('/cadastro', methods=['POST'])
def cadastro():
    # Aqui você pode lidar com os dados do formulário enviado
    nome = request.form['nome']
    email = request.form['email']
    # Aqui você pode salvar os dados em um banco de dados, por exemplo
    # Por enquanto, vamos apenas imprimir os dados
    print('Nome:', nome)
    print('Email:', email)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

