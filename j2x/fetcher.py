import aiohttp


sess = aiohttp.ClientSession()

async def get(url):
    async with sess.get(url) as resp:
        return await resp.json()
