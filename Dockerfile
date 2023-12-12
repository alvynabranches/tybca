FROM python:3.11.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0", "--reload" ]