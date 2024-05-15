import http
import os
from urllib.request import Request

from fastapi import FastAPI
from starlette.responses import JSONResponse

from config.global_config import GlobalConfig
from entity.BaseResponse import BaseResponse
from route.cv import cv

app = FastAPI()

app.include_router(cv, prefix="/cv", tags=["图片处理"])


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, e: Exception):
    """
    全局异常处理
    """
    response = BaseResponse()
    response.error(str(e))
    return JSONResponse(
        status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        content=response.__dict__
    )


if __name__ == '__main__':
    import uvicorn

    config = GlobalConfig()
    # 使用 GPU 0
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    os.environ["MODELSCOPE_CACHE"] = config.local_cache_dif

    uvicorn.run(app, host='0.0.0.0', port=config.http_port)
