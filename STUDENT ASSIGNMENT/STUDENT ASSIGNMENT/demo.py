from flask import Flask, url_for,redirect
app = Flask(__name__)
@app.route("/faculty")
def hi():
    return"hearty welcome"
@app.route("/type/<desg>")
def desg(desg):
    return "welcome all"  + desg +  "to CAD class"
@app.route("/to/<person>")
def to(person):
    if person == "faculty":
        return redirect(url_for("faculty"))
    else:
        return redirect(url_for("desg",desg = person))
    
if __name__=="__main__":
    app.run(debug=True)