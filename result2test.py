# parse result.json and read every telegram poll
# and write it to test.json

import json

file = open("result.json", "r", encoding="utf-8")

# read json file
data = json.load(file)

from fpdf import FPDF
  
# save FPDF() class into a 
# variable pdf
pdf = FPDF()
  
# Add a page
pdf.add_page()
  
# set style and size of font 
# that you want in the pdf
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 9)
  
# create a cell
pdf.cell(200, 10, txt = "Tests telegram", 
         ln = 1, align = 'C')

question_index = 0
# iterate over every poll
for message in data["messages"]:

    if message["type"] == "message" and "poll" in message:
        print("Poll: " + message["poll"]["question"])
        # write poll to  pdf
        question  = str(question_index+1) + ") " + message["poll"]["question"]
        question_index += 1

        # make text to fit in the width of the page
        pdf.multi_cell(0, 5, question)
        pdf.ln(5)
        # iterate over every option

        # pdf.cell(200, 10, txt = question, ln = 1, align = 'C')
        # iterate over every option
        for index, answer in enumerate(message["poll"]["answers"]):
            option = str(index+1) + ") " + answer["text"]
            # write option to pdf
            pdf.cell(200, 5, txt = option, ln = 1, align = 'C')
        pdf.ln(5)
        
# save pdf
pdf.output("test.pdf")