import openai

def getInfomation(topic, language, api_key):
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": 
            f"""Write me everything important about the topic {topic}. I am going to use it for my powerpoint presentation.
                Format the output like following:
                Divide all the information into subtopics and under every subtopic add the relevant information as multiple very short bullet points. Not more then 6 words.
                All in {language}"""}
    ]
    )
    return completion.choices[0].message.content