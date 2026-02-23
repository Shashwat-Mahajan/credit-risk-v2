
FROM python:3.12.6


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app



CMD gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT