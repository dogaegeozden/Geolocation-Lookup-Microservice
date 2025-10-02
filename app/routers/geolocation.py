from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_limiter.depends import RateLimiter
from app.modules.geolocation import (
    extract_geolocation_all,
    extract_geolocation_country,
    extract_geolocation_city,
    extract_geolocation_coordinates,
)

router = APIRouter(prefix="/geolocation")

@router.get(
    "/all/{ip_address}",
    response_class=JSONResponse,
    dependencies=[Depends(RateLimiter(times=1, seconds=1))]
)
async def get_all(ip_address):
    return extract_geolocation_all(ip_address)

@router.get(
    "/country/{ip_address}",
    response_class=JSONResponse,
    dependencies=[Depends(RateLimiter(times=1, seconds=1))]
)
async def get_country(ip_address):
    return extract_geolocation_country(ip_address)

@router.get(
    "/city/{ip_address}",
    response_class=JSONResponse,
    dependencies=[Depends(RateLimiter(times=1, seconds=1))]
)
async def get_city(ip_address):
    return extract_geolocation_city(ip_address)

@router.get(
    "/coordinates/{ip_address}",
    response_class=JSONResponse,
    dependencies=[Depends(RateLimiter(times=1, seconds=1))]
)
async def get_coordinates(ip_address):
    return extract_geolocation_coordinates(ip_address)