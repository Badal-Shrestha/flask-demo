from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def add():
    s = 5+5
    return render_template ("index.html",value=s)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)