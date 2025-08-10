from TTS.api import TTS


tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC",
                                        progress_bar=False)


text = 'A very long time ago, in a far-far away galaxy... Luke Skywalker came back to his home planet, Tatooine, in an attempt to free his friend, Han Solo, from a nasty outlaw - Jabba the Hutt.'


tts.tts_to_file(text=text, file_path="output.wav")