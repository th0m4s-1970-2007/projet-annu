from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pc_database.db'
db = SQLAlchemy(app)

# Définition de la classe PCPortable pour représenter les informations d'un PC portable
class PCPortable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prix = db.Column(db.Float)
    taille_ecran = db.Column(db.Float)
    carte_graphique = db.Column(db.String(100))
    ram = db.Column(db.Integer)
    stockage = db.Column(db.Integer)
    processeur = db.Column(db.String(100))

    def __repr__(self):
        return '<PCPortable {}>'.format(self.id)

# Page d'accueil de l'application web
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prix = request.form['prix']
        taille_ecran = request.form['taille_ecran']
        carte_graphique = request.form['carte_graphique']
        ram = request.form['ram']
        stockage = request.form['stockage']
        processeur = request.form['processeur']

        # Recherche des PC portables correspondant aux critères de l'utilisateur
        pcs = PCPortable.query.filter(
            PCPortable.prix <= prix,
            PCPortable.taille_ecran == taille_ecran,
            PCPortable.carte_graphique == carte_graphique,
            PCPortable.ram == ram,
            PCPortable.stockage == stockage,
            PCPortable.processeur == processeur
        ).all()

        return render_template('results.html', pcs=pcs)

    return render_template('index.html')

# Page pour afficher les résultats de la recherche
@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
