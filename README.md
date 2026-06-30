# Python Base Shaip Code
Base code that can be pulled and used to develop a Python API using a Docker container.

## Architecture Overview

This application is designed as a lightweight, high-performance execution layer. It follows a clean separation of concerns by decoupling the HTTP transport layer from the actual business logic.

### 1. Separation of Concerns & Task Delegation
- **Entry Point (`app/main.py`)**: This file serves strictly as the routing and transport layer. It intercepts the HTTP requests, extracts the payload, and delegates the processing execution to dedicated, discrete functions.
- **Business Logic (`app/services/`)**: Core application operations and heavy processing tasks live in this isolated directory (e.g., `app/services/math_operations.py`). This allows developers to modify or scale business rules without touching the web framework configuration.

### 3. Managing Dependencies
As you scale this application and introduce new packages (e.g., database drivers, HTTP clients, or utility libraries):
1. Install them in your active local virtual environment (e.g., `pip install <package-name>`).
2. **Crucial:** You must append these packages to the `requirements.txt` file in the root directory. The `Dockerfile` uses this file to build the production image; if a dependency is missing from `requirements.txt`, the build or execution on Google Cloud Run will fail.

---

### 2. Pre-Validated Data Pipeline
This API does not perform heavy structural input validation on incoming request bodies. Strict schema validation and sanitization are handled by upstream gateway/middleware infrastructure before requests ever route to this application.

---

## API Contract

### Execute Addition

* **Endpoint:** `/shaip`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`

#### Request Body (JSON)
The endpoint expects a flat JSON object with the numerical inputs `a` and `b`:
```json
{
  "a": 12.5,
  "b": 7.5
}
```

#### Response (JSON)
```json
{
  "a": 12.5,
  "b": 7.5,
  "result": 20.0
}
```
