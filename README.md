# Satellite Telemetry Monitoring Pipeline

End-to-end telemetry processing pipeline for real UWE-4 satellite telemetry using MQTT, InfluxDB, and Grafana.

## Overview

This project collects telemetry frames from the UWE-4 satellite through the SatNOGS Telemetry API, decodes raw beacon frames into engineering telemetry, streams the decoded data through MQTT, stores it in InfluxDB, and visualizes key spacecraft health metrics using Grafana.

The system provides monitoring of battery voltages, currents, temperatures, power consumption, frame processing statistics, and decoder success rates.

## Architecture

```text
SatNOGS Telemetry API
          │
          ▼
 Telemetry Ingestion Service
          │
          ▼
   UWE-4 Beacon Decoder
          │
          ▼
      MQTT Publisher
          │
          ▼
    Mosquitto Broker
          │
          ▼
        Telegraf
          │
          ▼
        InfluxDB
          │
          ▼
   Grafana Dashboard
```


## Features

* Fetches real UWE-4 telemetry frames from SatNOGS
* Decodes raw hexadecimal beacon frames into telemetry parameters
* Streams telemetry through MQTT
* Stores time-series telemetry data in InfluxDB
* Visualizes spacecraft health metrics using Grafana
* Tracks processed frames, decoding failures, and decoder success rate
* Supports historical telemetry replay and analysis

## Monitored Parameters

* Battery A Voltage
* Battery B Voltage
* Battery A Current
* Battery B Current
* Battery A Temperature
* Battery B Temperature
* OBC Temperature
* Power Consumption

## Telemetry recieved after decoding, parsing and extracting required fields

<img width="812" height="226" alt="Image" src="https://github.com/user-attachments/assets/f371f14a-9763-47c5-8528-2a7ea28f229b" />

## Dashboard

The Grafana dashboard provides:

* Current telemetry values through stat panels
* Historical telemetry trends through time-series visualizations
* Frame processing statistics
* Decoder success rate monitoring

<img width="805" height="378" alt="Image" src="https://github.com/user-attachments/assets/d35aef69-1cfc-45e8-93ca-dd984eab87cd" />

<img width="772" height="362" alt="Image" src="https://github.com/user-attachments/assets/1159cbb6-4510-4be1-b8af-f40f56b82fe4" />

<img width="818" height="314" alt="Image" src="https://github.com/user-attachments/assets/6d392cbb-a1b9-4e59-8a1a-38e12eed163c" />

## Technology Stack

* Python
* SatNOGS Telemetry API
* MQTT (Mosquitto)
* Telegraf
* InfluxDB
* Grafana

## Project Structure

```text
project/
├── config/
│   ├── grafana_dashboard.json
│   ├── settings.py
│   └── telegraf.conf
│
├── src/
│   ├── decoder/
│   ├── docs/
│   ├── publisher/
│   └── satnogs/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```


## Running the Project

The telemetry pipeline requires the following services to be available:

Mosquitto MQTT Broker,
Telegraf,
InfluxDB,
Grafana

Once the supporting services are running, execute:

python main.py

## Future Work

* Containerized deployment using Docker 
* Continuous live telemetry ingestion from SatNOGS observations
* Multi-satellite telemetry support
* Telemetry anomaly detection and health monitoring
* Automated alerting for abnormal telemetry condition


