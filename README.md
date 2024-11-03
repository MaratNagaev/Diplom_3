## Дипломный проект. Задание 3: веб-приложение


Проект по автоматизации UI-тестов для сервиса Stellar Burgers
`https://stellarburgers.nomoreparties.site/` 
 ---

Перед работой с репозиторием требуется установить зависимости: 
```
pip install -r requirements.txt
```
Запустить тесты:
```
pytest tests --alluredir=allure_results
```
Просмотреть отчет о тестировании:
```
allure serve allure_results
```
