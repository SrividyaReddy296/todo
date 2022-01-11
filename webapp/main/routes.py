from flask import Blueprint
from flask import render_template, request, Blueprint
from webapp.models import Todo
from flask_login import current_user


main=Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        alltodos = Todo.query.filter_by(user_id=current_user.id).order_by(Todo.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template('home.html',title=current_user.username,alltodos=alltodos)
    else:
        return render_template('home.html',title='home')


@main.route("/about")
def about():
    return render_template('about.html',title='about')

