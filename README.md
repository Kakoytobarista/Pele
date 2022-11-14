# Pele
![example workflow](https://github.com/Kakoytobarista/Pele/actions/workflows/django.yml/badge.svg)
Web application for making an appointment at the PELE barbershop.

Technologies stack:
bla bla

Miro prototype:
https://miro.com/app/board/uXjVPLSL8fk=/

### How to deploy project (local):

1. Clone project:
```git clone https://github.com/Kakoytobarista/Pele.git```
2. go to development branch:
```git checkout development_branch```
3. Go to directory with 'manage.py':
```cd pele```
4. Upload data: 
```python3 manage.py uploader_appointments {current date}{Y-M-D} {until date}{Y-M-D}```
5. Activate crons: 
```python3 manage.py crontab add ```
6. Run server:
```python3 manage.py runserver```
