# TSETMC Web Scraping & Data Extraction API

A Python web scraping and data extraction project that collects market data from TSETMC, processes and normalizes the data, stores it in PostgreSQL, caches recent results with Redis, and serves the collected data through a FastAPI REST API.

This project is built as a web scraping portfolio project. It demonstrates how raw public data can be collected, cleaned, stored, cached, and exposed through a clean API for dashboards, reporting tools, automation systems, or business applications.

> Note: This project focuses on public data extraction from a market data endpoint. It does not bypass authentication, paywalls, captchas, or restricted systems.

---

## Features

- Web scraping / public data extraction from TSETMC
- Async data fetching with `aiohttp`
- Data validation and cleaning with Pydantic
- PostgreSQL storage for extracted data
- Redis caching for faster repeated responses
- FastAPI REST API for serving scraped data
- Sorting by fields such as price, volume, P/E, EPS, and more
- Filtering by instrument code
- Pagination with `limit` and `offset`
- Persian field-name conversion for API responses
- Docker-ready project structure
- Health check endpoint

---

## Tech Stack

- Python
- FastAPI
- aiohttp
- PostgreSQL
- Redis
- SQLAlchemy
- Pydantic
- Docker

---

## Project Structure

```text
.
├── app
│   ├── cache.py
│   ├── database.py
│   ├── fetcher.py
│   ├── main.py
│   ├── models.py
│   ├── models_postgres.py
│   ├── persian_converter.py
│   ├── postgres_reader.py
│   ├── postgres_writer.py
│   └── socket_client.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md