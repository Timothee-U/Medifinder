import os
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    city = data.get('city')
    category = data.get('category')

    if not city or not category:
        return jsonify({"error": "Please provide city and category"}), 400

    # Geocode city name to lat/lon
    geocode_url = (
        f"https://api.geoapify.com/v1/geocode/search?"
        f"text={city}&limit=1&apiKey={GEOAPIFY_API_KEY}"
    )

    try:
        geocode_resp = requests.get(geocode_url)
        geocode_resp.raise_for_status()
        geocode_data = geocode_resp.json()
        if not geocode_data['features']:
            return jsonify({"error": "City not found"}), 404

        lon, lat = geocode_data['features'][0]['geometry']['coordinates']

        # Search places near the city coordinates
        places_url = (
            f"https://api.geoapify.com/v2/places?"
            f"categories={category}&"
            f"filter=circle:{lon},{lat},5000&"
            f"limit=10&apiKey={GEOAPIFY_API_KEY}"
        )

        places_resp = requests.get(places_url)
        places_resp.raise_for_status()
        return jsonify(places_resp.json())

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)