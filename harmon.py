from music21 import converter, chord, harmony, scale

# Load the MusicXML content
file_path = 'music_goblin.xml'  # Change to your actual file path
score = converter.parse(file_path)

# Analyze the key
key = score.analyze('key')
print(f'Detected Key: {key.tonic.name} {key.mode}')

# Create a scale object from the key
scale_obj = scale.ConcreteScale(pitches=key.getPitches())
print(f'Scale Pitches: {scale_obj.pitches}')  # Debug print

# Define the cycling pattern for the scale degrees
degree_pattern = [1, 3, 5, 2, 4]
degree_index = 0  # To keep track of the position in the degree_pattern

def get_next_chord():
    global degree_index
    # Get the current degree from the pattern
    degree = degree_pattern[degree_index]
    
    # Get the pitch for the scale degree
    pitch = scale_obj.pitchFromDegree(degree)
    
    # Form a chord by adding intervals (third and fifth) to the pitch
    third = pitch.transpose('m3')  # Major third
    fifth = pitch.transpose('P5')  # Perfect fifth
    chord_pitches = [pitch, third, fifth]
    
    print(f'Chord pitches: {chord_pitches}')  # Debug print
    
    # Move to the next degree in the pattern
    degree_index = (degree_index + 1) % len(degree_pattern)
    return chord.Chord(chord_pitches)


def add_chords_to_score(score):
    # Check if the score has parts
    parts = score.getElementsByClass('Part')
    print(f'Number of parts: {len(parts)}')  # Debug print

    for part in parts:
        measures = part.getElementsByClass('Measure')
        print(f'Number of measures in Part: {len(measures)}')  # Debug print

        for measure in measures:  # Iterate through measures
            print(f'Processing measure: {measure.number}')  # Debug print
            # Get the next chord based on the pattern
            c = get_next_chord()
            print(f'Chord: {c}')  # Debug print
            # Set the duration of the chord (e.g., whole note)
            c.duration.type = 'whole'
            # Add the chord to the measure
            measure.append(c)



# Call the function to add chords to the score
add_chords_to_score(score)

# Save the modified score to a new MusicXML file
new_file_path = 'modified_score.xml'
score.write('musicxml', fp=new_file_path)
