import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# say method on the engine that passing input text to be spoken
engine.say('hello Dande vamshivardhan, pppaaaannndhheega ,sigguleyda ')

# run and wait method, it processes the voice commands.
engine.runAndWait()
