FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./j2x /j2x

CMD uvicorn --host=0.0.0.0 j2x.main:app
