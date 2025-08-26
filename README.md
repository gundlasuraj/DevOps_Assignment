# ACEest Fitness Tracker

A simple desktop application for logging workouts, built with Python and Tkinter. This project is configured with a full suite of automated testing, and a CI/CD pipeline using Docker and GitHub Actions.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Git
- Docker

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Dev

2.  **Install dependencies:**
    This project uses `pip` for package management. The required packages are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Running the Application

To run the fitness tracker application directly on your machine:
```bash
python ACEest_Fitness.py
```

### Local Testing

To run the entire `pytest` suite manually:
```bash
pytest
```

### Automated Local Checks (pre-commit)

The repository is configured with `pre-commit` hooks to automatically format code, check for issues, and run tests before each commit. To enable these hooks, run this command once after cloning:
```bash
pre-commit install
```

## 🐳 Containerization

This project includes a `Dockerfile` to create a portable and consistent environment for the application.

### Building the Docker Image

To build the image locally, run the following command from the project root:
```bash
docker build . -t my-app
```

### To test the Application functionality within the built Docker image

To run the application inside a Docker container and test its functionality, run the following command.
```bash
docker run --rm my-app pytest
```

## 🔄 CI/CD Pipeline

This repository is configured with a fully automated CI/CD pipeline using GitHub Actions that validates every change.

1.  **Trigger**: The pipeline runs on every `push` or `pull_request` to the `main` branch.
2.  **Build**: A Docker image is built from the `Dockerfile`, packaging the application and all its dependencies.
3.  **Test**: The `pytest` suite is executed *inside* the newly built Docker container to verify the application's functionality.

This process ensures that all code merged into the main branch is automatically built, tested, and Containerized.
