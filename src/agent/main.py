from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os

def firstagent():
    load_dotenv()
    set_tracing_disabled(True)
    
    provider = AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash-exp",
        openai_client=provider,
    )
    
    Agent1 = Agent(
        name="Translator",
        instructions="""
You are a translator. Translate the given text (which can be in any language including Urdu) into the following 10 languages: English, French, Spanish, German, Chinese, Arabic, Russian, Hindi, Japanese, Italian.
Provide the output in a clear format showing each language and its translation.
""",
        model=model
    )
    
    # User se input lene ke liye:
    input_text = input("Apna matn likhein (urdu ya koi bhi zuban): ")
    
    response = Runner.run_sync(
        starting_agent=Agent1,
        input=input_text,
    )
    
    print("\nTranslation in 10 languages:\n")
    print(response.final_output)

# Function call
firstagent()
