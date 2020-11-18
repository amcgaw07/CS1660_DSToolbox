from flask import Flask, render_template
from flask_fontawesome import FontAwesome
app = Flask(__name__)
fa = FontAwesome(app)

@app.route('/')
def hello_world():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')