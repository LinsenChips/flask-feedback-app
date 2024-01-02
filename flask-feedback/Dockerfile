# Verwende das offizielle Python-Image als Basis
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anwendungsdateien in das Arbeitsverzeichnis
COPY app.py /app/
COPY templates /app/templates

# Installiere die Flask- und MongoDB-Abhängigkeiten
RUN pip install --no-cache-dir Flask pymongo

# Exponiere den Port, auf dem die Anwendung läuft
EXPOSE 5000

# Starte die Anwendung beim Containerstart
CMD ["python", "app.py"]
