# -*- coding: utf-8 -*-
"""llama4_trip_planning_agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FyxaGSTiS9QIJwmAc12tde51T21TxveB
"""

! pip install agno groq

from dotenv import load_dotenv
load_dotenv()



from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.thinking import ThinkingTools

# If you have a travel data tool, you can plug it in similarly.
# For this demo, we're assuming it's reasoning based.

travel_planner = Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[
        ThinkingTools(),
        # Optionally: Add custom TravelTools if available
    ],
    instructions=dedent("""\
    ## General Instructions
    - Always start by using the think tool to map out the steps needed to complete the task.
    - After receiving tool results (or if using general knowledge), use the think tool as a scratchpad to validate the results.
    - Before responding to the user, use the think tool to jot down final thoughts and ideas.
    - Present final outputs in well-organized tables or bullet points when comparing places.

    ## Using the think tool
    At every step, use the think tool as a scratchpad to:
    - Restate the objective in your own words to ensure full comprehension.
    - Identify the user's travel preferences (e.g. adventure, culture, relaxation, etc.)
    - Compare Kathmandu and Pokhara based on relevant factors (scenery, activities, weather, etc.)
    - Check if enough information is available to make a personalized recommendation.
    - Clearly justify the final suggestion to visit either Pokhara or Kathmandu.\
    """),
    show_tool_calls=True,
    markdown=True,
)

# Sample travel planning query
travel_planner.print_response("Plan a trip to Nepal. Compare Kathmandu and Pokhara and suggest which one to visit based on a preference for adventure and natural beauty.", stream=True)

