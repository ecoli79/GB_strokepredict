from http.client import responses
import json
from urllib import response

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json
import dill
import pandas as pd
import flask

def load_model(model_path):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	print(model)

modelpath = "/app/app/models/randomforest_pipeline.dill"
load_model(modelpath)

class ClientDataForm(FlaskForm):
    hypertension = SelectField(u'Гипертония', choices=[('0', 'Нет'), ('1', 'Да')],validators=[DataRequired()])
    heart_disease = SelectField(u'Сердечные заболевания', choices=[('0', 'Нет'), ('1', 'Да')],validators=[DataRequired()])
    age = StringField('Возраст', validators=[DataRequired()])
    avg_glucose_level = StringField('Средний уровень глюкозы в крови', validators=[DataRequired()])
    bmi = StringField('Индекс массы тела', validators=[DataRequired()])
    gender = SelectField(u'Пол', choices=[('0', 'Женский'), ('1', 'Мужской')], validators=[DataRequired()])
    ever_married = SelectField(u'Семейное положение', choices=[('0', 'Женат/Замужем'), ('1', 'Не женат/Не замужем')], validators=[DataRequired()])
    work_type = SelectField(u'Характер работы', choices=[('0', 'Private'), ('1', 'Self-employed'), ('2', 'children'), ('3', 'Govt_job')], validators=[DataRequired()])
    Residence_type = SelectField(u'Место жительства', choices=[('0', 'Городской'), ('1', 'Сельский')], validators=[DataRequired()])
    smoking_status = SelectField(u'Курение', choices=[('0', 'Никогда не курил'), ('1', 'Затрудняюсь ответить'), ('2', 'Ранее курил'), ('3', 'Курю')], validators=[DataRequired()])
                                 


app = Flask(__name__)

app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    form = ClientDataForm()
    
    return render_template('form.html', form=form)
    
    
@app.route('/result', methods=['GET', 'POST'])
def result():
    
    data = dict()
    
    if request.method == 'POST':
      
        data = {}
    
        data["hypertension"] = request.form.get('hypertension')
        data["heart_disease"] = request.form.get('heart_disease')
        data["age"] = request.form.get('age')
        data["avg_glucose_level"] = request.form.get('avg_glucose_level')
        data["bmi"] = request.form.get('bmi')
        data["gender"] = request.form.get('gender')
        data["ever_married"] = request.form.get('ever_married')
        data["work_type"] = request.form.get('work_type')
        data["Residence_type"] = request.form.get('Residence_type')
        data["smoking_status"] = request.form.get('smoking_status')
        
        df = pd.DataFrame([data])
        
        preds = model.predict(df)

    return render_template('predicted.html', response=preds)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
