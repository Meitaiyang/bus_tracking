FROM python:3.9-slim

COPY . /project

WORKDIR /project

RUN python3 -m pip install -r requirements.txt

ENV  FLASK_APP=app

# CMD [ "python3", "-m" , "flask", "run", "-h", "0.0.0.0" ,"-p","5050"]

CMD [ "pytest", "tests/"]