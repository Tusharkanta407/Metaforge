from fastapi import APIRouter

router = APIRouter(prefix="/integrations/om", tags=["integrations"])


@router.get("/ping")
def ping_om() -> dict:
    return {"message": "om oauth router ready"}
