import uvicorn
from admin.user_views import UserView
from config.db_config import sync_engine
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask
from flask_admin import Admin
from model.user_model import User
from routers import router
from sqlalchemy.orm import Session

db = Session(sync_engine)

flask_app = Flask(__name__)
flask_app.config["SECRET_KEY"] = "secret"

app = FastAPI(title="some peace of sh...  test", redoc_url="/redoc")

admin = Admin(flask_app, template_mode="bootstrap4")
app.include_router(router)

admin.add_view(UserView(User, db))

app.mount("", WSGIMiddleware(flask_app))
app.mount("/admin", WSGIMiddleware(admin.app))
