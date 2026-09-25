# sas_ci360_solutions

Historical SAS Customer Intelligence 360 solutions repository, retained as a reference for the consolidated implementation. It is the orchestration layer of the `sas-ci360` package family: it runs as a long-lived Windows/Unix service that schedules and drives the individual CI 360 API packages (marketing data, content delivery, identity data, planning) end to end.

> This repository is superseded by [`sas-ci360-solutions`](https://github.com/mnelson3/sas-ci360-solutions), which holds the maintained implementation. Use this repository for reference only.

<br>

### Table of Contents

- <a href="#overview">Overview</a>
- <a href="#prerequisites">Prerequisites</a>
- <a href="#installation">Installation</a>
- <a href="#getting-started">Getting Started</a>
- <a href="#solutions-code">Solutions Code</a>
- <a href="#contributing">Contributing</a>
- <a href="#license">License</a>
- <a href="#additional-resources">Additional Resources</a>

<br>

### Overview

`sasci360solutions` is a scheduled service (see `src/WindowsService.py`, `src/UnixService.py`, `src/SASCI360Service.py`) that downloads, cleans, and builds CI 360 marketing data, uploads/reports on identity bridge data, builds content-delivery email data, and can export results to cloud targets such as Google BigQuery. It's driven by `config/config.ini` and built on the shared `sasci360apicore` and `sasci360api*` client packages.

<br>

### Prerequisites

- Python 3.6+
- A SAS CI 360 tenant with API credentials
- For the Windows service mode: `pywin32` / `servicemanager`; for Unix: the `python-daemon`/`service` packages
- Optional: Google Cloud credentials if exporting to BigQuery

<br>

### Installation

```bash
pip install -r requirements.txt
```

<br>

### Getting Started

1. Populate `config/config.ini` with tenant host, credentials, and job settings (never commit real credentials — use environment variables or a secrets manager instead).
1. Run as a one-off job via `src/sasci360solutions/main.py`, or install as a service via `src/WindowsService.py` (Windows) or `src/UnixService.py` (Unix/Linux).

<br>

### Solutions Code

The service is organized by data domain:

1. **marketing_data** — create/clean/download marketing tables
1. **identity_data** — upload identity bridge data, generate and send identity bridge reports/status messages
1. **content_delivery** — build content-delivery (e.g. email) data
1. **planning** — planning-related data operations
1. **cloud** — export to cloud targets (e.g. Google BigQuery)

<br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit contributions to this project.

<br>

### License

This project is licensed under the [Apache 2.0 License](LICENSE).

<br>

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
