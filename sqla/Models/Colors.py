from pydantic import BaseModel

class Color(BaseModel):
    red: str = "red"
    yellow: str = "yellow"
    green: str = "green"