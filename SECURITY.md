# Security Policy

## Supported Versions

This repository holds a historical SAS Customer Intelligence 360 solutions orchestration service (runs as a Windows/Unix service tying together the CI 360 marketing data, content delivery, identity, and cloud-export packages), retained as a reference and no longer under active development. Only the code currently deployed on each environment branch is supported — there is no long-term support for older commits.

| Branch | Environment | Status |
|---|---|---|
| `main` | Production | Supported |
| `staging` | Staging | Supported |
| `develop` | Development | Supported |

## Reporting a Vulnerability

This repository doesn't have a public issue tracker, so please don't report security concerns that way. Use one of:

- GitHub's [private vulnerability reporting](https://github.com/mnelson3/sas_ci360_solutions/security/advisories/new) (enabled on this repo), or
- Email **support@nelsongrey.com**

Either way, include:

- A description of the vulnerability and its potential impact
- Steps to reproduce, or a proof of concept if available
- Any relevant logs, request/response samples, or affected endpoints

You should get an acknowledgement within a few business days.

## Automated Dependency Scanning

Dependabot alerts and security updates, native GitHub secret scanning (with push protection), and code scanning (CodeQL) are all enabled on this repository. Avoid committing credentials or secrets regardless — API keys, tenant credentials, and cloud (e.g. Google BigQuery) service account keys are supplied at runtime via `config/config.ini` (kept out of source control) or environment variables / a secrets manager, never committed to source.
