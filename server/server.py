from flask import Flask,jsonify
from friday import call_lift,goto_lift,thank_you,check_for_mask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'hello'

@app.route('/call_the_lift')
def call_the_lift():
    response = jsonify({
        'floor_number_gen' : str(call_lift())
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/go_to_lift')
def go_to_lift():
    responsenew = jsonify({
        'floornew' : str(goto_lift())
    })
    responsenew.headers.add('Access-Control-Allow-Origin','*')
    return responsenew

@app.route('/thank')
def thank():
    thank_you()
    return None

@app.route('/check_mask')
def check_mask():
    responsemask = jsonify({
        'mask_ans' : check_for_mask()
    })
    responsemask.headers.add('Access-Control-Allow-Origin','*')
    return responsemask

if __name__ == "__main__":
    app.run(debug=False)
