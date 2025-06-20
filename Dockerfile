FROM python:3-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
