import os
from langchain import OpenAI, PromptTemplate, LLMChain

# Set your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')  # This assumes you've set the environment variable

# Alternatively, you can directly set the API key here (less secure)
# api_key = 'your_openai_api_key'

# Initialize your LLM with the API key
llm = OpenAI(model="text-davinci-003", openai_api_key=api_key)

# Define a prompt template with instructions for JSON output
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="""
    Pretend you are a medical school student. 

    Given the following input, generate a response structured as a JSON object:
    Input: {input_text}
    JSON Response:
    """
)

# Create an LLMChain with the prompt template and LLM
chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Example input text
input_text = "Provide a computational phenotype for <INSERT_PHENOTYPE> with codes needed and their name, and logical conditions as well as how many codes are needed. In the following tabular format: Logic (inclusion or exclusion), code vocabulary, code identifier, code name, and code count."

# Run the chain with the input text
result = chain.run(input_text=input_text)

print(result)
