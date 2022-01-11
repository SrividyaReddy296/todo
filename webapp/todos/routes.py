from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from webapp import db
from webapp.models import Todo
from webapp.todos.forms import TodoForm

todos=Blueprint('todos',__name__)



@todos.route("/todo/new", methods=['GET', 'POST'])
@login_required
def new_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(todo)
        db.session.commit()
        flash('Your Todo has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_todo.html', title='New Todo',
                           form=form, legend='New Todo')


@todos.route("/todo/<int:todo_id>/update", methods=['GET', 'POST'])
@login_required
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    form = TodoForm()
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.content = form.content.data
        db.session.commit()
        flash('Your Todo has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.title.data = todo.title
        form.content.data = todo.content
    return render_template('create_todo.html', title='Update Todo',
                           form=form, legend='Update Todo')


@todos.route("/todo/<int:todo_id>/delete", methods=['POST'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('Your todo has been deleted!', 'success')
    return redirect(url_for('main.home'))

