from sqlalchemy import Column, String, Float
from sqlalchemy.orm import validates
from src.models.base_model import BaseModel



class Product(BaseModel):
    __tablename__ = 'PRODUCT'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    price = Column('price', Float, nullable=False)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price
    
    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        if not name.strip():
            raise ValueError("Name can't be empty value")
        if len(name) > 100:
            raise ValueError("Name length is more than 100 characters")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description must be str")
        if len(description) > 255:
            raise ValueError("Description length is more than 100 characters")
        return description

    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, float):
            raise TypeError("Price must be float")
        if price <= 0:
            raise ValueError(f"Price can't be lower than zero.")
        return price