import os

from fastapi import APIRouter, Depends, UploadFile, File

from config.global_config import GlobalConfig
from entity.BaseResponse import BaseResponse
from service.cv2textService import CV2NLPService

cv = APIRouter()


@cv.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


config = GlobalConfig()

@cv.post('/image2text')
def cv2nlp(file: UploadFile = File(...), service: CV2NLPService = Depends(CV2NLPService)):
    response = BaseResponse()
    file_name = file.filename

    # 临时目录创建
    local_tmp_dir = config.local_tmp_dir
    if not os.path.exists(local_tmp_dir):
        os.makedirs(local_tmp_dir)

    local_file_path = os.path.join(local_tmp_dir, file_name)
    with open(local_file_path, "wb") as local_file:
        local_file.write(file.file.read())
        data = service.image2Text(local_file_path)
        response.success(data)
    # 清理文件
    if os.path.exists(local_file_path):
        os.remove(local_file_path)
    return response
