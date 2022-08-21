FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY . /app
COPY main.py /app
COPY consumer.py /app
ENV FLASK_APP=main.py
# RUN pipenv run flask db init
# RUN pipenv run flask db migrate
# RUN pipenv run flask db upgrade
# CMD [ "pipenv","run","python","main.py" ]