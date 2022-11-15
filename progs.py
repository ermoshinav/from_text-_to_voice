from gtts import gTTS 
from playsound import playsound 
#input string
text_val = 'Dessert is often Christmas Pudding. Mince pies and lots of chocolates are often eaten as well. The dinner table is decorated with a Christmas Cracker for each person and sometimes flowers and candles.'
language='en'
obj=gTTS(text=text_val, lang=language, slow=False)
#save audio
obj.save("audio.mp3")
# play file
playsound("audio.mp3")