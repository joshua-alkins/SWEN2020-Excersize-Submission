import flask
import os

from flask_mail import Mail
from flask_mail import Message

mail = Mail()

app = flask.Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mfa.registry.team@gmail.com'#os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = 'valiantl3adershane'#os.environ.get('MAIL_PASSWORD')

mail.init_app(app)

msg = Message('test subject', sender='mfa.registry.team@gmail.com', recipients=['jason.charles105@gmail.com','joshua_alkins@hotmail.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)
