import ipaddress
import IP2Location
import pathlib
from app.core.settings import settings

ip_db = IP2Location.IP2Location(settings.IP2LOCATION_DB)

def extract_geolocation_all(ip_address):
    try:
        ip_addr = ipaddress.ip_address(ip_address)
        rec = ip_db.get_all(str(ip_addr))
    except Exception:
        all = "??"

    return {
        "all": rec,
    }

def extract_geolocation_country(ip_address):
    try:
        ip_addr = ipaddress.ip_address(ip_address)
        rec = ip_db.get_all(str(ip_addr))
        country_code = rec.country_short
    except Exception:
        country_code = "??"
    return {
        "country_code": country_code,
    }

def extract_geolocation_city(ip_address):
    try:
        ip_addr = ipaddress.ip_address(ip_address)
        rec = ip_db.get_all(str(ip_addr))
        city_name = rec.city
    except Exception:
        country_code = "??"
    return {
        "city_name": city_name,
    }

def extract_geolocation_coordinates(ip_address):
    try:
        ip_addr = ipaddress.ip_address(ip_address)
        rec = ip_db.get_all(str(ip_addr))
        latitude = rec.latitude
        longitude = rec.longitude
        coordinates = f"{rec.latitude}, {rec.longitude}"
    except Exception:
        coordinates = "??"
    return {
        "coordinates": coordinates,
    }
