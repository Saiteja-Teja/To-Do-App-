from flask import Blueprint,request,redirect,url_for,render_template,flash,session
auth_bp=Blueprint('auth',__name__)
user_credentials={'username':'admin','password':'123'}
@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        if username==user_credentials['username'] and password==user_credentials['password']:
            session['user']=username
            flash('login successful','success')
            return redirect(url_for('task.view_tasks'))
        else:
            flash('invalid credentials', 'danger')
    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('logout successful','success')
    return redirect(url_for('auth.login'))

