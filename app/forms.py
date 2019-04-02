from flask_wtf import Form 
from wtforms import TextField , validators

class CityTemperatureForm(Form):
	name = TextField("CityName",validators=[validators.required()])
