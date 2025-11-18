from gtts import gTTS

text = """
Washington Sundar faced more balls across two innings in Kolkata than anyone on either side, and was the only batter to go past the 50-ball mark twice. 
And he did this with a control percentage of 88.51.He did this at No. 3, having walked in inside the first ten overs of both innings, on a pitch where 
the ball was at its worst behaviour when it was new and hard.He did this while batting at No. 3 for the first time in his Test career
"""
tts = gTTS(text)
tts.save("output.mp3")

print("Audiobook created successfully!")
