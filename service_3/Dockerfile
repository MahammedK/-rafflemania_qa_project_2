FROM python:3.8.10

WORKDIR /service_3

RUN pip3 install -r requirements.txt

COPY app.py .

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]