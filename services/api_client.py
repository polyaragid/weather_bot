import time
import aiohttp
from aiohttp import ClientError, ClientTimeout

class WeatherClient:
    def __init__(self, api_key_wheater: str, cache_ttl: int = 300, timeout: int = 10):
        self.api_key_wheater = api_key_wheater
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.timeout = timeout  # Таймаут запроса в секундах

        self._wheater_cache: dict[str, tuple[float, dict]] = {}  # city -> (timestamp, data)
        self.cache_ttl = cache_ttl  # Время жизни кэша в секундах

    async def get_weather(self, city: str) -> dict:
        now = time.time()

        # Проверка кэша
        if city in self._wheater_cache:
            ts, data = self._wheater_cache[city]
            if now - ts < self.cache_ttl:
                return data

        try:
            # Создаем клиент с таймаутом
            timeout = ClientTimeout(total=self.timeout)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                try:
                    async with session.get(
                        f"{self.base_url}/weather?q={city}&appid={self.api_key_wheater}"
                    ) as response:
                        data = await response.json()
                        
                        # Сохраняем в кэш
                        self._wheater_cache[city] = (now, data)
                        return data
                        
                except ClientError as e:
                    # Обработка ошибок соединения/таймаута
                    raise Exception(f"Failed to get weather data: {str(e)}")
                    
        except Exception as e:
            # Обработка других исключений
            raise Exception(f"Unexpected error occurred: {str(e)}")
