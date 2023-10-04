from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return '<p>logout</p>'
 
@auth.route('/sign-up',  methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be more than 3 chars', category='error')
        elif len(firstname) < 2:
            flash('Firstname must be more than 1 chars', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be more than 7 chars', category='error')
        else:
            flash('User added', category='success')
    return render_template('sign_up.html')