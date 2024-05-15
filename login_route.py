from fastapi import APIRouter, Depends, HTTPException, Request
from sql_dir import schemas, crud
from sql_dir.database import SessionLocal
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="static/html")

log_route = APIRouter(
    prefix='/login',
    tags=['login']
)

log_route.mount("/static", StaticFiles(directory="static"), name="static")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@log_route.get('/', response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@log_route.post('/user')
async def login_user(user: schemas.LoginModel, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail='User is not registered')
    if not check_password_hash(db_user.password, user.password):
        raise HTTPException(status_code=401, detail='Password does not match. Please try again.')

    return {"message": "Login success"}
