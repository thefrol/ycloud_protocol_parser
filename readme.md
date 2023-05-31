# Как пользоваться

## Парсинг протоколов
https://functions.yandexcloud.net/<function_id>?protocol_url=https://mosff.ru/player/2060&match_time=80
protocol_url - адрес протокола
match_time - время матча(опционально)

## Парсинг игроков
https://functions.yandexcloud.net/<function_id>?player_url=https://mosff.ru/player/2060
player_url - адрес игрока

## Парсинг команд
https://functions.yandexcloud.net/<function_id>?team_url=https://mosff.ru/team/2044
team_url - адрес игрока

# Тестирование фукции

Чтобы проверить, что все нормально рабортает можно воспользоваться скриптом тестировщиком веб сервиса

    python -m test адрес_фунции

Если все прошло нормально

    > python -m test https://functions.yandexcloud.net/d...on6
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 3.079s

    OK
