FROM python:3
RUN ["/bin/bash", "-c", "apt-get update > /dev/null 2>&1"]
RUN mkdir /app
RUN mkdir /app/app
WORKDIR /app/app
RUN ["/bin/bash", "-c", "apt-get --assume-yes install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "pip3 install pyaudio > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "pip3 install SpeechRecognition > /dev/null 2>&1"]
RUN ["/bin/bash", "-c", "pip3 install pyttsx3 > /dev/null 2>&1"]
CMD ["/bin/bash", "-c", "python client.py"]
