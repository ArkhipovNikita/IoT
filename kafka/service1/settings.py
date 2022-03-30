from pydantic import BaseSettings


class KafkaSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'kafka_'

    @property
    def url(self):
        return '{}:{}'.format(self.host, self.port)


class GRPCSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'grpc_'

    @property
    def url(self):
        return '{}:{}'.format(self.host, self.port)


kafka_settings = KafkaSettings()
grpc_settings = GRPCSettings()
