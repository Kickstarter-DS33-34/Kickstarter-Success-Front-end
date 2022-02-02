from flask import Flask, render_template, request
from os import getenv
import kickstarter.functions as f
import kickstarter.query_functions as qf
from kickstarter.model import MODEL


def create_app():
    
    app = Flask(__name__)
    
    @app.route("/", methods=['POST', 'GET'])
    @app.route("/index.html", methods=['POST', 'GET'])
    def root():
        return render_template('index.html', title='tst title')
    

    @app.route("/prediction.html", methods=['POST', 'GET'])
    def prediction():
        return render_template('prediction.html', title='prediction')
    
    
    @app.route('/data', methods = ['POST', 'GET'])
    def data():
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/prediction.html' to submit form"
        if request.method == 'POST':
            try:
                form_data = request.form
                # Dataframe of form data to be used in prediction.
                # Outputs a single row dataframe sample
                transformed_data = f.transform(form_data)
                # In the future, prediction and chance
                # will be calculated from the model.
                # These are assigned in order to test the 
                # database functionality.
                prediction = MODEL.predict(transformed_data)
                chance = prediction[0][0]
                qf.insert_table(form_data, chance)
                return render_template('data.html', form_data=form_data, chance=chance)
            except:
                return f'Please be sure you are correctly formatting your inputs.'

    return app
