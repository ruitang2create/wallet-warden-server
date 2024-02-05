from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.controller.routers import api_router

app = FastAPI(debug=True, title="Wallet Warden API", version="1.0")

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

# import api.controller.spending # noqa
# import api.controller.income # noqa