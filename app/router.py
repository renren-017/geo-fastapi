from bson.objectid import ObjectId
from fastapi import APIRouter, status

from app.database import shop_collection, shop_helper
from app.schemas import ShopBase, ShopUpdate

shop_router = APIRouter(
    prefix="/shops",
    tags=["shops"],
)


@shop_router.get("/", status_code=status.HTTP_200_OK)
def read_shops():
    shops = []
    for shop in shop_collection.find():
        shops.append(shop_helper(shop))
    return shops


@shop_router.post("/", response_model=ShopBase, status_code=status.HTTP_201_CREATED)
def post_shops(shop_data: ShopBase):
    shop = shop_collection.insert_one(shop_data.dict())
    new_shop = shop_collection.find_one({"_id": shop.inserted_id})
    return shop_helper(new_shop)


@shop_router.put("/{id}", status_code=status.HTTP_201_CREATED)
def update_shop(id: str, shop_data: ShopUpdate):
    shop_data = {k: v for k, v in shop_data.dict().items() if v is not None}
    shop = shop_collection.find_one({"_id": ObjectId(id)})
    if shop:
        shop_collection.update_one({"_id": ObjectId(id)}, {"$set": shop_data})
        return {"details": f'Shop with id {id} was updated successfully'}
    return {"details": "Shop not found"}


@shop_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shop(id: str):
    shop = shop_collection.find_one({"_id": ObjectId(id)})
    if shop:
        shop_collection.delete_one({"_id": ObjectId(id)})
        return {'details': f'Shop with id {id} was deleted successfully'}
    return {"details": "Shop not found"}
