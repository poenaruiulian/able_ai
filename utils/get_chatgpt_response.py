from utils.get_all_data_context import get_all_data_context
import openai

from utils.get_prompt import get_prompt


def get_chatgpt_response(user_message: str, datasets, user_location) -> str:


    # Combine the entire datasets into a single context string
    data_context = get_all_data_context(datasets)

    response = openai.ChatCompletion.create(
        model="o1",
        messages=[
            {"role": "system", "content": "Ești un asistent pentru persoane cu dizabilități locomotorii care va incerca sa se gandeasca la cele mai bune raspunsuri pentru el."},
            {"role": "user", "content": get_prompt(user_message, user_location, data_context)},
        ]
    )
    return response.choices[0].message.content
