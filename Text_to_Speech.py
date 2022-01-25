from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
text = '''Twinkle twinkle little star,
            How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
            
            When the blazing sun is gone,
            When he nothing shines upon,
            Then you show your little light,
            Twinkle twinkle all the night.
            
            Then the traveler in the dark
            Thanks you for your tiny spark,
            How could he see where to go,
            If you did not twinkle so?
            
            In the dark blue sky you keep,
            Often through my curtains peep
            For you never shut your eye,
            Till the sun is in the sky.
            
            As your bright and tiny spark
            Lights the traveler in the dark,
            Though I know not what you are,
            Twinkle twinkle little star.'''

# Language in which you want to convert
language = 'en'

speech= gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named

speech.save("test.mp3")
