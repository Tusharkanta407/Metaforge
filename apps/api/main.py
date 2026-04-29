from fastapi import FastAPI
from routers import auth, workspaces
from routers.integrations import om_oauth

app = FastAPI(title="MetaForge API")

app.include_router(auth.router)
app.include_router(workspaces.router)
app.include_router(om_oauth.router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
