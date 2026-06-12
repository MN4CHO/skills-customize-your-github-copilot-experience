# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, scalable REST APIs using the FastAPI framework. You will create an API for managing a collection of books, implementing proper routing, validation, and data persistence.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI and Create Basic Endpoints

#### Description
Create a new FastAPI application with GET and POST endpoints for managing a book collection. Start with in-memory storage to focus on learning the framework basics.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create a GET endpoint (`/books`) that returns a list of books
- Create a POST endpoint (`/books`) that adds a new book to the collection
- Store books in a simple Python list during runtime
- Return appropriate HTTP status codes (200 for success, 201 for created)

---

### 🛠️ Task 2: Add Data Validation with Pydantic Models

#### Description
Enhance your API with Pydantic models to validate incoming data and ensure API responses follow a consistent structure. This prevents bad data from being saved and documents your API's contract.

#### Requirements
Completed program should:

- Define a Pydantic model for a Book with fields: `id`, `title`, `author`, `year`, `isbn`
- Use the model for request/response validation
- Return a 400 error if required fields are missing or invalid
- Automatically generate OpenAPI documentation that reflects your models
- Test your endpoints using FastAPI's interactive Swagger UI (`/docs`)

---

### 🛠️ Task 3: Implement CRUD Operations and Path Parameters

#### Description
Build a complete CRUD (Create, Read, Update, Delete) API with individual resource endpoints using path parameters. Students will learn how to design RESTful APIs following best practices.

#### Requirements
Completed program should:

- Add a GET endpoint (`/books/{book_id}`) to retrieve a single book by ID
- Add a PUT endpoint (`/books/{book_id}`) to update a book's information
- Add a DELETE endpoint (`/books/{book_id}`) to remove a book
- Return a 404 error when a book ID is not found
- Maintain data consistency across all operations
- Handle edge cases (duplicate IDs, invalid updates)

---

### 🛠️ Task 4: Add Error Handling and Testing (Stretch Goal)

#### Description
Make your API production-ready by adding comprehensive error handling and writing unit tests. This task teaches defensive programming and quality assurance practices.

#### Requirements
Completed program should:

- Define custom exception handlers for common errors (404, 400, 500)
- Add logging to track API requests and errors
- Write at least 5 unit tests using pytest to verify endpoint behavior
- Test both success and error cases
- Achieve at least 80% code coverage on core functions
- Document how to run tests with clear instructions
