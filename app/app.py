import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
print(f"Loaded GEOAPIFY_API_KEY: {GEOAPIFY_API_KEY}")

@app.route('/')
def home():
    return 'Welcome to MediFinder! Use /find-hospitals?lat=...&lon=...'

@app.route('/find-hospitals')
def find_hospitals():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Please provide both 'lat' and 'lon' in the query"}), 400

    url = (
        f"https://api.geoapify.com/v2/places?"
        f"categories=healthcare.hospital&"
        f"filter=circle:{lon},{lat},5000&"
        f"limit=10&apiKey={GEOAPIFY_API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
