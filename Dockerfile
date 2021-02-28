FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

# Install pre-reqs
COPY ./requirements.txt /
RUN pip install -r /requirements.txt

# Import the app code
COPY ./app /app
