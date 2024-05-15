class CV2NLPEntity:
    # 算法标识, 无实际意义
    key: str = ''
    # 文本内容
    value: str = ''
    # 算法描述
    description: str = ''

    def __init__(self, key: str = None, value: str = None, description: str = None):
        self.key = key
        self.value = value
        self.description = description
