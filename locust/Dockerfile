FROM python:3.9-slim
WORKDIR /locust
COPY locustfile.py ./
RUN pip install locust requests
CMD ["locust"]