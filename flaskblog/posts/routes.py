from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


#-----------------------------------Route zum Erstellen eines Kommentares  ------------------------------------------
@posts.route("/post/new", methods=['GET', 'POST'])
#Die Seite kann nur aufgerufen werden, wenn ein User eingeloggt ist
@login_required
def new_post():
    form = PostForm()
    #Wenn das Kommentarformular korrekt ausgefüllt wurde, wird der Kommentar zur Datenbank hiinzugefügt
    if form.validate_on_submit():
        post = Post(title=form.title.data, content= form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Dein Kommentar wurde veröffentlicht', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Neuer Kommentar', form=form, legend='Neuer Kommentar')


#----------------------------------Route für einen spezifischen Kommentar  ------------------------------------------
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


#-----------------------------------Route zum Aktualisieren eines spezifischen Kommentares  ------------------------------------------
@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    #Zugriff auf den Kommentar ist nur erlaubt, wenn der eingeloggte User auch den Kommentar verfasst hat 
    if post.author != current_user:
        abort(403)
    form = PostForm()
    #Auf der Update-Seite werden der zuvor gespeicherte Titel und die BEschreibung angezeigt
    #Bei einer Aktualisierung wird die Datenbank überschrieben 
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Der Kommentar wurde aktualisiert!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Kommentar aktualisieren', form=form, legend='Kommentar aktualisieren')


#-----------------------------------Route zum Löschen eines spezifischen Kommentares  ------------------------------------------
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    #Zugriff auf den Kommentar ist nur erlaubt, wenn der eingeloggte User auch den Kommentar verfasst hat 
    if post.author != current_user:
        abort(403)
    #Wenn der Löschen Button betätigt wird, werden die Daten des Kommentars aus der Datenbank entfernt
    db.session.delete(post)
    db.session.commit()
    flash('Der Kommentar wurde erfolgreich gelöscht!', 'success')
    return redirect(url_for('main.home'))