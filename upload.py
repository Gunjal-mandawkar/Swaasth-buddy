from fastapi import APIRouter

upload_router = APIRouter()

@upload_router.get("/upload_test")
def upload_test():
    return {"message": "Upload route is working!"}
