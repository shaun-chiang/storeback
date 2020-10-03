FROM python:3.6-alpine

COPY . /project
RUN pip install -r /project/requirements.txt

WORKDIR /project/app
CMD ["python","app.py"]