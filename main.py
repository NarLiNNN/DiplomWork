from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from endpoint.report.ReportRequestGet import ReportGetRouter
from endpoint.report.ReportRequestPost import ReportPostRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI()
app.include_router(ReportPostRouter)
app.include_router(ReportGetRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", port = 8080, reload = True)