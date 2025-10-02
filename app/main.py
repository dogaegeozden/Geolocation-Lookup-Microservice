from fastapi import FastAPI
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from app.routers import landing, geolocation
from app.core.limiter import init_limiter
from app.core.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_limiter(app) # initialize Redis limiter
    yield

app = FastAPI(lifespan=lifespan)

# Middlewares
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=settings.ALLOWED_REQUEST_TYPES,
    allow_headers=settings.ALLOWED_REQUEST_HEADERS,
)

# Static files
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

# Routers
app.include_router(landing.router)
app.include_router(geolocation.router)