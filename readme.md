# HTTP Health Monitor
Author: Logan Cornforth

## Overview

This Python script monitors the health of HTTP endpoints specified in a YAML file. It performs periodic requests to the provided endpoints, logs the results, and displays the availability percentage for each domain.

## Features

- Reads HTTP endpoints from a YAML file.
- Performs periodic health checks on the specified endpoints.
- Logs and displays the availability percentage for each domain.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `yaml`

## Usage

1. **Install Dependencies:**
   In your OS command line type:
  ```
   pip install requests pyyaml
   ```

2. **Run the Script:**
  In your OS command line navigate to the folder containing the program and type:
   ```
   python health_monitor.py
   ```
   Follow the on-screen instructions to input the file path containing the list of HTTP endpoints in YAML format.

3. **Stop the Monitoring:**
   Press `ctrl + c` to stop the monitoring process.

## Configuration

- Endpoint details are specified in a YAML file.
- Customize the file path and contents according to your monitoring requirements.

## File Format Example (YAML)

```
- url: https://example.com
  name: Example Endpoint 1
  method: GET
  headers:
    Authorization: "Bearer token123"
  body: {}

- url: https://api.example.org/data
  name: Example Endpoint 2
  method: POST
  headers:
    Content-Type: application/json
  body:
    key1: value1
    key2: value2
```

## Notes

- Ensure the YAML file is correctly formatted.
- The script runs indefinitely, displaying availability percentages every 15 seconds.

---
