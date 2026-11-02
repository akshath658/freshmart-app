from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import database_models
from database import SessionLocal, engine
from models import Product

# Drop and recreate tables (dev only)
database_models.Base.metadata.drop_all(bind=engine)
database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://10.97.40.139:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def greet():
    return "Hello, welcome to Our Site!"


products = [
    Product(id=1,  name="Bananas (1 dozen)",     description="Fresh Alphonso bananas, naturally ripened",           price=60.00,  quantity=200),
    Product(id=2,  name="Apples (1 kg)",         description="Crisp Shimla apples, hand-picked daily",              price=180.00, quantity=150),
    Product(id=3,  name="Tomatoes (1 kg)",       description="Farm-fresh hybrid tomatoes",                           price=40.00,  quantity=300),
    Product(id=4,  name="Onions (1 kg)",         description="Premium Nashik onions",                                price=35.00,  quantity=400),
    Product(id=5,  name="Potatoes (1 kg)",       description="Fresh Kufri potatoes",                                 price=30.00,  quantity=350),
    Product(id=6,  name="Milk (1L)",             description="Amul Taaza full-cream milk",                           price=66.00,  quantity=500),
    Product(id=7,  name="Eggs (1 dozen)",        description="Farm-fresh brown eggs",                                price=84.00,  quantity=250),
    Product(id=8,  name="Wheat Flour (5 kg)",    description="Whole wheat atta, stone-ground",                       price=225.00, quantity=100),
    Product(id=9,  name="Rice (5 kg)",           description="Basmati rice, aged 1 year",                            price=350.00, quantity=120),
    Product(id=10, name="Cooking Oil (1L)",      description="Fortune sunflower oil",                                 price=145.00, quantity=200),
    Product(id=11, name="Mangoes (1 kg)",        description="Sweet Kesar mangoes, in season",                       price=150.00, quantity=180),
    Product(id=12, name="Oranges (1 kg)",        description="Juicy Nagpur oranges",                                 price=80.00,  quantity=160),
    Product(id=13, name="Green Peas (500g)",     description="Fresh garden peas",                                    price=50.00,  quantity=140),
    Product(id=14, name="Cucumbers (1 kg)",      description="Crisp local cucumbers",                                price=30.00,  quantity=220),
    Product(id=15, name="Bread (1 loaf)",        description="Whole wheat bread, baked fresh daily",                 price=45.00,  quantity=100),
    Product(id=16, name="Yogurt (400g)",         description="Amul Dahi, full cream",                                price=35.00,  quantity=180),
    Product(id=17, name="Tea (250g)",            description="Tata Golden Tips premium tea",                         price=125.00, quantity=90),
    Product(id=18, name="Sugar (1 kg)",          description="Refined white sugar",                                  price=45.00,  quantity=200),
    Product(id=19, name="Salt (1 kg)",           description="Iodized table salt",                                   price=25.00,  quantity=300),
    Product(id=20, name="Washing Powder (1 kg)", description="Surf Excel Matic",                                     price=110.00, quantity=150),
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
    db.close()

init_db()


@app.get("/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@app.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=Product)
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}   