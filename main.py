from fastapi import FastAPI

from core.config import settings
from routes import order_items, auth

app = FastAPI(debug=settings.debug)

app.include_router(order_items.router)
app.include_router(auth.router)



"""
{
  "id": 2,
  "name": "saxeli",
  "email": "test@example.com",
  "is_active": true
}


"""