from flask import render_template, request, redirect, jsonify, make_response
from app import app

from datetime import datetime

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.template_filter()
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/jinja")
def jinja():
    my_name = 'Augustine'
    my_age = 30
    langs = ['Python', 'Javascript', 'Java', 'Rust']
    friends = {
        'Judi': 27,
        'Tom': 29,
        'David': 25,
        'Taylor': 32
    }
    colors = ('Red', 'Blue')
    cool = True

    class GitRemote:
        def __init__(self, name, description, repos):
            self.name = name
            self.description = description
            self.repos = repos
        
        def pull(self):
            return f"Pulling repo '{self.name}'"
        
        def clone(self):
            return f"Cloning from {self.repos}"
        

    my_remote = GitRemote(
        name="zero_hero",
        description="Software Engineer Zero to Hero",
        repos = "https://github.com/augustine0890/zero-hero.git"
    )

    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h2>This is some HTML</h2>"

    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    return render_template(
        "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, cool=cool, GitRemote=GitRemote,
        my_remote=my_remote, repeat=repeat, date=date, my_html=my_html, suspicious=suspicious
    )

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        req = request.form
        missing = list()

        for k, v in req.items():
            if v == '':
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)

        return redirect(request.url)

    return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):
    user = None
    
    if username in users:
        user = users[username]

    return render_template("/public/dynamic.html", username=username, user=user)

@app.route("/multiple/<foo>/<bar>/<baz>/")
def multiple(foo, bar, baz):
    print(f"foo is {foo}")
    print(f"bar is {bar}")
    print(f"baz is {baz}")

    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json_example():
    # Validate the request body contains JSON
    if request.is_json:
        req = request.get_json()
        response_body = {
            "message": "JSON received!",
            "sender": req.get("name")
        }
        res = make_response(jsonify(response_body), 200)
        return res
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)


