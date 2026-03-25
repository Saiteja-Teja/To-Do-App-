from flask import Blueprint,request,redirect,url_for,session,render_template,flash
from app import db
from app.models import Task
task_bp=Blueprint('task',__name__)
@task_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    tasks=Task.query.all()
    return render_template('tasks.html',tasks=tasks)
@task_bp.route('/add',methods=["POST"])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('task added successfully', 'success')
    return redirect(url_for('task.view_tasks'))
@task_bp.route('/toggle/<int:task_id>',methods=['POST'])
def toggle_status(task_id):
    task=Task.query.get(task_id)
    if task:
        if task.status=='Pending':
            task.status='Working'
        elif task.status=='Working':
            task.status='Completed'
        else:
            task.status="Pending"
        db.session.commit()
    return redirect(url_for('task.view_tasks'))
@task_bp.route('/clear',methods=['POST'])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('all tasks are deleted','info')
    return redirect(url_for('task.view_tasks'))

    
