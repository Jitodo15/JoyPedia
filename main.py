from tkinter import *
import config
import requests


API_KEY = config.JP_API_KEY
API_HOST = 'wiki-briefs.p.rapidapi.com'


def get_query():

    query = entry.get()

    params = {
        "q": query,
        "topk": 3
    }

    headers = {
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': API_HOST
      }

    try:
        response = requests.get(url='https://wiki-briefs.p.rapidapi.com/search', params=params, headers=headers)
        response.raise_for_status()
        data = response.json()["summary"]

        if not data:
            canvas.delete("some_tag")
            canvas.create_text(350, 250, width=550, text="Search not found. Check for spelling errors.",
                               font=("Arial", 40, "bold"), tags="some_tag")
            canvas.grid(row=3, column=0, columnspan=5)

        else:
            summaries = []
            for item in data:
                summaries.append(item)
            canvas.delete("some_tag")
            canvas.create_text(350, 250, width=550, text="\n\n".join(summaries), font=("Arial", 20), tags="some_tag")
            canvas.grid(row=3, column=0, columnspan=5)

    except requests.exceptions.RequestException as e:
        canvas.delete("some_tag")
        canvas.create_text(350, 250, text="Search not found. Check for spelling errors.", font=("Arial", 20, "bold"), anchor="center", tags="some_tag")

    entry.delete(0, END)


window = Tk()
window.title("JoyPedia")
window.minsize(width=600, height=600)
window.configure(pady=50, padx=50, bg='darkseagreen1')


heading = Label(text="JoyPedia", font=('Verdana', 36, 'bold'), bg='darkseagreen1')
message = Label(text='Enter search', font=('Verdana', 16), bg='darkseagreen1')
entry = Entry(font=('Verdana', 16), width=40)
canvas = Canvas(width=700, height=500, bg="white")
# output = Label(font=('Verdana', 16), bg='darkseagreen1', wraplength=400, justify='left')


search_button = Button(text='Search', font=('Verdana', 16), command=get_query)

heading.grid(row=0, column=1,  columnspan=3, pady=10)
message.grid(row=2, column=0)

entry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
search_button.grid(row=2, column=4)


mainloop()
