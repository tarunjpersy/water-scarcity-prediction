from flask import Flask,request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)

import requests
import json
@app.route('/')
@cross_origin()
def water_scarcity():
    return 'Water Scarcity Detection!'

@app.route('/scarcity', methods=["POST"])
@cross_origin()
def add_data():
    ddata = request.get_json()
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "MUcO9IxfJfYA6FQ_PjhOqYCUMqWZxRf_00PZFAc3Huh1"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    data = json.dumps(ddata[0])
    print(data[0])
    details = json.loads(data)
    print(details)
# NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ["Year","State",
                                "Population",
                                "Annual_average_Rainfall",
                                "Per_Capita_Water_Availability",
                                "No_of_reservoirs_monitered",
                                "Live_capacity",
                                "Current_year",
                                "Last_year",
                                "Last_10_ Avg",
                                "Current_year_percentage",
                                "Last_year_percentage",
                                "Last_10_avg",
                                "percent_departure_from_10_avg",
                                "Annual_Ground_Water_Recharge",
                                "Total_Natural_Discharges",
                                "Current_Annual_Groun_Water_Extraction",
                                "Stage_of_Ground_Water_Extraction_percent",
                                "Net_Ground_Water_Availability_for_future_use"], "values": [[details['year'],details['state'],details['pop'],details['aar'],details['pcwa'],details['norm'],details['lc'],details['cy'],details['ly'],details['liy'],details['cyp'],details['lyp'],details['lia'],details['pdfa'],details['agwr'],details['tnd'],details['cagw'],details['sogw'],details['ngwa']]]}]}

    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/7b96539d-df96-4bb5-bfe3-128bc7cad9ce/predictions?version=2021-05-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    return response_scoring.json()

if __name__ == '__main__':
    app.run(debug=True)



