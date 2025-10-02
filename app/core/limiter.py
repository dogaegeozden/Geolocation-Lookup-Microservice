import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter

async def init_limiter(app):
    redis_conn = await redis.from_url(
        "redis://localhost:6379",
        encoding="utf8",
        decode_responses=True,
    )
    await FastAPILimiter.init(redis_conn)
    # Store the connection on app state if you want to close it later
    app.state.redis = redis_conn
