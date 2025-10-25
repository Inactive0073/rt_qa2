from dataclasses import dataclass
from environs import Env

@dataclass
class Config:
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str




env = Env().read_env()
config = Config(
    POSTGRES_DB=env("POSTGRES_DB"),
    POSTGRES_USER=env("POSTGRES_USER"),
    POSTGRES_PASSWORD=env("POSTGRES_PASSWORD"),
)
