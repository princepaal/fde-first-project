# uvicorn app.main:app --reload


# Let's break it down:

# uvicorn → Starts the server.
# app.main → Looks for the main.py file inside the app folder.
# :app → Uses the app = FastAPI() object inside main.py.
# --reload → Automatically restarts the server whenever you save a file.