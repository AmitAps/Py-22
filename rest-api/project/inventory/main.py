from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


redis = get_redis_connection(
    host="redis-15050.c301.ap-south-1-1.ec2.cloud.redislabs.com",
    port=15050,
    password="twalZqtBKBHdyVx3j5YhyNjokffZKaV5",
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity_available: int

    class Meta:  #Meta calss
        database = redis




@app.get("/products")
def all():
    return [format(pk) for pk in Product.all_pks()]  #list comprehension

def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity_available
    }

@app.post('/products')
def create(product: Product):
    return product.save()


#19:20
