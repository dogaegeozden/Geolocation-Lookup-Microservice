# Geolocation Lookup

A lightweight microservice for IP-based geolocation lookup, providing country, city, region, coordinates and more via a simple API.

---

## Features

- Lookup full geolocation details for an IP address  
- Retrieve country, city, region, timezone, latitude, and longitude  
- Simple RESTful API endpoints  
- Lightweight and easy to deploy  
- Uses [IP2Location LITE](https://lite.ip2location.com) database  

---

## Examples

1)
       curl http://localhost:8000/geolocation/all/212.8.253.145

2)
       curl http://localhost:8000/geolocation/country/212.8.253.145

3)
       curl http://localhost:8000/geolocation/city/212.8.253.145

4)
       curl http://localhost:8000/geolocation/coordinates/212.8.253.145

