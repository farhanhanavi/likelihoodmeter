from datetime import datetime
from flaskblog.__innit__ import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    ktp = db.Column(db.String(16), unique = True, nullable = False)
    nama = db.Column(db.String(30), nullable = False)
    nomor_hp = db.Column(db.String(15), nullable = False)
    umur = db.Column(db.String(2), nullable = False)
    jenis_kelamin = db.Column(db.String(10), nullable = False)
    alamat = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

    kontak = db.relationship('ContactHistory', backref = 'testcontactuser', lazy = True)
    gejala = db.relationship('Symptoms', backref = 'testsymptomsuser', lazy = True)
    categories = db.relationship('Categories', backref = 'testcategoriesuser', lazy = True)
    def __repr__(self):
        return f"user('{self.ktp}', '{self.nama}', '{self.email}', '{self.password}')"



class ContactHistory(db.Model):
    contact_id = db.Column(db.Integer, nullable= False, primary_key = True) 
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    riwayat_jalan = db.Column(db.String(10), nullable = False)
    riwayat_kontak = db.Column(db.String(10), nullable = False)
    riwayat_kontak_pdp = db.Column(db.String(10), nullable = False)
    contactresult = db.Column(db.Integer, nullable = False, default = '0')

    
    def __repr__(self):
        return f"result('{self.riwayat_jalan}', '{self.riwayat_kontak}', '{self.riwayat_kontak_pdp}', '{self.contactresult}')"   

class Symptoms(db.Model):
    symptomsid = db.Column(db.Integer, nullable= False, primary_key = True) 
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)   
    demam = db.Column(db.String(10), nullable = False)
    batuk = db.Column(db.String(10), nullable = False)
    pilek = db.Column(db.String(10), nullable = False)
    nyeri_tenggorokan = db.Column(db.String(10), nullable = False)
    sesak = db.Column(db.String(10), nullable = False)
    symptomsresult = db.Column(db.Integer)
    
				
    
    def __repr__(self):
        return f"result('{self.demam}', '{self.batuk}', '{self.pilek}',''{self.nyeri_tenggorokan}','{self.sesak}', '{self.symptomsresult}')"

class Categories(db.Model):
    response_id = db.Column(db.Integer, nullable = False, primary_key = True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    contact_result = db.Column(db.Integer)
    symptoms_result = db.Column(db.Integer)
    categories = db.Column(db.String(20), nullable = False, default = 'test')
    def __repr__(self):
        return f"result('{self.categories}')"