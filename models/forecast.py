from langchain_core.pydantic_v1 import BaseModel

class Forecast(BaseModel):
    city_id: str
    pollen_level: str