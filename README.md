# FastAPI Clean Architecture

A production-grade FastAPI project following **hexagonal (clean) architecture** with async PostgreSQL, Alembic migrations, and Pydantic v2.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI |
| Database | PostgreSQL (async via `asyncpg`) |
| ORM | SQLAlchemy 2.0 (async) |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Config | pydantic-settings |
| Runtime | Python 3.11+ / Uvicorn |

---

## Project Structure

```
fastapi-clean-arch/
│
├── main.py                        # App factory, lifespan, exception handlers
├── pyproject.toml                 # Dependencies, tooling config
├── .env.example                   # Copy to .env and fill in secrets
├── alembic.ini
│
├── alembic/
│   ├── env.py                     # Async migration runner
│   ├── script.py.mako             # Migration file template
│   └── versions/                  # Generated migration files
│
└── app/
    ├── core/                      # Cross-cutting concerns
    │   ├── config.py              # Pydantic Settings — reads from .env
    │   ├── exceptions.py          # App-wide exception hierarchy
    │   └── logging.py             # Structured logging (JSON in prod)
    │
    ├── domain/                    # Pure business rules — no framework deps
    │   ├── base.py                # Entity base dataclass
    │   ├── models/                # Domain entity classes
    │   └── repositories/
    │       └── base.py            # Repository[T] abstract port (interface)
    │
    ├── application/               # Orchestration — no HTTP, no ORM
    │   ├── base.py                # BaseUseCase[Request, Response] template
    │   ├── services/              # Multi-step orchestration services
    │   └── use_cases/             # Single-responsibility use cases
    │
    ├── infrastructure/            # Adapters — implements domain ports
    │   ├── database/
    │   │   ├── base.py            # SQLAlchemy DeclarativeBase + UUID + timestamps
    │   │   ├── session.py         # Async engine, session factory, get_db_session()
    │   │   └── models/            # ORM model classes
    │   ├── messaging/             # Pub/sub, queues (Kafka, Redis, etc.)
    │   └── providers/             # External API clients / adapters
    │
    ├── api/                       # HTTP presentation layer
    │   ├── dependencies.py        # DBSession / AppSettings typed DI aliases
    │   └── v1/
    │       ├── router.py          # Aggregates all v1 route modules
    │       └── routes/
    │           ├── events.py      # /api/v1/events
    │           └── rules.py       # /api/v1/rules
    │
    ├── schemas/                   # Pydantic v2 request / response DTOs
    │   ├── event.py               # EventCreate, EventUpdate, EventResponse
    │   └── rule.py                # RuleCreate, RuleUpdate, RuleResponse
    │
    └── workers/
        └── tasks.py               # Background task definitions
```

---

## Dependency Flow

Outer layers depend inward. Inner layers never import from outer layers.

```
api ──▶ application ──▶ domain
        application ──▶ infrastructure  (through domain repository ports)
schemas             ──▶ (api layer only)
workers             ──▶ application / infrastructure
core                ──▶ imported by all layers
```

---

## Getting Started

### 1. Clone and install

```bash
git clone <repo-url>
cd fastapi-clean-arch
pip install -e ".[dev]"
```

### 2. Configure environment

```bash
cp .env.example .env
```

Edit `.env` and set at minimum:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
SECRET_KEY=<output of: openssl rand -hex 32>
```

### 3. Run database migrations

```bash
# Create your first migration (after adding ORM models)
alembic revision --autogenerate -m "init"

# Apply migrations
alembic upgrade head
```

### 4. Start the server

```bash
uvicorn main:app --reload
```

| URL | Description |
|---|---|
| `http://localhost:8000/docs` | Swagger UI (dev only) |
| `http://localhost:8000/redoc` | ReDoc (dev only) |
| `http://localhost:8000/api/v1/health` | Liveness probe |

---

## Adding a New Feature

Follow these steps to keep layers clean:

1. **Domain model** — add a dataclass to `app/domain/models/`
2. **Repository port** — add an abstract interface to `app/domain/repositories/`
3. **ORM model** — add a SQLAlchemy model to `app/infrastructure/database/models/`
4. **Repository impl** — implement the port in `app/infrastructure/database/`
5. **Use case** — add business logic to `app/application/use_cases/`
6. **Schema** — add Pydantic DTOs to `app/schemas/`
7. **Route** — add endpoints to `app/api/v1/routes/` and register in `router.py`

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `APP_NAME` | `FastAPI Clean Arch` | Application name |
| `APP_VERSION` | `0.1.0` | Application version |
| `DEBUG` | `false` | Enables debug logging and SQL echo |
| `ENVIRONMENT` | `development` | `development` / `staging` / `production` |
| `DATABASE_URL` | _(required)_ | Must use `postgresql+asyncpg://` scheme |
| `DATABASE_POOL_SIZE` | `10` | SQLAlchemy connection pool size |
| `DATABASE_MAX_OVERFLOW` | `20` | Max connections above pool size |
| `SECRET_KEY` | _(required)_ | Used for token signing |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | JWT expiry window |
| `API_V1_PREFIX` | `/api/v1` | URL prefix for all v1 routes |

---

## Development

```bash
# Lint
ruff check .

# Type check
mypy app

# Tests
pytest
```
