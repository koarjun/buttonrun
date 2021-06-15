from app import app

"""
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('sophome.html')

@app.route("/soprun",methods=["POST"])
def sop_run():
    if request.method == "POST":
        btnid=request.form.get('clickbutton')
        print(btnid)
        returnmsg = "My return message"
        return render_template("/sophome.html",returnmsg=returnmsg)
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)