from fastapi import FastAPI
from api.events import app as info_router

app = FastAPI()

app.include_router(info_router, prefix="/api/res")

@app.get("/love")
async def root():
    return await love()
async def love():
    return {"message": "satvik known fastapi"}