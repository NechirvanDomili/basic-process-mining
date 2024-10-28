# Basis-Image festlegen
FROM python:3.9-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /opt/app

# Installiere die Abhängigkeiten (einschließlich pandas)
RUN pip install pandas

# Kopiere das Python-Skript in das Arbeitsverzeichnis
COPY basic_process_mining.py .

# Startbefehl für den Container festlegen
ENTRYPOINT ["python", "basic_process_mining.py"]
