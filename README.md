# Pele ![example workflow](https://github.com/Kakoytobarista/Pele/actions/workflows/django.yml/badge.svg)

>Web application for making an appointment at the PELE barbershop.
Link on host: https://pele.serveirc.com/
_______
### Technologies stack:
* python
* django
* django rest framework
* java script/html/css
* AWS
* cron
* bootstrap
* nginx
* certbot
* postgresSql
* docker
* docker-compose
* sentry


### Miro prototype:
https://miro.com/app/board/uXjVPLSL8fk=/

### How to deploy project:

1. Clone project:
```
git clone https://github.com/Kakoytobarista/Pele.git
```
2. Go to development branch:
```
git checkout development_branch
```
3. Go to directory with 'manage.py':
```
cd pele
```
4. Upload data: 
```
python3 manage.py uploader_appointments {current date}{Y-M-D} {until date}{Y-M-D}
```
5. Activate crons: 
```
python3 manage.py crontab add
```
6. Run server:
```
python3 manage.py runserver
```
