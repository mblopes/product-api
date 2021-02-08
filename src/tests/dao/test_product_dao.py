import sys
sys.path.append('.')

import pytest  # noqa: E402
from sqlalchemy.orm.exc import UnmappedInstanceError  # noqa: E402
from src.dao.product_dao import ProductDao  # noqa: E402
from src.models.product import Product  # noqa: E402


@pytest.fixture
def create_instance():
    product = Product('Name', 'Description', 1.99)
    return product


def test_instance():
    product_dao = ProductDao()
    assert isinstance(product_dao, ProductDao)


def test_save(create_instance):
    product_saved = ProductDao().save(create_instance)
    assert product_saved.id_ is not None
    ProductDao().delete(product_saved)


def test_not_save():
    with pytest.raises(UnmappedInstanceError):
        product_saved = ProductDao().save('product')


def test_read_by_id(create_instance):
    product_saved = ProductDao().save(create_instance)
    product_read = ProductDao().read_by_id(product_saved.id_)
    assert isinstance(product_read, Product)
    ProductDao().delete(product_read)


def test_not_read_by_id():
    with pytest.raises(TypeError):
        product_read = ProductDao().read_by_id('product_saved.id_')


def test_read_all():
    product_read = ProductDao().read_all()
    assert isinstance(product_read, list)


def test_delete(create_instance):
    product_saved = ProductDao().save(create_instance)
    product_read = ProductDao().read_by_id(product_saved.id_)
    ProductDao().delete(product_read)
    product_read = ProductDao().read_by_id(product_saved.id_)
    assert product_read is None


def test_not_delete():
    with pytest.raises(UnmappedInstanceError):
        ProductDao().delete('product_read')
