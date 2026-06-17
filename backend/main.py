from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="business_dashboard"
)

@app.get("/")
def home():
    return {"message": "Business Dashboard API Running"}

@app.get("/businesses")
def get_businesses():
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM listing_master LIMIT 20")

    data = cursor.fetchall()

    return data
@app.get("/search")
def search_business(city: str):

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT *
    FROM listing_master
    WHERE city = %s
    LIMIT 20
    """

    cursor.execute(query, (city,))
    data = cursor.fetchall()

    return data

@app.get("/filter")
def filter_business(city: str, category: str):

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT *
    FROM listing_master
    WHERE city=%s
    AND category=%s
    """

    cursor.execute(query, (city, category))

    data = cursor.fetchall()

    return data

@app.get("/total-count")
def total_count():

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
    SELECT COUNT(*) as total
    FROM listing_master
    """)

    data = cursor.fetchone()

    return data

@app.get("/city-count")
def city_count():

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
    SELECT city,
           COUNT(*) as count
    FROM listing_master
    GROUP BY city
    """)

    data = cursor.fetchall()

    return data

@app.get("/category-count")
def category_count():

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
    SELECT category,
           COUNT(*) as count
    FROM listing_master
    GROUP BY category
    """)

    data = cursor.fetchall()

    return data

from pydantic import BaseModel

class Business(BaseModel):
    business_name: str
    category: str
    city: str
    address: str
    phone: str
    source: str


@app.post("/add-business")
def add_business(business: Business):

    cursor = db.cursor()

    query = """
    INSERT INTO listing_master
    (business_name, category, city, address, phone, source)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        business.business_name,
        business.category,
        business.city,
        business.address,
        business.phone,
        business.source
    )

    cursor.execute(query, values)
    db.commit()

    return {"message": "Business Added Successfully"}

@app.delete("/delete-business/{business_id}")
def delete_business(business_id: int):

    cursor = db.cursor()

    query = """
    DELETE FROM listing_master
    WHERE id=%s
    """

    cursor.execute(query, (business_id,))
    db.commit()

    return {"message": "Business Deleted Successfully"}

@app.put("/update-business/{business_id}")
def update_business(business_id: int, business: Business):

    cursor = db.cursor()

    query = """
    UPDATE listing_master
    SET business_name=%s,
        category=%s,
        city=%s,
        address=%s,
        phone=%s,
        source=%s
    WHERE id=%s
    """

    values = (
        business.business_name,
        business.category,
        business.city,
        business.address,
        business.phone,
        business.source,
        business_id
    )

    cursor.execute(query, values)
    db.commit()

    return {"message": "Business Updated Successfully"}