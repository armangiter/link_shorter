# Django Link Shortener

## Overview
This is a simple Django-based link shortener that allows users to create, manage, and use short links.

## Prerequisites
- Ensure you have Docker installed on your system.
- Create an `.env` file from the sample provided in `.envs/samples` before running the project.

## Getting Started
### Running the Project with Docker
To start the project using Docker, run the following command:
```sh
docker compose up -d
```
This will spin up the necessary containers in detached mode.

## API Documentation
Once the project is running, you can access the API documentation at:
- `api/docs/` (for a browsable API interface)
- `api/schema/` (for schema documentation)

## API Endpoints
After running the project, you can interact with the API using the following endpoint:

### Link Management
**Base URL:** `http://0.0.0.0:8090/links`

#### Supported Methods:
- `POST`: Create a new short link.
- `GET`: Retrieve a list of all short links.
- `PATCH`: Update an existing short link.
- `PUT`: Replace an existing short link.
- `DELETE`: Remove a short link.

### Using the Shortened Link
Once a short link is created, you can use it by making a request to the main domain of the application:
```
http://0.0.0.0:8090/{shorted-link}
```
This will redirect to the original URL.

## Notes
- Ensure the `.env` file is correctly configured before starting the project.
- The application runs on ports `8090` (for API interactions) and `8089` (for using short links).

## License
This project is open-source. Feel free to contribute and improve!
