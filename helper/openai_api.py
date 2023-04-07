import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(prompt: str, i) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:

        if i == 0:
            response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "user", "content": prompt} # role: user means we
]
)
            content = response['choices'][0]['message']['content']

        elif i ==1:

            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages =[
                    {"role":"assistant", "content":content},
                    {'role':'user', 'content':prompt}
                ]
            )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ' '
        }
        