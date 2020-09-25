from flask import render_template, request, redirect
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

