
# Book Recommendation API

## Overview

This project provides a RESTful API for recommending books based on user preferences. It uses Python with Flask for the API and Pandas for handling and processing the book data. The API includes features for retrieving recommendations, handling pagination, and querying by author.

## Features

- **Book Recommendations**: Fetch book recommendations based on ratings or author filters.
- **Pagination**: Retrieve results in pages to handle large datasets efficiently.
- **Caching**: Speed up responses using in-memory caching for frequently requested data.
- **Error Handling**: Graceful handling of invalid inputs and server errors.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pandas
- Flask
- Flask-Caching
- Flask-Testing (for testing)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/book-recommendation-api.git
    cd book-recommendation-api
    ```

2. **Set Up a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare Data Files**

    Ensure your CSV files `1.csv` and `2.csv` are located in the `data/` directory. These files should contain book data and be formatted according to the examples provided.

### Configuration

The API uses Flask-Caching for caching. By default, caching is enabled for production environments and disabled for testing.

To disable caching in a testing environment, ensure the `FLASK_ENV` environment variable is set to `test` before running tests:

```bash
export FLASK_ENV=test  # On Windows use `set FLASK_ENV=test`
```

### Running the Application

To run the application locally:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`.

### API Endpoints

#### Get Recommendations

- **URL**: `/recommend`
- **Method**: `GET`
- **Query Parameters**:
  - `author` (optional): Filter by author name.
  - `page` (optional, default=1): Page number for pagination.
  - `per_page` (optional, default=10): Number of results per page.

- **Responses**:
  - **200 OK**: Returns a JSON object with book recommendations.
  - **400 Bad Request**: Returns an error message for invalid parameters.
  - **500 Internal Server Error**: Returns an error message for unexpected issues.

**Example Request**:
```bash
curl "http://127.0.0.1:5000/recommend?page=1&per_page=5"
```

### Running Tests

To run the test suite, use:

```bash
python test.py
```

### Project Structure

- **app.py**: Main Flask application with API endpoints.
- **utils/data_loader.py**: Contains the `DataLoader` class for reading and processing CSV data.
- **test.py**: Contains unit tests for the API.
- **data/**: Directory for storing CSV data files.
- **requirements.txt**: List of required Python packages.

### Example CSV Data

**1.csv**:
```csv
bookID,title,authors,average_rating,isbn,isbn13,language_code,num_pages,ratings_count,text_reviews_count,publication_date,publisher
1,Harry Potter and the Half-Blood Prince,J.K. Rowling/Mary GrandPré,4.57,0439785960,9780439785969,eng,652,2095690,27591,9/16/2006,Scholastic Inc.
2,Harry Potter and the Order of the Phoenix,J.K. Rowling/Mary GrandPré,4.49,0439358078,9780439358071,eng,870,2153167,29221,9/1/2004,Scholastic Inc.
```

**2.csv**:
```csv
bookId,title,author,series,description,genres,awards,characters,places,isbn,isbn13,language,first_publish_date,publish_date,num_pages,num_ratings,num_reviews,avg_rating,rated_1,rated_2,rated_3,rated_4,rated_5
1,Harry Potter and the Half-Blood Prince,J.K. Rowling,Harry Potter #6,"Description",Genres,Awards,Characters,Places,0439785960,9780439785969,English,July 16th 2005,September 16th 2006,652,2553909,41470,4.57,13147,29020,174312,608825,1728605
2,Harry Potter and the Order of the Phoenix,J.K. Rowling,Mary GrandPré,Harry Potter #5,"Description",Genres,Awards,Characters,Places,0439358078,9780439358071,English,June 21st 2003,September 2004,870,2631427,44793,4.5,16236,41738,231438,665628,1676387
```

### Troubleshooting

- **Invalid Parameters**: Ensure that `page` and `per_page` parameters are positive integers.
- **Caching Issues**: If encountering errors related to caching during tests, ensure caching is disabled in the test environment.

### Contributing

Feel free to fork the repository and submit pull requests. Please ensure your contributions adhere to the existing code style and include appropriate tests.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` provides a comprehensive guide to setting up, running, and testing the Book Recommendation API. Let me know if you need any additional information or modifications!
