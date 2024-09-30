from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses  import RedirectResponse
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/", response_class=RedirectResponse)
async def redirect_fastapi():
    return "/static/index.html"

# @router.get("/hello")
# def hello():
#     return { "message": "Hello World!" }

app.include_router(book_router, tags=["books"], prefix="/book")