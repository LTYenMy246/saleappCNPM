from app.models import Category, Product
from app import app
def load_categories():
    return Category.query.all()

def load_products(page=1):
    prod = Product.query
    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    prod = prod.slice(start, start + page_size)
    return prod.all()
def count_products():
    return Product.query.count()