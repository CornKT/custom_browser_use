# test function get_linkedin_profile
import asyncio
from utils.browser_use import get_linkedin_profile

async def test_get_linkedin_profile():
    name = "John Doe"
    result = await get_linkedin_profile(name)
    print(result)

from utils.browser_use import get_house_urls
async def test_get_house_urls():
    url = "https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=London&useLocationIdentifier=true&locationIdentifier=REGION%5E87490&radius=0.0&_includeSSTC=on&includeSSTC=false"
    result = await get_house_urls(url)
    print(result)

asyncio.run(test_get_house_urls())