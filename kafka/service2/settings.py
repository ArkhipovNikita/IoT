from pydantic import BaseSettings


class KafkaSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'kafka_'

    @property
    def url(self):
        return '{}:{}'.format(self.host, self.port)


kafka_settings = KafkaSettings()
