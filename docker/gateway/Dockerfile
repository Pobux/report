FROM python:3.5-alpine
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["cat", "run.py"]
CMD ["python3", "run.py"]
