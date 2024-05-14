class BaseResponse:
    code: int = 0
    message: str = ''
    data: any = {}

    def __init__(self):
        self.code = 0
        self.message = 'OK'

    def success(self, data):
        self.data = data

    def error(self, message):
        self.code = -1
        self.message = message
        self.data = {}
