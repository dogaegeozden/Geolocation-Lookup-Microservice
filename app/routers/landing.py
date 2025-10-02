from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from app.modules.geolocation import extract_geolocation_country
from app.modules.client_info import get_ip
from app.core.templates import templates

router = APIRouter()

@router.get("/")
async def root(request: Request):
    ip_address = get_ip(request)
    country_code = extract_geolocation_country(ip_address)
    return RedirectResponse(url="/tr/" if info["country_code"] == "TR" else "/en/")

@router.get("/en/", response_class=HTMLResponse)
async def landing_page_en(request: Request):
    return templates.TemplateResponse("landing_en.html", {"request": request})

@router.get("/tr/", response_class=HTMLResponse)
async def landing_page_tr(request: Request):
    return templates.TemplateResponse("landing_tr.html", {"request": request})