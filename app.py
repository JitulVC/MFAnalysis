from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus

from controller.mfperformance import MFPerformanceController

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
 

@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')

@app.route('/mfanalysis', methods=['GET'])
def mfanalysis():
    mfPerformanceController = MFPerformanceController()
    qdata = {'crisilrankf' : 0, 
            'crisilrankt' : 0,
            'ytdreturnf' : 0,
            'ytdreturnt' : 0,
            'oneyreturnf' : 0,
            'oneyreturnt' : 0,
            'twoyreturnf' : 0,
            'twoyreturnt' : 0,
            'threeyreturnf' : 0,
            'threeyreturnt' : 0,
            'fiveyreturnf' : 0,
            'fiveyreturnt' : 0
        }

    return mfPerformanceController.mfperformance(qdata)
             
@app.route('/mfanalysis', methods=['POST'])
def mfanalysisqry():
    mfPerformanceController = MFPerformanceController()
    crisilrankf = float(request.form.get("crisilrankf"))
    crisilrankt = float(request.form.get("crisilrankt"))
    ytdreturnf = float(request.form.get("ytdreturnf"))
    ytdreturnt = float(request.form.get("ytdreturnt"))
    oneyreturnf = float(request.form.get("oneyreturnf"))
    oneyreturnt = float(request.form.get("oneyreturnt"))
    twoyreturnf = float(request.form.get("twoyreturnf"))
    twoyreturnt = float(request.form.get("twoyreturnt"))
    threeyreturnf = float(request.form.get("threeyreturnf"))
    threeyreturnt = float(request.form.get("threeyreturnt"))
    fiveyreturnf = float(request.form.get("fiveyreturnf"))
    fiveyreturnt = float(request.form.get("fiveyreturnt"))
    qdata = {'crisilrankf' : crisilrankf, 
                'crisilrankt' : crisilrankt,
                'ytdreturnf' : ytdreturnf,
                'ytdreturnt' : ytdreturnt,
                'oneyreturnf' : oneyreturnf,
                'oneyreturnt' : oneyreturnt,
                'twoyreturnf' : twoyreturnf,
                'twoyreturnt' : twoyreturnt,
                'threeyreturnf' : threeyreturnf,
                'threeyreturnt' : threeyreturnt,
                'fiveyreturnf' : fiveyreturnf,
                'fiveyreturnt' : fiveyreturnt
            }

    return mfPerformanceController.mfperformance(qdata)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

