from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


#### create database comments ####
# from app import db
# from app import Person, Segment_skor, Sehir_skor
# db.create_all()
# person_1 = Person(kimlik='1234', ad_soyad='hasan d', gelir='5000', tel= '0543', ikamet='34', segment_skor='10000', sehir_skor= '7')
# person_2 = Person(kimlik='3456', ad_soyad='ahmet d', gelir='10000', tel= '0532', ikamet='35', segment_skor='15000', sehir_skor= '6')
# segment_skor_1 = Segment_skor(person_kimlik='1234', segment_skor='7')
# segment_skor_2 = Segment_skor(person_kimlik='3456', segment_skor='6')
# sehir_skor_1 = Sehir_skor(ikamet_il='34', sehir_skor='10000')
# sehir_skor_2 = Sehir_skor(ikamet_il='35', sehir_skor='15000')
# db.session.add(person_1)
# db.session.add(person_2)
# db.session.add(segment_skor_1)
# db.session.add(segment_skor_2)
# db.session.add(sehir_skor_1)
# db.session.add(sehir_skor_2)
# db.session.commit()



app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"localhost": "*"}})
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Person(db.Model):
    kimlik = db.Column(db.Integer, primary_key=True)
    ad_soyad = db.Column(db.String(50), unique=True, nullable=False)
    gelir = db.Column(db.Integer, nullable=False)
    tel = db.Column(db.String(12), unique=True, nullable=False)
    ikamet = db.Column(db.Integer, nullable=False)
    segment_skor = db.Column(db.Integer, nullable=False)
    sehir_skor = db.Column(db.Integer, nullable=False)
    segment_skoru = db.relationship('Segment_skor', backref='segment_skor_kimlik', lazy=True)
    sehir_skoru = db.relationship('Sehir_skor', backref='sehir_skor_il', lazy=True)

    def __repr__(self):
        return f"Person('{self.kimlik}', '{self.ad_soyad}', '{self.gelir}', '{self.tel}', '{self.ikamet}', '{self.segment_skor}', '{self.sehir_skor})"


class Segment_skor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    segment_skor = db.Column(db.Integer, nullable=False) # 1-9
    person_kimlik = db.Column(db.Integer, db.ForeignKey('person.kimlik'), nullable=False)

    def __repr__(self):
        return f"Skor_Segment('{self.person_kimlik}', '{self.segment_skor}')"

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
        'sehir_skor': '15000',
    }
]


@app.route("/showScore", methods=["GET"])
def showScore():
    try:
        # kimlik_no = request.args.get('kimlik')
        kimlik_no='12345'
        person = Person.query.filter_by(kimlik=kimlik_no).first()
        print(person.kimlik)
        return jsonify(kimlik_no)

        # if control > 0:
        #     datas = cur.fetchall()

        #     for data in datas:
        #         obj = { "id": data[0], "title": data[1], "albumId": data[2], "artistName1": data[3], "artistName2": data[4], "artistName3": data[5], "artistName4": data[6] }
        #         songs.append(obj)
        # else:
        #     print("Kayit bulunamadi")

        # return jsonify({'data': songs})
    except Exception as e:
        return False

if __name__ == '__main__':
    app.run(debug=True)