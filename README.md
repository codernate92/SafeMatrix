# 🛡️ SafeMatrix

A modular, end-to-end **Threat Hunting Framework** built for analysts and researchers. SafeMatrix combines real-time log ingestion, CTI enrichment, alerting, and incident response automation using powerful tools like TheHive, Splunk, MISP, and OSQuery.

---

## ⚙️ Architecture Overview

```
SafeMatrix/
├── config/
│   ├── settings.yaml
│   └── thehive_config.json
│
├── data/
│   ├── test_logs.py
│   ├── threatintel.csv
│   └── data_cleanup.py
│
├── integrations/
│   ├── aws_log_fetcher.py
│   ├── osquery_monitor.py
│   ├── threatintel_importer.py
│   ├── splunk_forwarder.py
│   └── thehive_api.py
│
├── scripts/
│   ├── helpers.py
│   ├── incident.py
│   └── main.py
│
├── tests/
│   ├── test_thehive_client.py
│   └── test_logs.py
│
├── requirements.txt
├── constraints.txt
└── README.md
```

---

## 🚀 Features

- **AWS CloudTrail + Sysmon** log ingestion
- **OSQuery** endpoint telemetry collection
- **MISP Integration** for IOC enrichment
- **TheHive** case creation + alerting
- **Splunk Integration** for visualizations
- Modular Python codebase with full test suite

---

## ✅ Requirements

- Docker
- Python 3.10+
- MISP instance (self-hosted or cloud)
- TheHive (running locally or via Docker)
- Splunk (or Splunk HEC token)

---

## 🔧 Installation

```bash
git clone https://github.com/YOUR_USERNAME/SafeMatrix.git
cd SafeMatrix
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure you update `config/settings.yaml` and `config/thehive_config.json` with your local instance details.

---

## 📦 Run the Framework

```bash
python scripts/main.py
```

It will:
1. Fetch logs from AWS and Sysmon.
2. Correlate events.
3. Enrich with MISP.
4. Create TheHive alerts.
5. Forward events to Splunk (optional).

---

## 🔍 Threat Intelligence Enrichment

SafeMatrix uses MISP’s API to enrich events based on:
- IP addresses
- Hashes
- Domains

Modify `integrations/threatintel_importer.py` to integrate your preferred CTI feeds.

---

## ⚠️ Alerts & Case Management

Cases are automatically created in TheHive with relevant context and severity. You can review, triage, and escalate them in your dashboard.

---

## 📊 Visualization

Use pre-built dashboards in Splunk for:
- Suspicious API calls
- Lateral movement detection
- Endpoint anomalies

---

## 🤝 Contributing

Pull requests welcome! Drop your threat detection ideas, rules, or integrations. Let’s make this the best analyst toolkit out there.

---

## 📜 License

MIT License

---

> Built with resilience by cyber analysts, for cyber analysts.
