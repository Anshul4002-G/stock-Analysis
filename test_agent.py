from agno.agent import Agent
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.5-flash-exec"),
    description="Test",
    instructions=["Do something simple."],
    markdown=True
)
print("Agent created fine")
