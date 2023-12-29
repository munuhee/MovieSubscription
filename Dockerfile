FROM python:3.10.12-alpine
WORKDIR /moviesubscription
COPY . /moviesubscription
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver  