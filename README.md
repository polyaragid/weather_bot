## weather_bot

## Участники проекта

1. Глаголева Полина Денисовна 465540
2. Котуранова Мария Сергеевна 408879

## О проекте

Асинхронный телеграмм бот, показывающий погоду. 

## Инструкцию по запуску

1. Скачать проект из гитхаба
2. Скачать модули(requirements.txt)
3. Разархивировать его
4. Получить токен для получения данных о погоде на [сайте](https://home.openweathermap.org/users/sign_in) 
5. Create an Account заполняете данные -> кликаете справа сверху на имя аккаунта(рядом с Support) -> My api keys -> создаёте ключ
6. Получить токен телеграмм бота в botfather
7. Создать .env файл в папке внутри проекта config/
8. Вставить в .env файл

telegram-api-key="Токен тг бота"

api-key-weather="Токен погоды openweathermap"

admins=[id(int)]

9. Запустить bot.py
