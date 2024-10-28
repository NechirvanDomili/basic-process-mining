# basic-process-mining
Dieses Projekt führt grundlegendes Process Mining auf einem Event-Log durch, um wichtige KPIs zu extrahieren:

    Anzahl der Ereignisse (Events)
    Anzahl der Fälle (Cases)
    Anzahl der Aktivitäten (Activities)
    Anzahl der Prozessvarianten (Variants)

## Voraussetzungen

    Docker
    Python-Paket pandas (im Docker-Image integriert)

### Installation und Ausführung
Docker-Image erstellen

Führe diesen Befehl im Projektverzeichnis aus, um das Docker-Image zu bauen:

bash

docker build -t basic-process-mining .

Container ausführen

 Stelle sicher, dass bookstore.csv im Projektverzeichnis liegt oder gib den Pfad an und führe den Container aus:

### Linux/macOS:

bash

docker run -ti --rm -v $(pwd)/bookstore.csv:/opt/app/bookstore.csv basic-process-mining /opt/app/bookstore.csv

Windows (mit absolutem Pfad):

bash

docker run -ti --rm -v /path/to/bookstore.csv:/opt/app/bookstore.csv basic-process-mining /opt/app/bookstore.csv

### Beispiel-CSV-Dateiformat

Die Datei bookstore.csv sollte das folgende Format haben:

python

Case;Activity;Timestamp
1;enter bookstore;2024-07-24T17:48:19.362Z
1;browse books;2024-07-24T17:49:24.362Z
...

### Funktionen

#### Das Skript berechnet:

    Anzahl der Events: Zeilenanzahl in der CSV-Datei.
    Anzahl der Cases: Eindeutige Werte in der Case-Spalte.
    Anzahl der Activities: Eindeutige Werte in der Activity-Spalte.
    Anzahl der Variants: Unterschiedliche Prozessvarianten (Sequenzen von Aktivitäten) pro Fall.

