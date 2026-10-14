from fastapi import FastAPI

from core.config import settings
from routes import order_items

app = FastAPI(debug=settings.debug)

app.include_router(order_items.router)


