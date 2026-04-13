from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.exceptions import DeliveryNotFoundException


async def delivery_not_found_handler(request: Request, exc: DeliveryNotFoundException):
    return JSONResponse(status_code=404, content={"message": str(exc) or "Доставка не найдена"})


exception_handlers = {
    DeliveryNotFoundException: delivery_not_found_handler
}
