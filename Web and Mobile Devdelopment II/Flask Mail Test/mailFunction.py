import flask

from flask_mail import Mail
from flask_mail import Message


def sendVerificationEmail(link, subject, textBody, recipient):
    #Sends a Verification Email with a link to the recipiant
    email = 'mfa.registry.team@gmail.com'
    password = 'valiantl3adershane'
    mail = Mail()

    app = flask.Flask(__name__)

    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = email #os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = password #os.environ.get('MAIL_PASSWORD')
 
    mail.init_app(app)

    msg = Message(subject, sender='MFA Team', recipients=[recipient])
    msg.body = 'text body'
    msg.html = '<p>'+textBody+':</p>'+'<br>'+link
    with app.app_context():
        mail.send(msg)


sendVerificationEmail('google.com', 'verification test', 'here is a link to google','joshua_alkins@hotmail.com')