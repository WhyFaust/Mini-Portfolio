from vosk import Model, KaldiRecognizer
import wave
import json
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import wave
import json


def initial_convert(filename):
   audio = AudioSegment.from_file(filename)


   audio = audio.set_channels(1)  # Преобразуем в моно
   audio = audio.set_frame_rate(16000)  # Устанавливаем частоту дискретизации на 16000 Гц
   audio = audio.set_sample_width(2)  # Устанавливаем ширину выборки (16 бит)


   audio.export(f'{filename.split(".")[0]}_converted.wav', format='wav')


   # Проверяем параметры сохранённого файла
   # audio = AudioSegment.from_file(output_file)
   # print(f"Каналы: {audio.channels}, Частота: {audio.frame_rate}, Ширина выборки: {audio.sample_width * 8} бит")


model = Model('vosk-model-small-ru-0.22')
rec = KaldiRecognizer(model, 16000)
initial_convert("input_good.wav")
wf = wave.open("input_good_converted.wav", "rb")


full_text = []
while True:
  data = wf.readframes(4000)
  if len(data) == 0:
      break
  if rec.AcceptWaveform(data):
      result = rec.Result()
      text = json.loads(result)["text"]
      full_text.append(text)
      print(full_text)


result = rec.FinalResult()
text = dict(json.loads(result))["text"]
full_text.append(text)
final_text = " ".join(full_text)
print("Полный распознанный текст:")
print(final_text)