from fastapi import APIRouter, Depends, HTTPException, Request
from sql_dir import crud, schemas
from sqlalchemy.orm import Session
from sql_dir.database import SessionLocal
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="static/html")

reg_route = APIRouter(
    prefix='/register',
    tags=['register']
)

reg_route.mount("/static", StaticFiles(directory="static"), name="static")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@reg_route.get('/', response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@reg_route.post('/user')
async def register_user(user: schemas.RegisterModel, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User is already registered.')
    return crud.register_user(db=db, user=user)


@reg_route.get('/all')
async def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_info(db=db)
