"""
FastAPI REST API Starter Code
Complete this assignment by implementing the required endpoints and features.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="Books API", version="1.0.0")

# ============================================================================
# TODO: Define your Pydantic models here
# You'll need a Book model with fields: id, title, author, year, isbn
# ============================================================================


# ============================================================================
# In-memory storage for books (Task 1)
# ============================================================================
books_db: List[dict] = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "isbn": "978-0132350884"
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "David Thomas, Andrew Hunt",
        "year": 1999,
        "isbn": "978-0135957059"
    }
]


# ============================================================================
# TODO: Implement Task 1 - Basic Endpoints
# ============================================================================
# 1. GET /books - return all books
# 2. POST /books - create a new book


# ============================================================================
# TODO: Implement Task 3 - CRUD Operations
# ============================================================================
# 1. GET /books/{book_id} - get a specific book
# 2. PUT /books/{book_id} - update a book
# 3. DELETE /books/{book_id} - delete a book


# ============================================================================
# Health Check Endpoint (provided as example)
# ============================================================================
@app.get("/health")
def health_check():
    """Simple health check endpoint to verify the API is running."""
    return {"status": "healthy", "message": "API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
