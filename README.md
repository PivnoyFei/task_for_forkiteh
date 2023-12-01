<h1 align="center">Тестовое задание для компании "Форкитех"</h1>

### Стек
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.12](https://img.shields.io/badge/3.12-blue?style=flat-square&logo=3.12)
![FastAPI](https://img.shields.io/badge/FastAPI-171515?style=flat-square&logo=FastAPI)![0.104.1](https://img.shields.io/badge/0.104.1-blue?style=flat-square&logo=0.104.1)
![Pytest--asyncio](https://img.shields.io/badge/Pytest--asyncio-171515?style=flat-square&logo=Pytest)

#### Сделать сервис на FastAPI, предоставляющий один метод: ```GET /test```

В качестве полезной работы метод спит 3 секунды:
```bash
async def work() -> None:
    asyncio.sleep(3)
```
#### При этом не допускается одновременная работа нескольких функций work()
#### В качестве овета метод возвращает фактически затраченое время на обработку запроса:
```bash
class TestResponse(BaseModel):
    elapsed: float
```
```bash
@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    ... организация вызовы функции work() ...
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
```
#### Тестирование:
Метод считается успешным, если при одновременном вызове каждый возвращающийся
ответ содержит elapsed отличающийся от предыдущего не менее чем на 3 секунды


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
gh clone https://github.com/PivnoyFei/task_for_forkiteh.git
```
```bash
cd task_for_forkiteh
```
```bash
cd src
```

#### Устанавливаем зависимости:
```bash
poetry install
```

#### Тестируем приложение:
```bash
poetry run pytest
```

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)
