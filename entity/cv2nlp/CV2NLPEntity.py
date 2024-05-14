class CV2NLPEntity:
    key: str = ''
    value: str = ''
    description: str = ''

    def __init__(self, key: str = None, value: str = None, description: str = None):
        self.key = key
        self.value = value
        self.description = description
