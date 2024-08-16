import os
from flask import Flask, request, jsonify
from flask_caching import Cache
from utils.data_loader import DataLoader

app = Flask(__name__)

# Conditional caching setup based on environment
if os.getenv('FLASK_ENV') == 'test':
    app.config['CACHE_TYPE'] = 'null'  # Disable caching during tests
else:
    app.config['CACHE_TYPE'] = 'simple'  # Simple in-memory caching

cache = Cache(app)

# Initialize the DataLoader with paths to your CSV files
# Adjust these paths if needed for deployment
data_loader = DataLoader('data/1.csv', 'data/2.csv')

@app.route('/recommend', methods=['GET'])
@cache.cached(timeout=60, query_string=True)  # Cache responses for 60 seconds
def recommend():
    author = request.args.get('author')
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        if page < 1 or per_page < 1:
            raise ValueError("Page and per_page must be positive integers.")
    except ValueError:
        return jsonify({'error': 'Invalid page or per_page parameter'}), 400

    try:
        recommendations = data_loader.get_recommendations(author)
        total = len(recommendations)
        start = (page - 1) * per_page
        end = start + per_page

        recommendations_paginated = recommendations[start:end]
        response = {
            'total': total,
            'page': page,
            'per_page': per_page,
            'data': recommendations_paginated.to_dict(orient='records')
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Set host and port for deployment
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
