# Water Scarcity Prediction 

The Water Scarcity Prediction is a application that predicts the likelihood of a drought based on user-provided parameters.
This README provides detailed instructions for setting up and using the application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
1. Build & Train Model using Auto AI.
   Use LGBM Classifier Algorithm.
   https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp

2. **Install Python:**

   If Python is not already installed on your system, you can download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/). 

3. **Clone the Repository:**

   Start by cloning the repository to your local machine using Git:

   ```bash
   git clone 
   cd LandslidePredictionSystem
   
4. **Install Dependencies:**
   Install the required Python packages listed in the requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Application**

   Start the Flask application using the following command:
   ```
   python -m flask run
   ```
   This will start the application, and you can send you POST requests at http://localhost:5000/scarcity.

2. The result will return the predicted water scarcity. 


    
   

