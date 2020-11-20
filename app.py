from flask import Flask, render_template, redirect
from flask_fontawesome import FontAwesome

app = Flask(__name__)
fa = FontAwesome(app)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/rstudio')
def open_rstudio():
    return redirect("http://localhost:8787", code=302)
@app.route('/hadoop')
def open_hadoop():
    return redirect("http://localhost:9870", code=302)
@app.route('/ibmsas')
def open_sas():
    return redirect("https://welcome.oda.sas.com/login", code=302)
@app.route('/tableau')
def open_tableau():
    return redirect("https://sso.online.tableau.com/public/idp/SSO", code=302)
@app.route('/wetty')
def open_wetty():
    return redirect("http://localhost:3000/wetty/ssh/term?pass=term", code=302)
@app.route('/sonar')
def open_sonar():
    return redirect("http://localhost:9001", code=302)    
@app.route('/jupyter')
def open_jupy():
    return redirect("http://localhost:8888?token=easy", code=302)
@app.route('/tensor')
def open_tensor():
    return redirect("http://localhost:8889?token=easy", code=302)
@app.route('/markdown')
def open_markdown():
    return redirect("http://localhost:12345", code=302)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')