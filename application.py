from flask import Flask,jsonify, request
from flask import render_template, send_file
import numpy as np


app = Flask(__name__,template_folder='PageFiles')


@app.route("/get")
def generate_graph_data():
    data_arr = np.random.randn(20)*100
    app.logger.info(data_arr)
    return jsonify(data=data_arr)

@app.route("/meters",methods=['POST','GET'])
def meters():
    meters = {}
    for i in range(288):
        meters[i] = [i,"resiential",123,"https://freesvg.org/img/uno-r3.png"]

    meters_compressed = jsonify(meters)
    return render_template("meterview.html",meter_data = meters,max_bound = len(meters.keys()))

@app.route("/home",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/marketplace",methods = ['POST','GET'])
def marketplace():
    return render_template('marketplace.html')

@app.route("/regulation",methods=['POST','GET'])
def regulation():
    return render_template('regulation.html')

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/styles")
def styles():
    return send_file("PageFiles/styles.css")

@app.route("/get_image")
def get_image():
    return send_file("PageFiles/images/Figure_" + request.args.get('id') + ".png")