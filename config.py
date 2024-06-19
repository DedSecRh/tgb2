# переменные окружения
# python-dotenv нужен для настройки переменных окружения

# Для передачи токена создайте файл .env со следующим содержимым
# TOKEN=ВАШ_ТОКЕН


import os
from dotenv import load_dotenv

# ### Включить для запуска на серевере
# load_dotenv()

# TOKEN: str = os.getenv('TOKEN')
# ### Включить для отладки в replit
TOKEN: str = os.environ['TOKEN']

CLIENT_ID: str = os.getenv('CLIENT_ID')

TOKEN_URL = f'https://oauth.yandex.ru/authorize?response_type=token&client_id={CLIENT_ID}'