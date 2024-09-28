
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import article
#if not having these libs  then
#pip install nltk
#pip install textblob
#on top
def summarize():
   pass
url = utext.get('1.0',"end").strip()


article = Article(url)

article.download()
article.parse()

article.nlp()

title.config(state = 'normal')
author.config(state = 'normal')
publication.config(state = 'normal')
summary.config(state = 'normal')
sentiment.config(state = 'normal')

title.delete('1.0','end')
title.insert('1.0',article.title)

author.delete('1.0','end')
author.insert('1.0',article.author)

publication.delete('1.0','end')
publication.insert('1.0',article.publish_date)

summary.delete('1.0','end')
summary.insert('1.0',article.summary)

# A SIMPLE PROGRAM FOR OUR PROJECT IS READY TILL LINE 11,BUT SINCE NEXGENAI DEMANDS MORE,
analysis = TextBlob(article.text)
sentiment.delete('1.0','end')
sentiment.insert('1.0',f'Polaruty:{analysis.polarity},Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


title.config(state = 'disable')
author.config(state = 'disable')
publication.config(state = 'disable')
summary.config(state = 'disable')
sentiment.config(state = 'disable')

# A SIMPLE PROGRAM FOR OUR PROJECT IS READY TILL LINE 11,BUT SINCE NEXGENAI DEMANDS MORE,

# BUILDING A GRAPHIC USER INTERFACE

root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200 x 600')


tlabel = tk.Label(root, text='title')
tlabel.pack()

tlabel = tk.Text(root, height = 1, width = 140)
title.config(state = 'disabled',bg = '')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height = 1, width = 140)
author.config(state = 'disabled',bg = '')
author.pack()

plabel = tk.Label(root, text='Publishing date')
plabel.pack()

publication = tk.Text(root, height = 1, width = 140)
publication.config(state = 'disabled',bg = '')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

Summary = tk.Text(root, height = 20, width = 140)
Summary.config(state = 'disabled',bg = '')
Summary.pack()

salabel = tk.Label(root, text='Sentiment Analysis')
salabel.pack()

sentiment = tk.Text(root, height = 1, width = 140)
sentiment.config(state = 'disabled',bg = '')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height = 1, width = 140)
utext.pack()

btn = tk.Button(root,text = 'Summarize' ,command=summarize)
btn.pack()




root.mainloop()
#kindly note that that all libs should be in your system to run the code (Newspaper3k specific)

