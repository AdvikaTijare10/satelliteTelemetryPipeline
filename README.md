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
   Frame Collector
          │
          ▼
  Telemetry Decoder
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

## Dashboard

The Grafana dashboard provides:

* Current telemetry values through stat panels
* Historical telemetry trends through time-series visualizations
* Frame processing statistics
* Decoder success rate monitoring

<img width="768" height="347" alt="Image" src="https://github.com/user-attachments/assets/de02c2c0-5568-48b4-b474-ff236dd65cbb" />

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
├── telemetry_pipeline.py
├── telegraf.conf
├── requirements.txt
├── screenshots/
└── README.md
```

## Running the Project

1. Start Mosquitto MQTT Broker
2. Start InfluxDB
3. Start Telegraf
4. Start Grafana
5. Run the telemetry pipeline script

## Future Work

* Docker Compose deployment
* Multi-satellite support
* Telemetry anomaly detection
* Automated alerting for abnormal telemetry conditions

```
```
