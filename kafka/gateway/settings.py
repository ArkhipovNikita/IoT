from pydantic import BaseSettings


class HttpSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'http_'


class GRPCSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'grpc_'

    @property
    def url(self):
        return '{}:{}'.format(self.host, self.port)


http_settings = HttpSettings()
grpc_settings = GRPCSettings()
