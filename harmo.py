from music21 import converter, chord, harmony, scale

# Load the MusicXML file
file_path = 'music_goblin.xml'
score = converter.parse(file_path)

# Analyze the key
key = score.analyze('key')
print(f'Detected Key: {key.tonic.name} {key.mode}')

# Create a scale from the key
scale_obj = scale.ConcreteScale(pitches=key.getPitches())

# Define the scale degree pattern
degree_pattern = [1, 3, 5, 2, 4]
degree_index = 0  # To keep track of the position in the degree_pattern

def get_next_chord():
    global degree_index
    degree = degree_pattern[degree_index]  # Get the current degree
    chord_pitches = scale_obj.pitches[(degree - 1) * 2: (degree - 1) * 2 + 3]  # Get the pitches for the chord (1, 3, 5 of the scale degree)
    degree_index = (degree_index + 1) % len(degree_pattern)  # Move to the next degree in the pattern
    return chord.Chord(chord_pitches)

def add_chords_to_score(score):
    for measure in score.measures(1, None):  # Iterate through measures
        c = get_next_chord()
        c.duration.type = 'whole'  # Set the duration of the chord
        measure.append(c)  # Add the chord to the measure

add_chords_to_score(score)

# Save the modified score to a new MusicXML file
new_file_path = 'music_goblin_with_chords.xml'
score.write('musicxml', fp=new_file_path)
