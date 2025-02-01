from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app=application

# Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else: 
        data=CustomData(
            type=request.form.get('type'),
            air_temperature_k = request.form.get('air_temperature_k'),
            process_temperature_k = request.form.get('process_temperature_k'),
            rotational_speed_rpm = request.form.get('rotational_speed_rpm'),
            torque_nm = request.form.get('torque_nm'),
            tool_wear_min = request.form.get('tool_wear_min'),
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")


        predict_pipeline=PredictPipeline()
        print("Mid Prediction")

        results=predict_pipeline.predict(pred_df)
        print("after Prediction")

        return render_template('home.html', results=results[0])
    
if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000)

