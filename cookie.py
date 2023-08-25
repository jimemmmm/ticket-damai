import asyncio

from damai.performer import ApiFetchPerform
from set_cookie import COOKIE

async def make_cookie():
    """滑块"""
    instant = ApiFetchPerform()
    instant.update_default_config(dict(COOKIE=COOKIE))
    response = await instant.build_order('728815643570_1_5221536150253')
    print(response.get("data", {}).get("url"))
    await instant.close()

if __name__ == '__main__':

    asyncio.run(make_cookie())