from music21 import stream, note, meter, key, tempo, metadata, configure

#configure.run()
def parse_text_to_notes(text):
    # Mapping of letters to notes or rhythmic values
    note_mapping = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'A#',  # or Bb
        'i': 'C#',  # or Db
        # ... add other mappings
    }
    
    # Define the duration of a rhythmic unit (e.g., '16th' for sixteenth note)
    rhythmic_unit = '16th'
    
    # Initialize an empty list to hold note and rest information
    notes_sequence = []
    
    # Track the count of consecutive non-note letters (for rests)
    non_note_count = 0
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is a note
        if char in note_mapping:
            # If there were non-note characters before this, add a rest
            if non_note_count > 0:
                notes_sequence.append({'type': 'rest', 'duration': rhythmic_unit, 'count': non_note_count})
                non_note_count = 0  # Reset the non-note counter

            # Add the note to the sequence
            notes_sequence.append({'type': 'note', 'pitch': note_mapping[char], 'duration': 'quarter'})  # Assuming quarter note for simplicity
        else:
            # If it's not a note, increment the non-note counter
            non_note_count += 1

    # Check if the text ended with non-note characters
    if non_note_count > 0:
        notes_sequence.append({'type': 'rest', 'duration': rhythmic_unit, 'count': non_note_count})

    return notes_sequence

def parse_text_to_notes_modular(text, scale, rhythm_pattern):
    # Mapping of characters to scale degrees using modular arithmetic
    def char_to_scale_degree(char):
        return ord(char.lower()) % len(scale)
    
    # Mapping count of non-note chars to a rhythm value
    def count_to_rhythm(count):
        return rhythm_pattern[count % len(rhythm_pattern)]
    
    # Initialize an empty list to hold note and rest information
    notes_sequence = []
    
    # Track the count of consecutive non-note letters (for rests)
    non_note_count = 0
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is a note
        if char.isalpha():
            # If there were non-note characters before this, add a rest
            if non_note_count > 0:
                rhythm_value = count_to_rhythm(non_note_count)
                notes_sequence.append({'type': 'rest', 'duration': rhythm_value})
                non_note_count = 0  # Reset the non-note counter

            # Map the character to a scale degree and then to a pitch
            degree = char_to_scale_degree(char)
            pitch = scale[degree]
            notes_sequence.append({'type': 'note', 'pitch': pitch, 'duration': 'quarter'})  # Assuming quarter note for simplicity
        else:
            # If it's not a note, increment the non-note counter
            non_note_count += 1

    # Check if the text ended with non-note characters
    if non_note_count > 0:
        rhythm_value = count_to_rhythm(non_note_count)
        notes_sequence.append({'type': 'rest', 'duration': rhythm_value})

    return notes_sequence


def create_music_xml(notes_sequence, rhythm_structure, filename='file'):
    # Create a music stream
    s = stream.Score(id='mainScore')
    
    # Add metadata (optional)
    s.insert(0, metadata.Metadata())
    s.metadata.title = 'Algorithmic Composition'
    s.metadata.composer = 'Composer Name'

    # Define the time signature and tempo
    ts = meter.TimeSignature('4/4')
    s.append(ts)
    s.append(tempo.MetronomeMark(number=120))  # 120 beats per minute
    
    # Create a part for the notes
    p = stream.Part(id='part1')
    
    for note_info in notes_sequence:
        # Create a Note or Rest object
        if note_info['type'] == 'note':
            n = note.Note(note_info['pitch'])
            n.duration.type = note_info['duration']
           
        elif note_info['type'] == 'rest':
            n = note.Rest()
            n.duration.type = note_info['duration']
        else:
            continue
        
        # Add the note/rest to the part
        p.append(n)

    # Add the part to the score
    s.insert(0, p)

    # Show the music score
    #s.show('musicxml')
    fp = s.write('musicxml', fp=
                 '{filename}.xml')
    print(f'MusicXML written to {fp}')

# Example usage:
'''
notes_sequence = [
    {'type': 'rest', 'duration': 'eighth'},  # representing "Lolol"
    {'type': 'note', 'pitch': 'B', 'duration': 'quarter'},
    {'type': 'note', 'pitch': 'A', 'duration': 'quarter'},
    {'type': 'rest', 'duration': '16th'},  # representing "bl"
    {'type': 'rest', 'duration': '16th'},  # representing "y"
    {'type': 'note', 'pitch': 'A', 'duration': 'quarter'},
    {'type': 'note', 'pitch': 'B', 'duration': 'quarter'},
    {'type': 'note', 'pitch': 'C#', 'duration': 'quarter'},  # Assuming C#/Db is C#
    {'type': 'rest', 'duration': '16th'},  # representing "t"
    {'type': 'note', 'pitch': 'D', 'duration': 'eighth'},
    {'type': 'note', 'pitch': 'C#', 'duration': 'eighth'},  # Assuming C#/Db is C#
    {'type': 'note', 'pitch': 'F', 'duration': 'eighth'},
    {'type': 'note', 'pitch': 'F', 'duration': 'eighth'},
    {'type': 'rest', 'duration': '16th'},  # representing "t"
    {'type': 'rest', 'duration': 'eighth'},  # representing "ype"
    {'type': 'rest', 'duration': 'eighth'},  # representing "o"
    {'type': 'note', 'pitch': 'F', 'duration': 'quarter'},
    {'type': 'note', 'pitch': 'A', 'duration': 'quarter'},
    {'type': 'rest', 'duration': '16th'},  # representing "l"
    {'type': 'note', 'pitch': 'G', 'duration': 'quarter'},
    {'type': 'rest', 'duration': '16th'},  # representing "or"
    {'type': 'rest', 'duration': '16th'},  # representing "i"
    {'type': 'note', 'pitch': 'C#', 'duration': 'quarter'},  # Assuming C#/Db is C#
    {'type': 'rest', 'duration': '16th'},  # representing "t"
    {'type': 'note', 'pitch': 'Bb', 'duration': 'quarter'},  # Assuming A#/Bb is Bb
    {'type': 'note', 'pitch': 'C#', 'duration': 'eighth'},  # Assuming C#/Db is C#
    {'type': 'note', 'pitch': 'C', 'duration': 'eighth'},
    {'type': 'note', 'pitch': 'C', 'duration': 'quarter'},
    {'type': 'rest', 'duration': 'quarter'},  # representing " musi"
    {'type': 'note', 'pitch': 'C', 'duration': 'quarter'},
]
'''

notes_sequence = parse_text_to_notes('Lolol bl yA B C#tD C#FFt ypeoFA lGor iC#tBbC#CC musiC')

create_music_xml(notes_sequence, rhythm_structure=None)


text = "Lolol probably a bit diff type of algorithmic music"
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'D#', 'F#', 'G#', 'A#']  # Chromatic scale
rhythm_pattern = ['16th', 'eighth', 'quarter', 'half']  # Example rhythm pattern
notes_sequence = parse_text_to_notes_modular(text, scale, rhythm_pattern)
#print(notes_sequence)


create_music_xml(notes_sequence, rhythm_structure=rhythm_pattern, filename='music2')
