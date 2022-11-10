FROM python:3.8.5
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
COPY pele /code
COPY README.md /code
RUN pip install poetry
RUN pip install psycopg2-binary
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
CMD [ "sh", "-c", \
"python3 manage.py crontab add \
&& \
python3 manage.py migrate \
&& \
python3 manage.py collectstatic --noinput \
&& \
python 3 manage.py loaddata db_data.json \
&& \
gunicorn pele.wsgi:application --bind 0:8000" \
]
