from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    URL = os.getenv("URL")
    verbose_env = os.getenv("VERBOSE") 
    VERBOSE = verbose_env is not None and verbose_env == "true"
