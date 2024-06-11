from langchain_core.pydantic_v1 import BaseModel

class City(BaseModel):
    id: str
    display_name: str
    code: str