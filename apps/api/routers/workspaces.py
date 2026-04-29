from fastapi import APIRouter

router = APIRouter(prefix="/workspaces", tags=["workspaces"])


@router.get("/ping")
def ping_workspaces() -> dict:
    return {"message": "workspaces router ready"}
