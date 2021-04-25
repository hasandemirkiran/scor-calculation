from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Person(db.Model):
    kimlik = db.Column(db.Integer, primary_key=True)
    ad_soyad = db.Column(db.String(50), unique=True, nullable=False)
    gelir = db.Column(db.Integer, nullable=False)
    tel = db.Column(db.String(12), unique=True, nullable=False)
    ikamet = db.Column(db.Integer, nullable=False)
    segment_skoru = db.relationship('Segment_skor', backref='segment_skor_kimlik', lazy=True)
    sehir_skoru = db.relationship('Sehir_skor', backref='sehir_skor_il', lazy=True)

    def __repr__(self):
        return f"Person('{self.kimlik}', '{self.ad_soyad}', '{self.gelir}', '{self.tel}', '{self.ikamet})"


class Segment_skor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    segment_skor = db.Column(db.Integer, nullable=False) # 1-9
    person_kimlik = db.Column(db.Integer, db.ForeignKey('person.kimlik'), nullable=False)

    def __repr__(self):
        return f"Skor_Segment('{self.person_kimlik}', '{self.skor_segment}')"

class Sehir_skor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ikamet_il = db.Column(db.Integer, db.ForeignKey('person.ikamet'), nullable=False)
    sehir_skor = db.Column(db.Integer, nullable=False) # 0-20.000

    def __repr__(self):
        return f"Sehir_skor('{self.ikamet_il}', '{self.sehir_skor}')"



segment_skoru = [
    {
        'segment_skor_kimlik': '1234',
        'segment_skor': '7',
    },
    {
        'segment_skor_kimlik': '3456',
        'segment_skor': '6',
    }
]

sehir_skoru = [
    {
        'sehir_skor_il': '34',
        'sehir_skor': '10000',
    },
    {
        'sehir_skor_il': '35',
        'sehir_skor': '150000',
    }
]
# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html', posts=posts)


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)