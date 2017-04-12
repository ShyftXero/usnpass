from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import itertools


class passForm(FlaskForm):
	password = StringField("Your password", validators=[DataRequired()])
	submit = SubmitField("check password")


def leetlist(str):
	str = str.lower()
	# return a list of strings that have been made as 1337 as possible
	leet_matches = [['a', 'A', '4', '@'],
					['b', 'B', '8', '|3'],
					['c', 'C', '<', '('],
					['d', 'D', '|)'],
					['e', 'E', '3'],
					['f', 'F'],
					['g', 'G', '6'],
					['h', 'H', '|-|'],
					['i', 'I', '1', '!'],
					['j', 'J'],
					['k', 'K', '|<'],
					['l', 'L', '1', '|'],
					['m', 'M', '/\/\\'],
					['n', 'N', '|\|'],
					['o', 'O', '0', '(/)', '()'],
					['p', 'P'],
					['q', 'Q'],
					['r', 'R'],
					['s', 'S', '$', '5'],
					['t', 'T', '+', '7'],
					['u', 'U', '|_|'],
					['v', 'V', '\/'],
					['w', 'W', '\/\/'],
					['x', 'X', '><'],
					['y', 'Y'],
					['z', 'Z', '2']]
	ret = []
	for letter in str:
		for match in leet_matches:
			if match[0] == letter:
				ret.append(match)

	return list(itertools.product(*ret))

def check_password(password):
	print("Checking password: ", password)
	score = 0
	res = ""
	bigrams = ['TH', 'EN', 'NG', 'HE', 'AT', 'AL', 'IN', 'ED', 'IT', 'ER', 'ND', 'AS', 'AN', 'TO', 'IS', 'RE', 'OR', 'HA', 'ES', 'EA', 'ET', 'ON', 'TI', 'SE', 'ST', 'AR', 'OU', 'NT', 'TE', 'OF']
	trigrams = ['THE', 'ERE', 'HES', 'AND', 'TIO', 'VER', 'ING', 'TER', 'HIS', 'ENT', 'EST', 'OFT', 'ION', 'ERS', 'ITH', 'HER', 'ATI', 'FTH', 'FOR', 'HAT', 'STH', 'THA', 'ATE', 'OTH', 'NTH', 'ALL', 'RES', 'INT', 'ETH', 'ONT']
	quadgrams = ['TION', 'OTHE', 'THEM', 'NTHE', 'TTHE', 'RTHE', 'THER', 'DTHE', 'THEP', 'THAT', 'INGT', 'FROM', 'OFTH', 'ETHE', 'THIS', 'FTHE', 'SAND', 'TING', 'THES', 'STHE', 'THEI', 'WITH', 'HERE', 'NGTH', 'INTH', 'THEC', 'IONS', 'ATIO', 'MENT', 'ANDT']
	symbols = [' ', '!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
	double_digits = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99']
	quad_digits = ['1900','1901','1902','1903','1904','1905','1906','1907','1908','1909','1910','1911','1912','1913','1914','1915','1916','1917','1918','1919','1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939','1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2044','2045','2046','2047','2048','2049','2050','2051','2052','2053','2054','2055','2056','2057','2058','2059','2060','2061','2062','2063','2064','2065','2066','2067','2068','2069','2070','2071','2072','2073','2074','2075','2076','2077','2078','2079','2080','2081','2082','2083','2084','2085','2086','2087','2088','2089','2090','2091','2092','2093','2094','2095','2096','2097','2098','2099']
	keyboard_patterns = ['asdf', 'jkl;']

	#words and stuff...
	bad_words = ['password', 'companyname']
	
	dictionary_words = [] #open a list of dictionary words and crackalate
	
	for el in bad_words:
		for x in leetlist(el):
			x = ''.join(x)
			count = password.count(el)
			score -= 10 * count
			if count > 0:
				res += " bad_word=" + el + "; "
				break
	
	#using jtr word list # quicker than regex from what I hear
	with open('john.txt', 'r') as f:
		lines = f.read()
		answer = lines.find(password)
		if answer > 0:
			res += " Found in dictionary;"
			score -= 30

		#reverse the list	
		lines = lines[::-1]
		answer = lines.find(password)
		if answer > 0:
			res += " Found in reversed dictionary;"
			score -= 25

	#see mangled.py
	with open('john.txt', 'r') as f:
		words = f.readlines()
		for word in words:
			leets = leetlist(word)
			length = len(leets)
			for perm in leets:
				if ''.join(perm) == password:
					res += " Found in mangle; "
					score -= 10
					break
		
	res += " "

	#character based tests
	for el in bigrams:
		for x in leetlist(el):
			x = ''.join(x)
			count = password.count(x)
			score -= 2 * count
			if count > 0:
				res += '"'+x+'"' + " * " + str(count) + ", "
	
	for el in trigrams:
		for x in leetlist(el):
			x = ''.join(x)
			count = password.count(x)
			score -= 3 * count
			if count > 0:
				res += '"'+x+'"' + " * " + str(count) + ", "
	
	for el in quadgrams:
		for x in leetlist(el):
			x = ''.join(x)
			count = password.count(x)
			score -= 4	* count	
			if count > 0:
				res += '"'+x+'"' + " * " + str(count) + ", "
	

	
	for el in symbols:
		count = password.count(el)
		score += 7 * count


	#length	
	if len(password) < 8:
		res += " Under 8 chars..."
		score -= 25
	if len(password) > 8 and len(password) < 16:
		score += 5
	if len(password) >= 16:
		score += 20




	#numbers
	for el in quad_digits:
		count = password.count(el)
		score -= 1 * count
		if count > 0:
			res += " quad_digits=" + el

	for el in double_digits:
		count = 0
		count = password.count(el)
		score -= 2 * count
		if count > 0:
			pass
			#res += " double_digits=" + el
	
	if score > -25 :
		score += 50	



	ret = "score = %d dings = %s" %(score, res)
	print(ret)
	flash(ret)




app = Flask(__name__)
app.secret_key = 'AKDJI9is92k2***2'

Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
	form = passForm()
	if form.validate_on_submit():
		flash("checked: "+form.password.data)
		check_password(form.password.data)
		return render_template('index.html', form=form)
	
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)
