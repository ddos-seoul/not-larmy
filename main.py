import asyncio
import time

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_408_REQUEST_TIMEOUT

from resolvers.router import api_router

app = FastAPI()


@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        start_time = time.time()
        return await asyncio.wait_for(call_next(request), timeout=1.5)

    except asyncio.TimeoutError:
        process_time = time.time() - start_time
        return JSONResponse(
            {
                "detail": "Request processing time excedeed limit",
                "processing_time": process_time,
            },
            status_code=HTTP_408_REQUEST_TIMEOUT,
        )


app.include_router(api_router)
