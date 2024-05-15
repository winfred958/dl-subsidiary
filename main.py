import os

from fastapi import FastAPI

from config.global_config import GlobalConfig
from route.cv import cv

app = FastAPI()

app.include_router(cv, prefix="/cv", tags=["图片处理"])

if __name__ == '__main__':
    import uvicorn

    config = GlobalConfig()
    # 使用 GPU 0
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    os.environ["MODELSCOPE_CACHE"] = config.local_cache_dif

    uvicorn.run(app, host='0.0.0.0', port=config.http_port)
