# MediFinder

MediFinder is a simple Flask web application that allows users to search for hospitals and pharmacies near a specified city. It uses the Geoapify API for geocoding city names and fetching places of interest.

---

## Features

- Search by **city name** for hospitals or pharmacies.
- Displays search results with names and addresses.
- Responsive, modern frontend with loading spinner and error messages.
- Simple backend built with Flask and Python.

---

## Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.
- Git installed to clone the repository.
- A Geoapify API key (free tier available) — sign up at [https://www.geoapify.com]

---

### Step 1: Clone the repository

Open PowerShell (or your terminal) and run:

```powershell
git clone https://github.com/yourusername/medifinder.git
cd medifinder

##Create a virtual environment by running 

python -m venv venv

##Activate the virtual environment:

-On Windows PowerShell:
.\venv\Scripts\Activate.ps1

-On Windows CMD:
venv\Scripts\activate.bat

-On macOS/Linux:
source venv/bin/activate

##Install required Python packages:

pip install flask requests python-dotenv


##Create a file named .env in the project root with your Geoapify API key:

GEOAPIFY_API_KEY= your_actual_geoapify_api_key_here

##Start the Flask app by running:

python app/app.py


###Open your browser and navigate to http://localhost:8080.

Enter any city name (e.g., Kigali, London, etc).

Choose either "Hospital" or "Pharmacy".

Click Search.

View the results below the form with a loading spinner while fetching.

medifinder/
├── app.py               # Flask backend application
├── .env                 # Environment variables (API key)
├── requirements.txt     # (Optional) Python dependencies list
├── templates/
│   └── index.html       # Frontend HTML template
└── static/
    ├── style.css        # Styling for frontend
    └── script.js        # JavaScript for frontend logic

NB: any additional file is to be disregarded as it was a result of tests.

##How it works
The frontend sends a POST request with city and category to /search.

The backend uses Geoapify Geocoding API to convert the city name to coordinates.

Then it queries Geoapify Places API for hospitals or pharmacies near those coordinates.

Results are returned as JSON to the frontend, which dynamically renders them.

The frontend shows a loading spinner during the search and displays errors or no-results messages gracefully.

###APIs Used
Geoapify Geocoding API: Convert city names into latitude/longitude.

Docs: https://apidocs.geoapify.com/docs/geocoding/

Geoapify Places API: Search for places by category near coordinates.

Docs: https://apidocs.geoapify.com/docs/places/


###Challenges and How They Were Overcome
Search by coordinates → Search by city name: Initially, the app required latitude and longitude inputs, which was not user-friendly. We integrated geocoding to let users simply input city names.

Loading and feedback: Added a loading spinner during API requests to improve user experience.

Error handling: Implemented clear error and no-results messages for smoother interaction.