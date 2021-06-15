from flask import Flask, render_template, request, redirect, jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('sophome.html')

@app.route("/soprun",methods=["POST"])
def soprun():
    if request.method=="POST":
        btnid=request.form.get('clickbutton')
        print(btnid)
        returnmsg="My return message"
        #print(returnmsg)
        return render_template("/sophome.html",returnmsg=returnmsg)

if __name__ == "__main__":
    app.run(debug=True)