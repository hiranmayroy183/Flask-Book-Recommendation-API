# Book Recommendation API

## Endpoints

### **GET /recommend**

Fetch book recommendations based on average rating. Optionally filter by author.

**Query Parameters:**
- `author` (optional): Filter books by author name.
- `page` (optional): Page number for pagination (default is 1).
- `per_page` (optional): Number of items per page (default is 10).

**Responses:**

- **200 OK**
  - Returns a JSON object with:
    - `total`: Total number of items.
    - `page`: Current page number.
    - `per_page`: Number of items per page.
    - `data`: List of books.

- **500 Internal Server Error**
  - Returns an error message if something goes wrong.

**Examples:**

- Request: `GET /recommend?page=1&per_page=5`
- Response:
  ```json
  {
    "total": 100,
    "page": 1,
    "per_page": 5,
    "data": [
      {
        "bookID": 1,
        "title": "Harry Potter and the Half-Blood Prince",
        "authors": "J.K. Rowling",
        "average_rating": 4.57,
        "isbn": "0439785960",
        "isbn13": "9780439785969",
        "language_code": "eng",
        "num_pages": 652,
        "ratings_count": 2095690,
        "text_reviews_count": 27591,
        "publication_date": "9/16/2006",
        "publisher": "Scholastic Inc."
      },
      ...
    ]
  }
