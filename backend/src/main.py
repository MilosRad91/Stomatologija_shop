
from flask import Flask,render_template,request,session,redirect,url_for,jsonify,json
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "RAF2021-2022"


def get_db_connection():
	return mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="stomatologija_shop"
	)

@app.route('/')
def main():
	return 'Hello world'

@app.route('/korisnici')
def korisnici():
	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = """	SELECT *
				FROM korisnici 
			 """
	cursor.execute(upit)
	data = cursor.fetchall()

	return jsonify({
		"korisnici" : data,
		"message" : "Korisnici uspesno preuzeti iz baze"
	})

@app.route('/korisnici/sve-vrste')
def sve_vrste_korisnika():
	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = """	SELECT *
				FROM korisnici 
				JOIN vrsta_korisnika ON vrsta_korisnika.id = korisnici.vrsta_korisnika_id
				WHERE vrsta_korisnika.naziv = 'kupac' OR vrsta_korisnika.naziv = 'prodavac' 
			"""
	cursor.execute(upit)
	data = cursor.fetchall()

	return jsonify({
		"sve_vrste_korisnika" : data,
		"message" : "Kupci uspesno preuzeti iz baze"
	}), 200


@app.route('/registracija/korisnik', methods=['POST'])
def registracija_korisnik():
	data = request.get_json()
	
	username = data.get('username')
	password = data.get('password')
	email = data.get('email')
	godina_rodjenja = data.get('godina_rodjenja')
	trenutno_stanje_novca = data.get('trenutno_stanje_novca')
	vrsta_korisnika_id = data.get('vrsta_korisnika_id')
	
	print(f"Primljeni podaci: Username-{username}\n,Password-{password}\n,Email-{email}\n,Godina rodjenja-{godina_rodjenja}\n,Stanje na racunu-{trenutno_stanje_novca}\n,Vrsta korisnika-{vrsta_korisnika_id}")

	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = "INSERT INTO korisnici VALUES (null,%s,%s,%s,%s,%s,%s)"
	params = (username,password,email,godina_rodjenja,trenutno_stanje_novca,vrsta_korisnika_id)
	cursor.execute(upit,params)
	mydb.commit()

	return jsonify({
		"message": "Podaci su uspešno primljeni!"
	}), 200


@app.route('/login', methods=['POST'])
def uloguj_se():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')

	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = '''
		SELECT *
        FROM korisnici k
        JOIN vrsta_korisnika v ON k.vrsta_korisnika_id = v.idVrstaKorisnika
        WHERE k.email = %s AND k.password = %s
	'''
	params = (email,password)
	cursor.execute(upit,params)
	korisnik = cursor.fetchone()
	print(korisnik['idKorisnici'])
	if korisnik:
		if korisnik['naziv'] == "kupac":
			cursor_korpa = mydb.cursor(dictionary=True)
			upit_korpa = '''
				INSERT INTO korpa
				VALUES (null, %s, CURDATE(), %s);
			'''
			params = (korisnik['idKorisnici'],'aktivna')
			cursor_korpa.execute(upit_korpa,params)
			mydb.commit()

			upit_korpa2 = '''
				SELECT * FROM korpa
				WHERE korpa.status = 'aktivna'
			'''
			cursor.execute(upit_korpa2)
			korpa = cursor.fetchone()

			session['korisnik_id'] = korisnik['idKorisnici']
			session['vrsta_korisnika'] = korisnik['naziv']
		
			return {'message': 'Uspesno logovanje', 'korisnik': korisnik, 'korpa' : korpa}, 200
		
		session['korisnik_id'] = korisnik['idKorisnici']
		session['vrsta_korisnika'] = korisnik['naziv']
		return {'message': 'Uspesno logovanje', 'korisnik': korisnik}, 200
	else:
		return {'message': 'Neadekvatni kredencijali za logovanje'}, 401


@app.route('/proizvodi')
def proizvodi():
	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = "SELECT * FROM proizvodi JOIN korisnici ON prodavac_id = korisnici.idKorisnici"
	cursor.execute(upit)
	data = cursor.fetchall()

	return jsonify({
		"proizvodi" : data,
		"message" : "Proizvodi uspesno preuzeti iz baze"
	}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	korisnik = data.get('korisnik')

	if isinstance(korisnik, str):
		korisnik = json.loads(korisnik)

	session.clear()

	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = '''
		UPDATE korpa
		SET status = 'otkazana'
		WHERE kupac_id = %s AND status != 'finalizovana';
	'''
	param = (korisnik['korisnik_id'], )
	cursor.execute(upit,param)
	mydb.commit()

	cursor2 = mydb.cursor(dictionary=True)
	upit2 = '''
		DELETE kp
		FROM korpa_proizvodi kp
		JOIN korpa k ON kp.korpa_id = k.idKorpa
		WHERE k.status = 'otkazana'
	'''
	cursor2.execute(upit2)
	mydb.commit()

	return jsonify({
		"message" : "Uspesno ste se odjavili"
	}), 200


@app.route('/korisnik', methods=['POST'])
def korisnik():
	data = request.get_json()
	ulogovani_korisnik_id = data.get('id_korisnika')
	print(ulogovani_korisnik_id)

	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = "SELECT * FROM korisnici WHERE idKorisnici=%s"
	param = (ulogovani_korisnik_id, )
	cursor.execute(upit,param)
	data = cursor.fetchone()

	return jsonify({
		"korisnik" : data,
		"message" : "Korisnik uspesno preuzeti iz baze"
	}), 200

@app.route('/dodaj_u_tabelu_korpa_proizvodi', methods=['POST'])
def dodaj_u_tabelu_korpa_proizvodi():
	data = request.get_json()
	
	kolicina_u_korpi = data.get('kolicina_u_korpi')
	cena = data.get('cena')
	proizvod_id = data.get('proizvod_id')
	korpa_id = data.get('korpa_id')
	prodavac_id = data.get('prodavac_id')

	print(f"Primljeni podaci: {data}")

	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)

	upit_provera = "SELECT * FROM korpa_proizvodi WHERE korpa_id = %s AND proizvod_id = %s"
	params_provera = (korpa_id, proizvod_id)
	cursor.execute(upit_provera, params_provera)
	proizvod = cursor.fetchone()

	if proizvod:
		upit_update = """
        	UPDATE korpa_proizvodi 
        	SET kolicina_u_korpi = kolicina_u_korpi + %s
        	WHERE korpa_id = %s AND proizvod_id = %s
    	"""
		params_update = (kolicina_u_korpi, korpa_id, proizvod_id)
		cursor.execute(upit_update, params_update)
		
	else:
		upit_insert = "INSERT INTO korpa_proizvodi (korpa_id, proizvod_id, kolicina_u_korpi, cena_proizvoda, prodavac_id) VALUES (%s, %s, %s, %s, %s)"
		params_insert = (korpa_id, proizvod_id, kolicina_u_korpi, cena, prodavac_id)
		cursor.execute(upit_insert, params_insert)

	mydb.commit()

	return jsonify({
		"message" : "Podaci su uspesno primljeni"
	}), 200

@app.route('/dohvati_iz_tabele_korpa_proizvodi')
def dohvati_iz_tabele_korpa_proizvodi():
	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = '''
		SELECT * FROM korpa_proizvodi
		JOIN korpa ON korpa_id = korpa.idKorpa
		JOIN proizvodi ON proizvod_id = proizvodi.idProizvodi
		JOIN korisnici ON korpa_proizvodi.prodavac_id = korisnici.idKorisnici
		WHERE korpa.status = 'aktivna'
	'''

	cursor.execute(upit)
	data = cursor.fetchall()
	
	if data:
		return jsonify({
			"odabrani_proizvodi" : data,
			"message" : "Uspesno preuzeto iz baze"
		}), 200
	else:
		return jsonify({
			"message" : "Greska prilikom dohvatanja podataka"
		}), 401

@app.route('/obrisi_stavke_iz_korpe')
def obrisi_stavke_iz_korpe():
	mydb = get_db_connection()
	cursor = mydb.cursor(dictionary=True)
	upit = '''
		DELETE kp 
		FROM korpa_proizvodi kp
		JOIN korpa k ON kp.korpa_id = k.idKorpa
		WHERE k.status = 'aktivna';
	'''
	cursor.execute(upit)
	mydb.commit()

	return jsonify({
		"message" : "Uspesno obrisani podaci iz tabele korpa_proizvodi"
	}), 200

app.run(debug=True)
