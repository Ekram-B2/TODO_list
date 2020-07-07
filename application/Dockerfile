FROM python:3

RUN apt-get update && apt-get install sqlite3 libsqlite3-dev -y && apt-get install nano

WORKDIR /root
ADD ./requirements.txt /root
RUN pwd
RUN pip install -r "requirements.txt"

ENTRYPOINT ["python", "app.py"]
