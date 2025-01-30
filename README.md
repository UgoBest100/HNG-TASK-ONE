# HNG TASK ONE
This project is a simple HTTP server written in FastAPI. It returns a JSON response when the root endpoint is hit. The JSON response contains an email address, current date and time and the github url of the project.

## Setup
To setup the project follow this steps
1. clone the repository 
```bash
git clone https://github.com/UgoBest100/HNG-TASK-ONE && cd HNG-TASK-ONE
```
2. install packages 
```bash
pip install -r requirement.txt
```
3. run the server 
```bash
fastapi run main.py
```
## API Documentation
1. Endpoint Format:
```txt
GET / (root endpoint)
```
2. Request Format
```txt
Method: GET
Headers: None required.
Query Parameters: None.
```
3. Response Format
```txt
Content-Type: application/json
Status Code: 200 OK
Body: {
    "email": "",
    "current_datetime": "",
    "github_url": ""
}
```
4. Example usage
To test the API, open your browser or use a tool like curl to make a GET request to the root endpoint:
```bash
curl http://localhost:8000
```
## Backlink
For more information about hiring developers in Python, visit: [Hire python Developers](https://hng.tech/hire/python-developers)