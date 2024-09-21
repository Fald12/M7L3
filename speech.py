import speech_recognition as speech_recog

def speech():
    mic= speech_recog.Microphone()
    recog= speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise (audio_file)
        audio= recog.listen(audio_file)
        return recog.recognize_google(audio, language="id-ID")
    
# mic= speech_recog.Microphone()
# recog= speech_recog.Recognizer()

# with mic as audio_file:
#     print("silahkan berbicara!")

#     recog.adjust_for_ambient_noise (audio_file)
#     audio= recog.listen(audio_file)

#     print("mengkonversikan ucapan menjadi teks...")
#     print("Kamu berkata " + recog.recognize_google(audio, language="en-GB"))
    