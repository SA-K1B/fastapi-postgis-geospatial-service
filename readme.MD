# Project Title

## Description
This project is a FastAPI application that manages ambulance data. It provides endpoints for creating ambulances and finding nearby ambulances based on geographical coordinates.

## Installation
To set up the project locally, follow these steps:
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment variables in a `.env` file, including the `DATABASE_URL`.

## Usage
### API Endpoints
- **Create Ambulance**
  - **Endpoint**: `POST /ambulances/`
  - **Request Body**:
    ```json
    {
      "name": "Ambulance Name",
      "location": [latitude, longitude]
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Ambulance Name",
      "location": [latitude, longitude]
    }
    ```

- **Find Nearby Ambulances**
  - **Endpoint**: `GET /ambulances/nearby/`
  - **Query Parameters**: `lat`, `lon`, `radius`
  - **Response**:
    ```json
    ["Ambulance 1", "Ambulance 2"]
    ```

## Database Configuration
The database is configured using a URL from environment settings. Ensure that the `DATABASE_URL` is set correctly in your `.env` file.

## License
This project is licensed under the MIT License.
