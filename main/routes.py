from main import app
from flask import render_template, url_for, flash, redirect,request
from main.forms import RegistrationForm, LoginForm , ContactForm
from main.models import User,Book
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
#request
from main import db, bcrypt,mail

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    msg = Message("Feedback for Online Bookstore Management Website",
            sender="decodemysteries2021@gmail.com",
            recipients=["receiver1@gmail.com","receiver2@gmail.com"])

    msg.body = '''Hey developers,
    A Client just viewed your website. The Details of feedback are:
                  
    Name of client: %s
    Email address: %s
    Feedback from client: %s
    '''%(form.name.data,form.email.data,form.feedback.data)
    mail.send(msg)
    
    if form.validate_on_submit():
        flash('Your feedback has been sent! We will get back to you shortly', 'success')
        return redirect(url_for('home'))

    return render_template('contact.html',title='Contact',form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, phone=form.phone.data, address=form.address.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
