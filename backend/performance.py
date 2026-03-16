import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def monitor_performance(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        logger.info(f"{func.__name__} took {duration:.2f}s")
        return result
    return wrapper
