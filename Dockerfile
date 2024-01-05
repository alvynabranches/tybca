FROM python:3.11.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# RUN python3 db.py

EXPOSE 8000

CMD [ "bash", "run.sh" ]