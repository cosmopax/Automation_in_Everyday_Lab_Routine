# syntax=docker/dockerfile:1
FROM python:3.13

COPY . /
WORKDIR /

RUN python -m pip install --upgrade pip setuptools flask flask-login flask-socketio pydantic numpy requests
RUN python -m pip install -e .
RUN python -m pip list

EXPOSE 5000

ENV ENDPOINT_ELN http://eln_server:5001/api/
CMD ["python","-m", "automationserver.main_server"]
