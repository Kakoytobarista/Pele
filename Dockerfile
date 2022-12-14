FROM python:3.8.5

ENV PYTHONUNBUFFERED=1


WORKDIR /code

COPY poetry.lock pyproject.toml /code/
COPY pele /code
COPY README.md /code
RUN apt-get update && apt-get -y install cron vim
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN pip3 install psycopg2-binary
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
CMD [ "sh", "-c", \
"python3 manage.py migrate \
&& \
python3 manage.py collectstatic --noinput \
&& \
python3 manage.py crontab add \
&& \
service cron start \
&& \
gunicorn pele.wsgi:application --bind 0:8000" \
]
