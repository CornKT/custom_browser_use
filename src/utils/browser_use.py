from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, Controller
import asyncio
from dotenv import load_dotenv

from schemas.region import Region
from schemas.system_prompt import MySystemPrompt

load_dotenv()

config = BrowserConfig(headless=False, disable_security=True)

browser = Browser(config=config)
house_controller = Controller(output_model=Region)


async def get_house_urls(url):
    # task = "Go to rightmove.co.uk and accept cookies if necessary, search 'London' and click on button having text: 'For sale', after load click on 'Search properties', return a list of house full url, the key of list in JSON always 'house_urls'. Each url must have correct format like 'abc.com/123'. REMEMBER: DONT CLICK ON BUTTONS HAVING THE TEXT DIFFERENT THAN WHAT I GIVEN."
    # task = f"Go to {url} and accept cookies if necessary, return a list of house full url, the key of list in JSON always 'house_urls'. Each url must have correct format, example: 'abc.com/123', click 'Next' and get the next page, i need 2 pages. REMEMBER: DONT CLICK ON BUTTONS HAVING THE TEXT DIFFERENT THAN WHAT I GIVEN."
    # scroll down to end page and click 'Next' button to go to next page, get the house url in next page and append to 'house_urls' list, i need 2 pages.
    task_1 = f"""Go to {url} and accept cookies if necessary, get a list of house full url,
        the key of list in JSON always 'house_urls'. Each url must have correct format, example: 'https://abc.com/123',
        Exit and return data.
        REMEMBER: DONT CLICK ON BUTTONS HAVING THE TEXT DIFFERENT THAN WHAT I GIVEN."""
    task_2 = f"""Go to {url} and accept cookies if necessary,
        if the result is empty ("We couldn't find what you're looking for right now"), return an empty list of house full url, the key of list in JSON always 'property_urls'.
        exit and return data.
        the key of list in JSON always 'property_urls'
        if the result is not empty, get a list of house full url,
        the key of list in JSON always 'property_urls'. Each url must have correct format, example: 'https://abc.com/123',
        Exit and return data.
        REMEMBER: THE KEY OF RETURN LIST ALWAY 'property_urls', DONT CLICK ON BUTTONS HAVING THE TEXT DIFFERENT THAN WHAT I GIVEN."""
    agent = Agent(
        browser=browser,
        task=task_2,
        llm=ChatOpenAI(model="gpt-4o-mini"),
        controller=house_controller,
        system_prompt_class=MySystemPrompt,
    )
    history = await agent.run()
    result = history.final_result()
    print(result)
    if result:
        parsed: Region = Region.model_validate_json(result)
        print(parsed)
        return parsed
    else:
        print("No result")
        return {"house_urls": []}


# if __name__ == '__main__':
# 	asyncio.run(get_house_urls())
