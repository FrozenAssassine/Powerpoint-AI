import collections.abc
from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.util import Pt
import powerpoint_helper
import ai
import data_cleaner
import image_helper
import os
from pathlib import Path

#Preferences:
topic = "TOPIC"
author = "AUTHOR"
language = "LANGUAGE" #example english, german
api_key = "API-KEY" #https://platform.openai.com/account/api-keys

#create the presentation from a template to get the correct format (16/9):
prs = Presentation("src/pptx-default-16x9.pptx")

#get some images:
current_image_index = 0
image_helper.get_image_topic(topic)
image_list = os.listdir(f"images/{topic}")
print(image_list)
#splashscreen
powerpoint_helper.add_text_slide(prs, topic, f"By {author}")

#content slides:
sub_topics = ai.getTopics(topic, language, api_key)
print("\n".join(sub_topics))

#table of content:
powerpoint_helper.add_text_slide(prs, "Table of content",  data_cleaner.clean_bullet_points("\n".join(sub_topics)))

#loop through the sub topics and create a slide for every topic
count = 0
for sub_topic in sub_topics:
    count = count + 1
    print(f"Slide {count}/{len(sub_topics)}")
    data = ai.getTopicInformations(sub_topic, topic, language, api_key)

    if count % 2 == 1 and current_image_index < len(image_list): #every two slides:
        powerpoint_helper.add_text_slide_with_background(prs, sub_topic, data_cleaner.clean_bullet_points(data), f"images/{topic}/{image_list[current_image_index]}")
        current_image_index = current_image_index + 1
    else:
        powerpoint_helper.add_text_slide(prs, sub_topic, data_cleaner.clean_bullet_points(data))



#sources and end:
powerpoint_helper.add_splash_slide(prs, "Thanks for listening!", "")
powerpoint_helper.add_text_slide(prs, "Sources", "")

[f.unlink() for f in Path(f"images/{topic}/").glob("*") if f.is_file()] 

print("DONE")
prs.save(f"{topic}.pptx")