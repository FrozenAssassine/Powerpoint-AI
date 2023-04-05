import openai

def prompt_ai(prompt, api_key):
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

#Get the sub topics to a specific topic
def getTopics(topic, language, api_key):
    msg = f"I have to make a powerpoint about {topic}. Which are the best top-categories. Not more then five to eight points as a list. Only one or two words per point. Please all in {language}"
    #msg = f"Give me five to eight of the most important and generalised topics for a powerpoint presentation about {topic} as bullet points. Only one or two words per point and please in {language}"
    return prompt_ai(msg, api_key).split("\n")

#get all the information to a subtopic 
def getTopicInformations(sub_topic, topic, language, api_key):
    msg = f"Give me the three or four most important informations about {sub_topic} from the main topic {topic} as short bullet points for a powerpoint not more than 8 words. Please all in {language} and in a easy understandable language style"
    return prompt_ai(msg, api_key)