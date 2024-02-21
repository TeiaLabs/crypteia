class ToBytes:
    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    def __call__(self, data: str) -> bytes:
        return data.encode(self.encoding)


class ToString:
    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    def __call__(self, data: bytes) -> str:
        return data.decode(self.encoding)
