from flask import Flask, request, render_template, flash, url_for, redirect
import csv

app = Flask(__name__)
app.secret_key="your_secret_key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/save', methods=['POST'])
def save_data():
    nom=request.form['name'].strip()
    #space for more info here

    try:
        with open("users.csv", "a", encoding="utf-8", newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([nom])
        flash("Données sauvegardées avec succès !")
    except Exception as e:
        flash("Error : {e}")
    return redirect(url_for("index"))
    
if __name__=="__main__":
    app.run(debug=True)