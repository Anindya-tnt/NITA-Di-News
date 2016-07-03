import re
import urllib
from bs4 import BeautifulSoup
from Tkinter import *
import webbrowser
import functools
import random
from tkMessageBox import *

#function for event handling
def callback(event, param):
    webbrowser.open_new(param)

def mainlogic(data):
    
    #searching for the pattern which appears before the unordered list of news
    start = re.search("<!--YOUR SCROLL CONTENT HERE-->",data)
    #startpoint of where search is successful
    stpoint = start.start()
    #updating data with only the parts required
    data = data[stpoint:]
    #searching for the end tag of unordered list
    end = re.search("<ul>",data)
    #noting the position of the </ul> tag
    endpoint = end.start()
    #setting start point for updating data
    stpoint = endpoint
    #further narrowing down data
    data = data[stpoint:]
    #setting endpoint
    endpoint = re.search("</ul>",data).end()
    #final data
    data = data[:endpoint]
    #parsing data as soup object
    soup = BeautifulSoup(data,"html.parser")
    #dictionary to be updated with the news and correspoding hyperlinks
    news = []
    links = []
    link_pat = u'href=(.*) '
    #finding all p tags
    li = soup.find_all("p")
    #adding the news to final_news
    for item in li:
        ifound = str(item).split("</a>")
        if len(ifound) == 2:
            #print ifound[1],ifound[0]
            links.append(re.findall(link_pat,ifound[0])[0].strip('"'))
            news.append(ifound[1][:len(ifound[1])-4])
    #dislaying final_news
    for i in range(len(news)):
        #set full URL to refer to
        URL = "www.nita.ac.in/"+str(links[i])
        #individual elements of the full URL
        URLsplit = URL.split("/")
        #to display only the doc name
        justDoc = URLsplit[len(URLsplit)-1]
        link = Label(root,bg = "light green", text=str(news[i]), font = "Helvetica 12 bold",fg="blue", cursor="hand2")
        link.pack()
        #bind action to mouse button 1 click event
        link.bind("<Button-1>", functools.partial(callback, param=URL))
        theLabel = Label(root,bg = "light green",text="_"*200)
        if not(i==len(news)-1):
            theLabel.pack()

    theLabel = Label(root,bg = "light green",text="\n")
    theLabel.pack()    

#initialize window
class ABC(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()     
root = Tk()
root.config(bg='lightgreen')
app = ABC(master=root)
app.master.title("NITA NEWS AT THIS INSTANT")

#messages to display when data is not available
funStrings = ["Data not available. Must be something fishy with the Internet!",
              "Eh, you sure you are connected to the Internet?",
              "This has got to be one of those Internet issues.",
              "Either your net is down or the server you looked up.",
              "Could not communicate with server. Make sure you are connected.",
              "My mom always told me to connect to the Internet before using this app.",
              "Rainy days and no network always gets me down.",
              "Ain't no Internet, ain't no news!",
              "Ever wonder why a network app does not work sometimes?",
              "Far far away a server resides, and you have got no connection to it.",
              "Some people turn on the net before using this app. Nearly all people do."]
#home page of nita
url = "http://www.nita.ac.in/index.html"

try:
    #html of the home page
    data = urllib.urlopen(url).read()
    #since data is available we can proceed
    mainlogic(data)
except:
    root.withdraw()
    #logic to display error info when data is not available
    toprint = funStrings[random.randint(0,len(funStrings)-1)]
    '''theLabel = Label(root,text=toprint)
    theLabel.pack()
    Button(text='Quit', command=callback).pack(fill=X)'''
    showinfo('NITA NEWS AT THIS INSTANT', toprint)
#tkinter event loop
root.mainloop()

