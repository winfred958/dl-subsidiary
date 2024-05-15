class GlobalConfig:
    def __init__(self):
        self.http_port = 16666
        # 模型本地缓存路径
        self.local_cache_dif = f"/data/modelscope/cache"
        # 上传的文件临时目录
        self.local_tmp_dir = f"/tmp/images/tmp"
