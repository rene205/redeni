#--------------Bearbeitet von Nikos Papaspiros--------------#

from flask import render_template, request, Blueprint
from flaskblog.models import Addproduct, Brand, Category
from flaskblog import app

items = Blueprint('items', __name__)


#---------------------------------------------------Anzeigen der Suchergebnisse--------------------------------------------------------------
@app.route('/search')
def search():
    #Das in die Suchleiste eingegebene Suchwort wird als "searchword" gespeichert.
    keyword = request.args.get('s')
    #Anschließend wird mit dem Suchwort in der Datenbank "Addproduct" nach dem Suchwort in den Spalten "name" und "desc" gesucht.
    #Die Ergebnisse werden in "products" gespeichert.
    products = Addproduct.query.msearch(keyword, fields= ['name', 'desc'], limit=20)
    #Rendert das Template und übergibt "products".
    return render_template("products/search.html", products=products)
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Darstellung der Produktseite-------------------------------------------------------------
@items.route("/products")
def products():
    page = request.args.get('page',1, type=int)
    #Filtert alle Produkte aus der Datenbank, die auf Lager sind und speichert diese dann in "products"
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=12)
    #Rendert das Template und übergibt die Produkte
    return render_template("products/products.html", products = products)
#--------------------------------------------------------------------------------------------------------------------------------------------  


#---------------------------------------------------Anzeigen einer einzelnen Produktseite----------------------------------------------------
@items.route("/product/<int:id>")
def single_page(id):
    #Beim anklicken eines Produktes auf der Produktübersichtsseite, wird die Produkt ID an die Funktion "single_page" übergeben.
    #Es wird dann das entsprechende Produkt aus der Datenbank abgerufen. 
    product = Addproduct.query.get_or_404(id)
    #Rendert das Template und übergibt das Produkt.
    return render_template('products/single_page.html', product = product)
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Kategorien anzeigen (Nutzeransicht)---------------------------------------
@items.route('/category/<int:id>')
def get_category(id):
    page = request.args.get('page',1, type=int)
    #Die Kategorie, welche angezeigt werden soll, wird anhand der ID aus der Datenbank abgerufen und in Variable "c" gespeichert. 
    c = Category.query.filter_by(id=id).first_or_404()
    #Alle Produkte, die zu der Kategorie gehören, werden aus der Datenbank abgerufen. 
    category = Addproduct.query.filter_by(category=c).paginate(page=page, per_page=4)
    #Das Template wird gerendert und "category" und "c" werden übergeben.
    return render_template('products/products.html', category = category, c=c)
#-----------------------------------------------------------------------------------------------------------------------------
    

#---------------------------------------------------Marken anzeigen (Nutzeransicht)-------------------------------------------
@items.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page',1, type=int)
    #Die Marke, welche angezeigt werden soll, wird anhand der ID aus der Datenbank abgerufen und in Variable "b" gespeichert. 
    b = Brand.query.filter_by(id=id).first_or_404()
    #Alle Produkte, die zu der Marke gehören, werden aus der Datenbank abgerufen. 
    brand2 = Addproduct.query.filter_by(brand=b).paginate(page=page, per_page=4)
     #Das Template wird gerendert und "brand2" und "b" werden übergeben.
    return render_template('products/products.html', brand2 = brand2, b=b)
#-----------------------------------------------------------------------------------------------------------------------------
