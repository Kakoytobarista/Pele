# Pele
![example workflow](https://github.com/Kakoytobarista/Pele/actions/workflows/django.yml/badge.svg)
Web application for making an appointment at the PELE barbershop.

Technologies stack:
bla bla

Miro prototype:
https://miro.com/app/board/uXjVPLSL8fk=/

### How to deploy project:

1. Run docker compose:
```docker-compose up -d```
3. Go to app container: ```docker exec -it {id of pele app} bash```
4. Upload data to data base: ```python manage loaddata dumb_data.json```
