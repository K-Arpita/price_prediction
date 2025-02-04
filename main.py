import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect,url_for
import pickle




app= Flask(__name__, static_folder='static')
data=pd.read_csv("Pune_rent.csv")
model=pickle.load(open('model.pkl','rb'))


@app.route("/", methods=["GET", "POST"])
def index():
    
    locations = sorted(data['location'].unique())

    return render_template('house_form.html',locations=locations,)


def predict_price_house(location, bedroom, area, bathroom, property_type, furnish):
    try:
        if 'BHK' in bedroom:
            bedroom = int(bedroom.replace('BHK', '').strip())  
        else:
            bedroom = int(bedroom) if bedroom else 1 
        area = int(area) if area else 0
        bathroom = int(bathroom) if bathroom else 0

        features = pd.DataFrame([[location, bedroom, area, bathroom, property_type, furnish]],
                                columns=['location','bedroom','area','bathroom','property_type','furnish'])
     
        predicted_price = model.predict(features)[0]
        return round(predicted_price, 2)
    except Exception as e:
        print("Error:", e)
        return "unable to predicted Price for this"

@app.route('/price',methods=['POST'])
def predict_price():
    location = request.form.get('location')
    bedroom = request.form.get('bedroom')
    area = request.form.get('area')
    bathroom = request.form.get('bathroom')
    property_type = request.form.get('property_type')
    furnish = request.form.get('furnish')

  
    predicted_price = predict_price_house(location,bedroom,area,bathroom,property_type,furnish)

    return render_template('predict_price.html',price=predicted_price,location=location, bedroom=bedroom, 
                           area=area, bathroom=bathroom, property_type=property_type, furnish=furnish) 

@app.route('/result')
def result():

    return "<h1>f'Predicted  House Price: ₹{predicted_price}'</h1>"
if __name__=="__main__":
    app.run(debug=True)   
 