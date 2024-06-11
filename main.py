from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import (
    # couldn't get async browser working in CLI
    # create_async_playwright_browser,
    create_sync_playwright_browser,
    get_current_page
)
from langchain_community.llms import Ollama
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from config import Config
from models.city import City
from models.forecast import Forecast

CITIES = [
    City(id="BurwoodVIC", display_name="Burwood VIC", code="15"),
    City(id="HornsbyNSW", display_name="Hornsby NSW", code="44"),
]

sync_browser = create_sync_playwright_browser()

def get_pollen_level_for_city(city: City):
    toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
    tools = toolkit.get_tools()

    tools_by_name = {tool.name: tool for tool in tools}
    navigate_tool = tools_by_name["navigate_browser"]
    extract_text_tool = tools_by_name["extract_text"]

    navigate_tool.run({"url": Config.URL}, verbose=Config.VERBOSE)

    # First time you select an option from a state different to the one you are
    # already viewing, it will take you to the default location for that state.
    # Do it again to select the actual location you want to view.
    for _ in range(2):
        get_current_page(sync_browser).content()

        doc = extract_text_tool.run(
            {}, verbose=Config.VERBOSE
        )
        # print(doc)

        llm = Ollama(temperature=0, model="llama3")
        parser = PydanticOutputParser(pydantic_object=Forecast)

        prompt = PromptTemplate(
            template="Answer the user query.\n{format_instructions}\n{query}",
            input_variables=["query"],
            # the definition of the CITIES are provided so that the model can use
            # it to look up the city id
            partial_variables={"format_instructions": f"{parser.get_format_instructions()}. The definition of cities are {CITIES}"}
        )

        chain = prompt | llm
        output = chain.invoke({"query": f"What is today's Grass pollen Forecast for {city.display_name} based on the content provided below? {doc}"})
        forecast = parser.invoke(output)
        return forecast

response = []
for city in CITIES:
    response += [get_pollen_level_for_city(city)]

print(response)

