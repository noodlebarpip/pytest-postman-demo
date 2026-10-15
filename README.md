# RUNNING THE CODE

**1. Clone and create a project**
```
git clone https://github.com/noodlebarpip/pytest-postman-demo.git
cd pytest-postman-demo
```

**2. Create a virtual environment**
For Windows:
```
py -m venv .venv
.venv\Scripts\Activate.ps1
```

For MacOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```
python -m pip install --upgrade pip
python -m pip install fastapi "uvicorn[standard]" pydantic pytest requests
```

Verify the installation:
```
python -c "import fastapi, pydantic, pytest, requests; print('All dependencies installed successfully')"
```

**4. Configure VSCode (if there are problem with imports)**
1. Open Command Palette (Cmd/Ctrl + Shift + P)
2. Select `Python: Select Interpreter`
3. Choose the Python interpreter inside `.venv`
4. If imports are still underlined, run `Developer: Reload Window`.

**5. Run the Backend**
Start the FastAPI server:
```
python -m uvicorn main:app --reload
```
Open the localhost (8000 possibly)

## 6. Demonstrate Postman and Pytest
**6.1 Testing with Postman**
A: Create a User:
1. Open Postman.
2. Create a new HTTP request.
3. Select POST.
4. Enter http://localhost:8000/users.
5. Select Body → raw → JSON.
6. Enter the example JSON request: ```{"name": "Alice", "email": "alice@demo.com"}```
7. Click Send.
8. Verify that the response status is 201 Created.
9. Record the returned user ID.

B: Retrieve a User:
1. Create another request.
2. Select GET.
3. Enter http://localhost:8000/users/{user_id}.
4. Replace {user_id} with the ID returned by the POST request.
5. Click Send.
6. Verify that the saved name and email are returned.

C: Retrieve all users: `GET http://localhost:8000/users`

**6.2 Testing with Pytest**
Run `python -m pytest -v`.

You can also verify the Postman data using Pytest, and demonstrate shared database, if you have time.
