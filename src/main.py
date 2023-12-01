import asyncio
from time import monotonic

from fastapi import FastAPI

from schemas import TestResponse

app = FastAPI(
    title="Тестовое задание для компании `Форкитех`",
    contact={
        "name": "Смелов Илья",
        "url": "https://github.com/PivnoyFei",
    },
)
lock = asyncio.Lock()


async def work() -> None:
    await asyncio.sleep(3)


@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()

    # Одновременно в этом with может находится только одна корутина
    async with lock:
        await work()

    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
