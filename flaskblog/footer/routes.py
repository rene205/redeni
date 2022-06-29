#--------------Bearbeitet von Nikos Papaspiros--------------#

from flask import render_template, Blueprint

footer = Blueprint('footer', __name__)

#---------------------------------------------------Footer: Link zum Impressum---------------------------------------------------------------
@footer.route('/impressum')
def impressum():
    return render_template("footer/impressum.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zum Bereich FAQ-------------------------------------------------------------
@footer.route('/faq')
def faq():
    return render_template("footer/faq.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zu den Garantieinformationen------------------------------------------------
@footer.route('/garantie')
def garantie():
    return render_template("footer/garantie.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zum den Kontaktinformationen------------------------------------------------
@footer.route('/kontakt')
def kontakt():
    return render_template("footer/kontakt.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zu den AGB------------------------------------------------------------------
@footer.route('/agb')
def agb():
    return render_template("footer/agb.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zu den Rücksendeinformationen-----------------------------------------------
@footer.route('/ruecksendung')
def ruecksendung():
    return render_template("footer/ruecksendung.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zu den Versand und Lieferinformationen--------------------------------------
@footer.route('/versand_lieferung')
def versand_lieferung():
    return render_template("footer/versand_lieferung.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zu den Zahlungsinformationen------------------------------------------------
@footer.route('/zahlung')
def zahlung():
    return render_template("footer/zahlung.html")
#--------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------Footer: Link zur About Page--------------------------------------------------------------
@footer.route("/about")
def about():
    return render_template('footer/about.html', title='About')
#--------------------------------------------------------------------------------------------------------------------------------------------