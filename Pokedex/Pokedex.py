from tkinter import *
import speech_recognition as sr
import pyttsx3
from PIL import Image ,ImageTk
import requests
from io import BytesIO
import pypokedex



window = Tk()
window.title('Pokedex')
window.geometry('1290x1290')

label1 = Label(window, text="Pokedex", fg="green", pady=30, font=('Helvetica',60))
label1.pack()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

def search():


    pokemon = pypokedex.get(name=pokemon_input)
    pokemon_types = [type for type in pokemon.types]
    pokemon_abilities = [Ability.name for Ability in pokemon.abilities]
    pokemon_Id = pokemon.dex
    pokemon_Weight = pokemon.weight/10
    pokemon_Height = pokemon.height*10

    try:

        speak(pokemon.name)
        speak(f"Id = {pokemon_Id}")
        speak(f"Height = {pokemon_Height}")
        speak(f"Weight = {pokemon_Weight}")
        speak(f"Types = {pokemon_types}")
        speak(f"Abilities = {pokemon_abilities}")



        response = requests.get(pokemon.sprites.front.get('default'))
        image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        pokemon_image.config(image=image)
        pokemon_image.image = image

    except AttributeError:
        pokemon_image.config(image='')


pokemon_input = takecommand()

pokemon_image = Label(window)
pokemon_image.pack(pady=200)


if __name__ == "__main__":
    search()
window.mainloop()

