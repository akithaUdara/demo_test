from flask import Flask , render_template , request

import generate_sen as m



app = Flask(__name__)


@app.route("/", methods = ['POST'])
def hello():
    if request.method == "POST":
        keywords = request.form("keywords")
        keyInput = keywords.split(" ")

        sentence = m.sentenceGen(keyInput)
        print(sentence)

    return render_template("index.html")
 


# @app.route("/sub", methods = ['POST'])
# def submit():
#     #Html -> .py
#     if request.method == "POST":
#         name = request.form["username"]

#     #.py -> Html
#     return render_template("sub.html", n = name)



if __name__ == "__main__":
    app.run()