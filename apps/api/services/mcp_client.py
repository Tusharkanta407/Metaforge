class MCPClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def ping(self) -> bool:
        return bool(self.endpoint)
