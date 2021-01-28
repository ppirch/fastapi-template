import uvicorn
from fastapi import FastAPI
from routers import router_template
from fastapi.middleware.cors import CORSMiddleware

DESC_TEXT = "FastAPI"

app = FastAPI(
    title='FastAPI',
    description=DESC_TEXT,
    version='0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_main():
    return {"msg": "FastAPI", "version": app.version}


app.include_router(router_template.router,
                   prefix="/template", tags=["Template"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
