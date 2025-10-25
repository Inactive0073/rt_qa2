from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int


env = Env()
env.read_env()
config = Config(
    POSTGRES_DB=env("POSTGRES_DB"),
    POSTGRES_USER=env("POSTGRES_USER"),
    POSTGRES_PASSWORD=env("POSTGRES_PASSWORD"),
    POSTGRES_PORT=env.int("POSTGRES_PORT"),
)
