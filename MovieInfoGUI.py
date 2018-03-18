from tkinter import * 
import json
import urllib.request

api_key = '5b5bb9cac9'

#Command Functions
def getInfo(title, year):
    name = title.replace(' ', '+')
    url = ""
    if(year == "fuck"):
        url = 'http://www.omdbapi.com/?t=' + name + '&plot=short&r=json&tomatoes=true'
    else:
        url = 'http://www.omdbapi.com/?t=' + name + '&y=' + str(year) + '&plot=short&r=json&tomatoes=true'
    obj = urllib.request.urlopen(url)
    data = str(obj.read())
    data = data[2:-1]
    jData = json.loads(data)
    return jData
def getUrl(title, year):
    name = title.replace(' ', '+')
    url = ""
    if(year == "fuck"):
        url = 'http://www.omdbapi.com/?t=' + name + '&plot=short&r=json&tomatoes=true'
    else:
        url = 'http://www.omdbapi.com/?t=' + name + '&y=' + str(year) + '&plot=short&r=json&tomatoes=true'
    return url
 
#Request Info  
def getTitle(jData):
    return jData['Title']
def getYear(jData):
    return jData['Year']
#Display Info
def getAudienceRating(jData):
    return jData['Rated']
def getReleased(jData):
    return jData['Released']
def getRuntime(jData):
    return jData['Runtime']
def getDirector(jData):
    return jData['Director'] 
def getGenre(jData):
    return jData['Genre']
def getPoster(jData):
    return jData['Poster']
def getPlot(jData):
    return jData['Plot']
def getLanguage(jData):
    return jData['Language']
def getRating(jData):
    return jData['tomatoRating']
def getReviews(jData):
    return jData['tomatoReviews']
#Events
def pop(event):
    movieInfo = getInfo(movieTitle.get(), year.get())
    
    movieTitle.delete(0, END)
    year.delete(0, END)
    
    name = getTitle(movieInfo)
    pop = Toplevel()
    pop.title(name)
    
    Label(pop, text="Movie Information").grid(row=0, column=0, columnspan=2, sticky=W, padx=4)

    Label(pop, text="Movie Title:").grid(row=1, column=0, sticky=W, padx=4)
    Label(pop, text=name).grid(row=1, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Release Date:").grid(row=2, column=0, sticky=W, padx=4)
    Label(pop, text=getYear(movieInfo)).grid(row=2, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Rated:").grid(row=3, column=0, sticky=W, padx=4)
    Label(pop, text=getAudienceRating(movieInfo)).grid(row=3, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Release Date:").grid(row=4, column=0, sticky=W, padx=4)
    Label(pop, text=getReleased(movieInfo)).grid(row=4, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Movie Length:").grid(row=5, column=0, sticky=W, padx=4)
    Label(pop, text=getRuntime(movieInfo)).grid(row=5, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Movie Director:").grid(row=6, column=0, sticky=W, padx=4)
    Label(pop, text=getDirector(movieInfo)).grid(row=6, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Movie Genre:").grid(row=7, column=0, sticky=W, padx=4)
    Label(pop, text=getGenre(movieInfo)).grid(row=7, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Movie Language:").grid(row=8, column=0, sticky=W, padx=4)
    Label(pop, text=getLanguage(movieInfo)).grid(row=8, column=1, columnspan=5, sticky=W, pady=4)

    Label(pop, text="Movie Rating:").grid(row=9, column=0, sticky=W, padx=4)
    Label(pop, text=getRating(movieInfo)).grid(row=9, column=1, sticky=W, pady=4)
    Label(pop, text="Out of " + str(getReviews(movieInfo)) + " reviews").grid(row=9, column=2, columnspan=5, sticky=W, pady=4)

def reset(event):
    movieTitle.delete(0, END)
    year.delete(0, END)
    
#Main Window
root = Tk()
root.wm_title("Movies")
Label(root, text="Movie Information by Santiago Uriarte").grid(row=0, column=0, columnspan=5, sticky=W)

Label(root, text="Movie Title").grid(row=1, column=0, columnspan=2, sticky=W, padx=4)
movieTitle = Entry(root)
movieTitle.grid(row=1, column=3, sticky=W, pady=4)

Label(root, text="Movie Year").grid(row=2, column=0, columnspan=2, sticky=W, padx=4)
year = Entry(root)
year.grid(row=2, column=3, sticky=W, pady=4)

resetFields = Button(root, text="Reset")
resetFields.grid(row=3, column=0, columnspan=2, sticky=E+W, pady=4)
resetFields.bind("<Button-1>", reset)

submit = Button(root, text="Submit")
submit.grid(row=3, column=3, sticky=E+W, pady=4)
submit.bind("<Button-1>", pop)

root.mainloop()
