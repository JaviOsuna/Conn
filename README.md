# Conn

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Run Postgresql

```sh
docker run --name some-postgres -e POSTGRES_DB=recipes3 -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```