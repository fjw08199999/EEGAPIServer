import requests
import json
from fastapi import FastAPI
from starlette.responses import FileResponse

url = "http://172.20.10.6:5555"
app = FastAPI()

# DataSampo
FoodData = [{
    "productID": 1,
    "productName": "巧克力脆皮雞蛋糕",
    "productImage": url+"/imageGIF",
    "productInfo": "濃郁苦甜巧顆粒, 在口中爆出濃濃的奇妙口感",
    "productPrice": 80
    }
    ,
    {
        "productID": 2,
        "productName": "草莓脆皮雞蛋糕",
        "productImage": url+"/image",
        "productInfo": "清甜的草莓味, 在口中爆出芬芳的味道, 這就是愛情的味道",
        "productPrice": 60
    }
    ,
    {
        "productID": 3,
        "productName": "抹茶脆皮雞蛋糕",
        "productImage": url+"/image",
        "productInfo": "帶點苦味的抹茶, 像極了初戀",
        "productPrice": 60
    }
    ,
    {
        "productID": 4,
        "productName": "香草脆皮雞蛋糕",
        "productImage": url+"/image",
        "productInfo": "基本款香草口味, 就像是對愛情的忠貞一樣, 始終如一",
        "productPrice": 60
    }]


@app.get("/")
async def home():
    return "Hello FastAPI"


@app.get("/foodInfo")
async def food_info():
    return FoodData


@app.get("/image")
async def image():
    fileName = "/Users/fredfu/Documents/PythonCode/Python/Code/EEGAPIServer/ImageData/1pic.png"
    return FileResponse(fileName, filename="pic1.png")


@app.get("/imageGIF")
async def image():
    fileName = "/Users/fredfu/Documents/PythonCode/Python/Code/EEGAPIServer/ImageData/337078.gif"
    return FileResponse(fileName, filename="pic2.gif")
