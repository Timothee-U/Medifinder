from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("GEOAPIFY_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    lat = data['lat']
    lon = data['lon']
    category = data['category']
    
    url = f"https://api.geoapify.com/v2/places?categories={category}&filter=circle:{lon},{lat},10000&bias=proximity:{lon},{lat}&limit=10&apiKey={API_KEY}"
    response = requests.get(url)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
