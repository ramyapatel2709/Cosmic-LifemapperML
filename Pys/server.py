from flask import Flask, request, jsonify
from flask_cors import CORS
from apSameer1 import get_all_planets, get_planet_details

app = Flask(__name__)
CORS(app)

@app.route('/api/planets', methods=['GET'])
def list_planets():
    return jsonify(sorted(get_all_planets()))

@app.route('/api/exoplanet', methods=['POST'])
def fetch_exoplanet_data():
    planet_name = request.json.get('planet_name')
    if not planet_name:
        return jsonify({"error": "No planet name provided"}), 400
    try:
        result = get_planet_details(planet_name)
        return jsonify({"report": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
