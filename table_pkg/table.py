class STable:
    def __init__(self, id: str) -> None:
        self.id: str = id
        self.columns: list[dict[str, str]] = []
        self.rows: list = []


    def 