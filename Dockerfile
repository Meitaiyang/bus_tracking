FROM python:3.9-slim 

WORKDIR /

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD [ "uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0"]
