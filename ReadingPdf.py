#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import PyPDF2
book = open('/Users/thenuka/Desktop/ashlee-vance-elon-musk-tesla-spacex-and-the-quest-for-a-fantastic-future.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(5)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()


# In[ ]:





# In[ ]:




