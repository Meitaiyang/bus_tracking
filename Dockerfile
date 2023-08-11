FROM python:latest

COPY . .

WORKDIR /

RUN python3 -m pip install -r requirements.txt

WORKDIR /tests/

ENV  FLASK_APP=app

# CMD [ "python3", "-m" , "flask", "run", "-h", "0.0.0.0" ,"-p","5050"]

CMD [ "pytest" ]