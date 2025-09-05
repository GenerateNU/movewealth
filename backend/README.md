# Instructions For Setting Up Backend

1. Run ```cd backend```
2. Install Python 3
3. Run ```python3 -m venv venv```
4. Run ```source venv/bin/activate```
5. Run ```pip install -r requirements.txt```
6. ```Cmd + Shift + P``` > ```Python: Select Interpreter``` > ```Enter interpreter path...``` > ```./backend/venv/bin/python```
7. Make a ```.env``` file
8. Set the values for the variables ```MONGODB_URL``` and ```ACCESS_TOKEN_EXPIRE_MINUTES```
9. Run ```python run.py```
10. Install Postman
11. Make a new tab, and send a GET request to ```http://localhost:8080/health``` and ensure that the returned result is ```{
    "status": "ok",
    "message": "API is running"
}```