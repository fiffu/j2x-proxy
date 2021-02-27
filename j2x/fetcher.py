import aiohttp


async def get(url):
    async with aiohttp.ClientSession().get(url) as resp:
        return await resp.json()
