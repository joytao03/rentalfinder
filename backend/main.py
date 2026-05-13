from fastapi import FastAPI
from pydantic import BaseModel

from extractor import extract_rental_info
from database import init_db, save_rental, get_all_rentals

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


init_db()


class RentalRequest(BaseModel):
    text: str
    url: str = ""
    title: str = ""


@app.get("/")
def home():
    return {"message": "Rental Finder API Running"}


@app.post("/extract")
def extract(data: RentalRequest):
    result = extract_rental_info(
        text=data.text,
        url=data.url,
        title=data.title
    )

    print("\n===== EXTRACTED RESULT =====")
    print(result)

    if result["is_rental"]:
        save_rental(result)

    return result


@app.get("/rentals")
def rentals():
    return get_all_rentals()