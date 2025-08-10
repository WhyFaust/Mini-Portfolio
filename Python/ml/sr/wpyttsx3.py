import pyttsx3


def getVoice(voices):
  for voice in voices:
      if 'ru' in voice.languages[0]:
           return voice




engine = pyttsx3.init()


engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)


voices = engine.getProperty('voices')
ru_voice = getVoice(voices)
print(ru_voice)
engine.setProperty('voice', ru_voice.id)


engine.save_to_file('Давным-давно в далёкой далёкой галактике... Люк Скайвокер вернулся на свою родную планету Татуин, пытаясь вырвать своего друга Хана Соло из рук свирепого бандита Джаббы Хатта', 'output.aiff')


engine.runAndWait()