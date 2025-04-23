import aiohttp

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0'

async def get(url):
    headers = {'user-agent': USER_AGENT}

    async with aiohttp.ClientSession().get(url, headers=headers) as resp:
        return await resp.json()
