"""
Background task definitions.

Wire up a task queue (ARQ, Celery, etc.) here.
Workers must never import from app.api — only from application/domain/infrastructure.
"""
