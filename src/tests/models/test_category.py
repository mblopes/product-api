import sys
sys.path.append('.')
from src.models.product import Product
import pytest


def test_product_instance():
    product = Product('name', "description", 2.0)

    assert isinstance(product, Product)


def test_product_name_empty():
    with pytest.raises(ValueError):
        product = Product('', 'descricao', 3.4)


def test_product_name_len():
    with pytest.raises(ValueError):
        product = Product('nome aleatorio'*100, 'descricao', 3.4)


def test_product_name_int():
    with pytest.raises(TypeError):
        product = Product(10, 'descricao', 3.4)


def test_product_description_len():
    with pytest.raises(ValueError):
        product = Product('nome aleatorio', 'descricao'*300, 3.4)


def test_product_description_int():
    with pytest.raises(TypeError):
        product = Product('nome aleatorio', 123, 3.4)


def test_product_price_zero():
    with pytest.raises(ValueError):
        product = Product('nome aleatorio', 'descricao', 0.0)


def test_product_price_not_float():
    with pytest.raises(TypeError):
        product = Product('nome aleatorio', 'descricao', '')
