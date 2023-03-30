import collections.abc
from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.util import Pt
import helper
import ai

#Preferences:
topic = "TOPIC"
author = "AUTHOR"
language = "LANGUAGE" #example english, german
api_key = "API-KEY" #https://platform.openai.com/account/api-keys

#create the presentation:
prs = Presentation()

#title slide:
title_slide = helper.add_slide(prs, 0)
helper.change_title(title_slide, topic, textlayout=helper.Textlayout(68, "Dubai", PP_ALIGN.CENTER))
title_slide.placeholders[1].text = f"By {author}"

#content slides:
raw_data = ai.getInfomation(topic, language, api_key)
print(raw_data)
print("Got data")

lines = raw_data.strip().split("\n")
data = ""
headline = ""

for line in lines:
	if "-" not in line and ":" in line or ("." in line and any(chr.isdigit() for chr in line)):
		#add a slide for each topic:
		slide = helper.add_slide(prs, 1)
		helper.change_title(slide, headline, textlayout=helper.Textlayout(48, "Dubai", PP_ALIGN.LEFT))
		slide.placeholders[1].text = data.strip()
		slide.placeholders[1].text_frame.paragraphs[0].font.size = Pt(32)
		data = ""

		headline = line.replace(":", "")
		continue

	data = data + line + "\n"

prs.save(f"{topic}.pptx")