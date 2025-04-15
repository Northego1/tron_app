from fastapi import APIRouter

from tron_app.presentation.api.v1.api import router as _router_v1

router = APIRouter(prefix="/api/v1")
router.include_router(_router_v1)
