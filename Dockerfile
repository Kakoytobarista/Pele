FROM python:3.8.5

ENV PYTHONUNBUFFERED=1


WORKDIR /code

COPY poetry.lock pyproject.toml /code/
COPY pele /code
COPY README.md /code
COPY requirements.txt /code
RUN poetry install
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install psycopg2-binary
CMD [ "sh", "-c", \
"python3 manage.py migrate \
&& \
python3 manage.py collectstatic --noinput \
&& \
gunicorn pele.wsgi:application --bind 0:8000" \
]
