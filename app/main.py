"""
Your main entry point to the app
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, service, auth
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS for all origins
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=user.router)
app.include_router(router=service.router)
app.include_router(router=auth.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the TEE Beauty API"}
