from pydantic import BaseSettings

class GlobalConfig(BaseSettings):
    APP_PORT: str
class BrokerSettings(BaseSettings):
    RABBIT_HOST: str
    RABBIT_PORT: str
    RABBIT_USER: str
    RABBIT_PASS: str
    RABBIT_EXCHANGE: str
    RABBIT_QUEUE: str
    RABBIT_ROUTING: str
    RABBIT_VHOST: str
class AppSettings(GlobalConfig,BrokerSettings):
    class Config:
        env_file = ".env"

app_setting = AppSettings()
