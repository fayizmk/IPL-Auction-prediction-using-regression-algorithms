from flask import Flask, render_template, request
import numpy as np

import allrounder
import batsman
import bowler
import wicketkeeper


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        typ = request.form["type"] 
    return render_template("sub.html", t = typ)

@app.route("/ar_p", methods = ["POST"])
def pred_ar():
    if request.method == "POST":
        int_features = [int(x) for x in request.form.values()]
        final_feature = [np.array(int_features)]
        prd = allrounder.pred_ar(final_feature)
    return render_template("ar_p.html", p = float(prd))         
@app.route("/bat_p", methods = ["POST"])
def pred_bat():
    if request.method == "POST":
        int_features = [int(x) for x in request.form.values()]
        final_feature = [np.array(int_features)]
        prd = batsman.pred_bat(final_feature)
    return render_template("bat_p.html", p = float(prd))         

@app.route("/bowl_p", methods = ["POST"])

def pred_bowl():
    if request.method == "POST":
       int_features = [int(x) for x in request.form.values()]
       final_feature = [np.array(int_features)]
       prd = bowler.pred_bowl(final_feature)
    return render_template("bowl_p.html", p = float(prd))         
      

@app.route("/wk_p", methods = ["POST"])
def pred_wk():
    if request.method == "POST":
        int_features = [int(x) for x in request.form.values()]
        final_feature = [np.array(int_features)]
        prd = wicketkeeper.pred_wk(final_feature)
    return render_template("wk_p.html", p = float(prd))         
     

if __name__  == "__main__":
    app.run(debug = True)
