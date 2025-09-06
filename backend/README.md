# Instructions For Setting Up Backend

1. Install Python 3 at the root level of your laptop
2. Run ```cd backend```
3. Run ```python3 -m venv venv```
4. Run ```source venv/bin/activate```
5. Run ```pip install -r requirements.txt```
6. ```Cmd + Shift + P``` > ```Python: Select Interpreter``` > ```Enter interpreter path...``` > ```./backend/venv/bin/python```
7. Make an ```.env``` file
8. Set the values for the variables ```MONGODB_URL``` (should be the connection string with <db_password> replaced by the password that Sierra will give you) and ```ACCESS_TOKEN_EXPIRE_MINUTES``` (300 is fine for now)
9. Run ```python run.py```
10. Install Postman
11. Make a new tab, and send a GET request to ```http://localhost:8080/health``` and ensure that the returned result is ```{ "status": "ok", "message": "API is running" }```
12. Make a MongoDB account and get Sierra to add you to the list of users by providing you an email
13. Run ```pre-commit install```

# Software Bootcamp Onboarding

1. Checkout the API endpoints in the ```persons``` controller using Postman
2. Hit the ```/new``` endpoint to add yourself to the DB!
3. Sign into your MongoDB account in the browser and verify that your name appears in the collection!
4. Get MongoDB VSCode extension
5. Make a new branch using git and make a new endpoint to fetch yourself