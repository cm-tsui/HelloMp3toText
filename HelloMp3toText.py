# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install pydub
# Windows Install FFmpeg, https://www.wikihow.com/Install-FFmpeg-on-Windows

import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

recognizer = sr.Recognizer()


def load_chunks(filename):
    long_audio = AudioSegment.from_mp3(filename)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=1700,
        silence_thresh=-17
    )
    return audio_chunks


for audio_chunk in load_chunks('long_audio.mp3'):
    audio_chunk.export("temp", format="wav")
    with sr.AudioFile("temp") as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Chunk : {}".format(text))
        except Exception as ex:
            print("Error occured")
            print(ex)

print("++++++")
