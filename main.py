import os

from fastapi import FastAPI

from route.cv import cv

app = FastAPI()

app.include_router(cv, prefix="/cv", tags=["图片处理"])

if __name__ == '__main__':
    import uvicorn

    # 使用 GPU 0
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    os.environ["MODELSCOPE_CACHE"] = "/data/modelscope/cache"

    uvicorn.run(app, host='0.0.0.0', port=6666)
