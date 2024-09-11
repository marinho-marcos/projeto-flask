# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from password import senha

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Porta padrão para TLS; para SSL, use 465
app.config['MAIL_USERNAME'] = 'testeemail.protocolos@gmail.com'
app.config['MAIL_PASSWORD'] = senha
app.config['MAIL_USE_TLS'] = True  #Transport layer security

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        to_email = request.form['to_email']
        
        msg = Message(subject=subject,
                      body=message,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[to_email])
        try:
            mail.send(msg)
            return redirect(url_for('email_sent'))
        except:
            return 'Ocorreu um erro ao enviar o e-mail.'

    return render_template('email_form.html')

@app.route('/sent')
def email_sent():
    return 'E-mail enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')