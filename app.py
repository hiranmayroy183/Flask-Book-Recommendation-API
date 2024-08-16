import os
from flask import Flask, request, jsonify, render_template_string
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
data_loader = DataLoader('data/1.csv', 'data/2.csv')

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Documentation</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            pre { background: #f4f4f4; padding: 10px; border: 1px solid #ddd; }
            code { color: #d14; }
        </style>
    </head>
    <body>
        <h1>API Documentation</h1>
        <p>Welcome to the API documentation. Here you will find information about all available endpoints.</p>
        
        <h2>/recommend</h2>
        <p><strong>Method:</strong> GET</p>
        <p><strong>Query Parameters:</strong></p>
        <ul>
            <li><code>author</code> (optional): The author for whom recommendations are to be fetched.</li>
            <li><code>page</code> (optional, default=1): The page number of the results to fetch.</li>
            <li><code>per_page</code> (optional, default=10): The number of results per page.</li>
        </ul>
        <p><strong>Response:</strong></p>
        <pre><code>{
    "total": 100,
    "page": 1,
    "per_page": 10,
    "data": [
        {"id": 1, "title": "Book Title 1", "author": "Author Name"},
        {"id": 2, "title": "Book Title 2", "author": "Author Name"},
        ...
    ]
}</code></pre>
        
        <p><strong>Errors:</strong></p>
        <pre><code>{
    "error": "Invalid page or per_page parameter"
}</code></pre>
        
        <p>If you have any questions, feel free to contact support.</p>
    </body>
    </html>
    '''
    return render_template_string(html_content)

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
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
