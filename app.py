from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators


def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise validators.ValidationError('Name must have more then 3 characters')

class ContactForm(FlaskForm):
    name = StringField('Your Name:', [validators.DataRequired(), CheckNameLength])
    email = StringField('Your e-mail address:', [validators.DataRequired(), validators.Email('your@email.com')])
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('Send Message')

app = Flask(__name__)

app.secret_key='mysecretkey'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'maciejsmusz@gmail.com'
app.config['MAIL_PASSWORD'] = 'Charlemagne'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def static_page():
    # form = ContactForm()

    # if request.method == 'POST':
    #     if form.validate() == False:
    #         return 'Please fill in all fields'
    #     else:
    #         msg = Message("Message from your visitor: " + form.name.data, sender='sender', recipients=['maciejsmusz@gmail.com'])
    #         msg.body = """ From: %s <%s>, %s""" % (form.name.data, form.email.data, form.message.data)
    #         mail.send(msg)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
