from flask import Flask , render_template , url_for ,request
import requests , json ,datetime 
from forms import CityTemperatureForm

app = Flask(__name__)
app.secret_key = 'development key'

def url_concatinate(news_url,reference_url,newsApi_key):

	url_for_ref = news_url+reference_url+newsApi_key
	response = requests.get(url_for_ref)
	response_json = response.json()
	articles = response_json['articles']
	return articles

time = datetime.datetime.now()

# @app.route('/')
# def home():
# 	pass



@app.route('/weather',methods=['POST','GET'])
def weather():
	if request.method == "POST":

		id = request.form['town']	 
		url = 'https://api.openweathermap.org/data/2.5/weather?zip={},in&units=metric&appid=ec921c7234e2d713831997a064ca3cc4'
		tem_req = requests.get(url.format(id)).json()
		print(tem_req)
		global weather
		weather ={
			'id':id,
			'city':tem_req['name'],
			'temperature':tem_req['main']['temp'],
			'description':tem_req['weather'][0]['description'],
			'icon':tem_req['weather'][0]['icon'],
			'time':datetime.datetime.fromtimestamp(int(tem_req['sys']['sunrise'])).strftime('%Y-%m-%d %H:%M:%S'),
			'lat_long':(tem_req['coord']['lon'], tem_req['coord']['lat'])
		} 
	return render_template('weather.html',weather = weather)




@app.route('/us')
def news_us():
	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=us&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"

	articles = url_concatinate(sub_url,ref_url,api_key)
	print(type(articles))

	# url = sub_url+ref_url+api_key

	# response = requests.get(url)
	# response_json = response.json()

	# articles = response_json['articles']
	# print(len(articles))
	return render_template('us_news.html',articles=articles)		

@app.route('/india')
def news_india():
	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=in&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"


	articles = url_concatinate(sub_url,ref_url,api_key)
	print(type(articles))
	return render_template('india_news.html',articles=articles)

@app.route('/india/india_business')
def news_india_business():
	#news_items = ['business','entertainment','health','science','sports','technology']

	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=in&category=business&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"

	articles = url_concatinate(sub_url,ref_url,api_key)
	return render_template('business_india.html',articles=articles)




@app.route('/india/india_entertainment')
def news_india_entertainment():
	#news_items = ['business','entertainment','health','science','sports','technology']

	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=in&category=entertainment&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"

	articles = url_concatinate(sub_url,ref_url,api_key)
	return render_template('entertainment_india.html',articles=articles)


@app.route('/india/india_health')
def news_india_health():
	#news_items = ['business','entertainment','health','science','sports','technology']

	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=in&category=health&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"

	articles = url_concatinate(sub_url,ref_url,api_key)
	return render_template('health_india.html',articles=articles)
	 


# @app.route('/india/india_technolcog')
# def news_india_science():
# 	#news_items = ['business','entertainment','health','science','sports','technology']

# 	sub_url = "https://newsapi.org/v2/top-headlines?"
# 	ref_url = "country=in&category=health&"
# 	api_key = "apiKey=e076e68a293b45398aa116162b827787"

# 	articles = url_concatinate(sub_url,ref_url,api_key)
# 	return render_template('india_news.html',articles=articles)

 

@app.route('/india/india_science')
def news_india_science():
	#news_items = ['business','entertainment','health','science','sports','technology']

	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=in&category=science&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"

	articles = url_concatinate(sub_url,ref_url,api_key)
	return render_template('science_india.html',articles=articles)



@app.route('/india/india_sports')
def news_india_sports():
	#news_items = ['business','entertainment','health','science','sports','technology']

	sub_url = "https://newsapi.org/v2/top-headlines?"
	ref_url = "country=in&category=sports&"
	api_key = "apiKey=e076e68a293b45398aa116162b827787"

	articles = url_concatinate(sub_url,ref_url,api_key)
	return render_template('sports_india.html',articles=articles)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contacts')
def contacts():
	return render_template('contacts.html')


@app.route('/blog')
def blog():
	return render_template('blog.html')



if __name__ == '__main__':
	app.run(debug = True)