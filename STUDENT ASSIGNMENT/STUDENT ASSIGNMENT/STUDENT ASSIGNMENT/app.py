from flask import Flask, render_template,request,session
import ibm_db
app = Flask(__name__)
app.secret_key = "_ab+d=5"
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;UID=vwd61428;PWD=Ncnf5RiccrZvLDvn;SECURITY=SSL;SSLCERTIFICATE=DigiCertGlobalRootCA.crt",'','')
print(ibm_db.active(conn))
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        global uname
        uname = request.form['username']
        pword = request.form['password']
        print(uname,pword)
        sql = "SELECT * FROM REGISTER WHERE USERNAME = ? AND password = ?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt ,1,uname)
        ibm_db.bind_param(stmt ,2,pword)
        ibm_db.execute(stmt)
        out = ibm_db.fetch_assoc(stmt)
        print(out) 
        if out != False:
            session['username'] = uname
            session['emailid'] = out['EMAILID']
         
            if out['ROLE'] == 0:
                return render_template("adminprofile.html",username = uname, emailid = out['EMAILID'])
            elif out['ROLE'] == 1:
                return render_template("studentprofile.html",username = uname, emailid = out['EMAILID'])
            else:
                return render_template("facultyprofile.html" ,username = uname, emailid = out['EMAILID'])
        else:
            msg = "invalid credentials"
            return render_template("login.html",message1=msg)
    return render_template ("login.html")
@app.route("/register")
def register():
    return render_template ("register.html")
        
if __name__=="__main__":
    app.run(debug=True)