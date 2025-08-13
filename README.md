# Automation Tool

A comprehensive test automation framework built with Behave (Python) for both API and UI testing. This tool provides a robust foundation for automated testing with support for Selenium WebDriver, API testing, and Kubernetes deployment.

## Features
- **API Testing**: RESTful API testing with JSON schema validation
- **BDD Framework**: Behavior-Driven Development using Behave
- **Docker Support**: Containerized execution environment
- **Kubernetes Integration**: CronJob deployment for scheduled test execution
- **Configuration Management**: YAML-based configuration system
- **Retry Logic**

## Prerequisites

- Docker
- Kubernetes cluster (optional, for scheduled execution)

## Installation

### Local Development Setup

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv
   uv sync
   ```

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t automation-tool .
   ```

2. **Run tests in container (windows)**
   ```bash
   docker run --rm -v "%cd%\reports:/reports" sdaia-test
   ```

## Usage

### Running Tests

#### All Tests
```bash
behave
```

### Configuration

The tool uses YAML configuration files located in `configs/`:

```yaml
api:
  base_url: "https://dummyjson.com"
timeouts:
  default: 15
```

## Project Structure

```
automation_tool/
├── configs/                 # Configuration files
│   └── config.yaml         # Main configuration
├── features/               # BDD feature files
│   ├── api/               # API test features
│   │   ├── auth.feature
│   │   └── protected.feature
│   ├── ui/                # UI test features
│   │   └── search.feature
│   ├── steps/             # Step definitions
│   │   ├── api_steps.py
│   │   └── ui_steps.py
│   └── environment.py     # Behave hooks and setup
├── src/                   # Source code
│   ├── api/              # API testing utilities
│   │   ├── client.py     # HTTP client
│   │   ├── schemas.py    # JSON schemas
│   │   ├── schema_validator.py
│   │   └── token.py      # Authentication
│   └── utils/            # Utility modules
│       ├── config.py     # Configuration loader
├── reports/              # Test reports and artifacts
│   ├── junit/           # JUnit XML reports
├── k8s/                 # Kubernetes manifests
│   ├── cronjob.yaml     # Scheduled test execution
│   └── debug.yaml       # Debug deployment
├── Dockerfile           # Container definition
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project metadata
└── behave.ini          # Behave configuration
```

## Test Examples

### API Testing

```gherkin
Feature: Authentication

Scenario: Successful login
  Given I have valid credentials
  When I login
  Then I receive an access token

Scenario: Failed login
  Given I have invalid credentials
  When I login
  Then I see an authentication error
```

## Kubernetes

### Kubernetes Deployment
1. **Setup**
   ```bash
   minikube start
   minikube image load automation-tool:latest
   ```

1. **Apply CronJob for scheduled execution**
   ```bash
   kubectl apply -f k8s/cronjob.yaml
   ```

2. **Check job status**
   ```bash
   kubectl get cronjobs
   kubectl get jobs
   kubectl logs job/<job-name>
   ```

## Reporting

### Test Results
Detailed test results are saved to `reports/junit/`.
