from fastapi import APIRouter

from app.api.dependencies import DBSession

router = APIRouter(prefix="/rules", tags=["rules"])


# Endpoints will be added here once domain models and use cases are defined.
# Example:
#   @router.get("/", response_model=list[RuleResponse])
#   async def list_rules(db: DBSession) -> list[RuleResponse]:
#       ...
