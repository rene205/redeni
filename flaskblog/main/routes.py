#--------------Bearbeitet von René Aumann--------------#


from flask import render_template, request, Blueprint
from flaskblog.models import Post, Addproduct

main = Blueprint('main', __name__)


#---------------------------------------------------Route die zur Startseite der Website führt------------------------------------------
#Zwei Routen führen dabei zum Ziel auf die Hompage zu gelangen
@main.route('/')
@main.route("/home")
def home():
    #In der folgenden Zeile werden die 6 neusten Produkte, die im Angebot sind, herausgesucht
    #Diese Liste wird für das Carousel auf der Startseite benötigt
    carouselproducts = Addproduct.query.filter(Addproduct.discount > 0).order_by(Addproduct.pub_date.desc()).limit(6)

    #Hier werden die 4 neusten Produkte herausgefilter, welche ebenfall auf der Startseite angezeigt werden 
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.pub_date.desc()).limit(4)
    page = request.args.get('page', 1, type=int)

    #Es wird hier geregelt, wie viele (4) und in welcher Reihenfolge (die neusten zuerst) die Kommentare auf der Startseite angezeigt werden
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    
    return render_template("home.html", posts=posts, products=products, carouselproducts=carouselproducts)


