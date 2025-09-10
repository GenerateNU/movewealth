from fastapi import APIRouter

router = APIRouter()


# Test
@router.get("/", status_code=200)
async def health_check():
    return {"status": "ok", "message": "API is running"}
