from fastapi import FastAPI, HTTPException, status
import asyncio
from pydantic import BaseModel
import uvloop
from utils.browser_use import get_house_urls
from utils.helpers import replace_space_with_plus

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = FastAPI()


class SearchParams(BaseModel):
    name: str
    code: str

@app.get("/")
async def hello():
    return {"message": 'hello'}


@app.post("/api/get_url/")
async def get_url(searchParams: SearchParams):
    if not searchParams.name or not searchParams.code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing region name or code"
        )
    # location_url = f"https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation={region.name}&useLocationIdentifier=true&locationIdentifier=REGION%5E{region.code}&radius=0.0&_includeSSTC=on&includeSSTC=false"
    postcode_url = f"https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation={replace_space_with_plus(searchParams.name)}&useLocationIdentifier=true&locationIdentifier=POSTCODE%5E{searchParams.code}&radius=0.0&_includeSSTC=on&includeSSTC=false"
    result = await get_house_urls(postcode_url)
    return {"status": "success", "result": result, "status_code": status.HTTP_200_OK}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
