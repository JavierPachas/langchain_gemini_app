from app_key import GEMINI_API_KEY
import os 
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

from langchain.chains import SequentialChain


os.environ['GEMINI_API_KEY'] = GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY)


def generator_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for it. Only one name without description.")

    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = 'restaurant_name')


    prompt_template_menu = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Suggest ten menu items for {cuisine} restaurant called {restaurant_name}. Return it as a comma separated list.")

    food_items_chain = LLMChain(llm = llm, prompt = prompt_template_menu, output_key = 'menu_items')

    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items'])

    response= chain.invoke({'cuisine':cuisine})

    return response



if __name__ == "__main__":
    print(generator_restaurant_name_and_items("Peruvian"))







