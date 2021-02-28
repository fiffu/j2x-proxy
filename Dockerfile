FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade -r ./requirements.txt
COPY ./app /app
