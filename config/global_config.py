class GlobalConfig:
    http_port = 16666
    # 模型本地缓存路径
    local_cache_dif = f"/data/modelscope/cache"
    # 上传的文件临时目录
    local_tmp_dir = f"/tmp/images/tmp"

    def __init__(self):
        pass
