#--------------Bearbeitet von René Aumann--------------#

import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


#---------------------------------------------------Speichern des Profilbilds-------------------------------------------------------
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # An dieser Stelle wird das Bild runterskaliert (Es spart eine Menge Speicherplatz!)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
#-----------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Senden der E-Mail zum zurücksetzen des Passworts--------------------------------
def send_reset_email(user):
    #Zur Authentifizierung wird ein Schlüssel generiert
    token = user.get_reset_token()
    #Der Versender und der Empfänger der Mail wird an dieser Stelle definiert
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    #Hier wird der Inhalt der E-Mail definiert 
    #Der Link inkl. des Schlüssels, damit der Zugriff auf die Seite zum eingeben eines neuen Passwortes besteht, wird übergeben 
    msg.body = f'''Um Ihr Passwort zurückzusetzen, folden Sie dem folgenden Link:
{url_for('users.reset_token', token=token, _external=True)} 
    
Wenn Sie ihr Passwort nicht zurücksetzen wollen, können Sie diese Email ignorieren
'''
    #Die Nachricht wird abgeschickt
    mail.send(msg)
#-----------------------------------------------------------------------------------------------------------------------------------