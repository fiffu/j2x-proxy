FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
RUN pip install --upgrade -r /app/requirements.txt
