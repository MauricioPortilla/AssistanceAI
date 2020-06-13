# Instalar:
# py -m pip install SpeechRecognition
# py -m pip install pyttsx3
# py -m pip install pipwin
# py -m pipwin install pyaudio
# py -m pip install pywin32

import speech_recognition as sr, pyttsx3, urllib.request, json, sys

def speak(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()

def userInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        query = r.recognize_google(audio, language="es-MX")
    return query

if __name__ == "__main__":
    speak("Hola, ¿qué deseas hacer? Puedo buscar en wikipedia o hacer una operación matemática.")
    request = userInput().lower()
    if "buscar en wikipedia" in request or "wikipedia" in request:
        speak("De acuerdo, ¿sobre qué quisieras buscar?")
        searchQuery = userInput().lower()
        try:
            wikipediaRequest = json.loads(urllib.request.urlopen(
                "http://localhost:5001/api/v1/wikipedia/" + searchQuery
            ).read())
            speak("Según Wikipedia, " + wikipediaRequest["data"])
        except:
            speak("Lo siento, la función de búsqueda en Wikipedia no está disponible por el momento.")
    elif "operación matemática" in request:
        speak("De acuerdo, ¿qué operación deseas hacer?")
        operation = userInput().lower()
        if operation in ["suma", "resta", "multiplicación", "división"]:
            speak("¿Cuál es el primer número?")
            num1 = userInput().lower()
            speak("¿Cuál es el segundo número?")
            num2 = userInput().lower()
            try:
                operationRequest = json.loads(urllib.request.urlopen(
                    "http://localhost:5000/api/v1/calculator/" + operation.replace("ó", "o") + "/" + num1 + "/" + num2
                ).read())
                if operationRequest["status"] == "success":
                    speak("El resultado es: " + str(operationRequest["data"]))
                else:
                    speak("Lo siento, no pude realizar la operación con estos datos, ya que " + operationRequest["message"])
            except Exception:
                print(sys.exc_info())
                speak("Lo siento, la función de calculadora no está disponible por el momento.")
