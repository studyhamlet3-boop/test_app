async def log_request(request, call_next):
    print("Logging request...")
    # logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    # logger.info(f"Response status: {response.status_code}")
    print("Request logged.")
    return response
