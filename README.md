<p align="center">
  <img src="https://raw.githubusercontent.com/ESTETIKA-2023/.github/main/profile/src/estetika-header-image.png" width="100%" height="auto" alt="ESTETIKA Header">
</p>

# ESTETIKA-API

Welcome to the `ESTETIKA-API` branch! This branch focuses on the development of the ESTETIKA platform's backend API using Python with the FAST API framework.

## Introduction

The `ESTETIKA-API` branch is dedicated to handling server-side logic, managing database interactions, and providing the API endpoints required for the ESTETIKA platform. This API serves as a crucial component for data communication between the frontend and backend of the application.

## Getting Started

To use the ESTETIKA API locally, follow these steps:

1. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the necessary packages for the ESTETIKA API.

3. There is a use of an environment file in this project, if you want to try it, you can contact us directly.

4. Run the API using `uvicorn`:

    ```bash
    uvicorn app.main:app --reload
    ```

    This command assumes that the main application is located in a file named `main.py` within a directory named `app`. Adjust the command if your file or directory structure is different.

5. Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the API documentation using Swagger UI. Here, you can explore and interact with the available API endpoints.

## Contact Us

If you encounter any issues, have questions, or need additional information, feel free to reach out to us.
