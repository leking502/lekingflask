from flask import Flask, request, redirect, flash, url_for, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import database
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'basic'
login_manager.login_view = "login"
login_manager.login_message = "请先登录。"
app.secret_key = "^&F(*G&(G(G*^TG&F^*"


@login_manager.user_loader
def user_loader(user_id):
    return database.UserData.get_user_for_id(user_id)


@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        user_info = request.form.to_dict()
        user = database.UserData.get_user_for_id(user_info.get("username"))


@app.route('/login', methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        user_info = request.form.to_dict()
        user = database.UserData.get_user_for_id(user_info.get("username"))
        if user is None:
            flash("没有该用户", )
            return render_template('login.html')
        if not user_info.get("password") == user.password:
            flash("密码不正确")
            return render_template('login.html')
        login_user(user)
        return redirect(url_for("index"))


@app.route("/", methods=("GET", "POST"))
@login_required
def index():
    if request.method == "GET":
        return render_template("Index.html", current_user=current_user)
    if request.method == "POST":
        logout_user()
        return redirect("/login")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug='True')
