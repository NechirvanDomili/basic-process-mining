FROM python:3.9-slim

WORKDIR /opt/app

RUN pip install pandas

COPY basic_process_mining.py .

ENTRYPOINT ["python", "basic_process_mining.py"]
