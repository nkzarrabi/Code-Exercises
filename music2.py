import re
from datetime import datetime
from music21 import stream, note, meter, key, tempo, metadata, configure



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

def create_music_xml(notes_sequence, key_sig, time_sig= '4/4', file_path=None):
    # Create a music stream
    s = stream.Score(id='mainScore')
    
    # Add metadata (optional)
    s.insert(0, metadata.Metadata())
    s.metadata.title = 'Algorithmic Composition'
    s.metadata.composer = 'Composer Name'

    # Define the time signature and tempo
    ts = meter.TimeSignature(time_sig)
    ks = key.KeySignature(key_sig.sharps)
    s.append(ks)
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

    # If no file path is provided, generate one
    if not file_path:
        # Sanitize input text to create a valid file name
        sanitized_text = re.sub(r'\W+', '', text)  # Remove non-alphanumeric characters
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')  # Current timestamp
        file_path = f'{sanitized_text}_{timestamp}.xml'  # Combine sanitized text and timestamp

    # Write the music score to a MusicXML file
    fp = s.write('musicxml', fp=file_path)
    s.show('musicxml')
    print(f'MusicXML written to {fp}')



def get_scale_from_key(key_obj):
    # Assuming key_obj is an instance of music21.key.Key
    return [str(p) for p in key_obj.pitches]

text = 'Lolol probably a bit diff type of algorithmic music'
key_obj = key.Key('d')  # or any other key you want
scale = get_scale_from_key(key_obj)
rhythm_pattern = ['eighth', 'quarter', 'half']

notes_sequence = parse_text_to_notes_modular(text, scale, rhythm_pattern)

create_music_xml(notes_sequence, key_obj, file_path='music_new_w.xml')





#text = 'How do I get my husband to stop going ‘Goblin Mode’ during sex?TLDR; My husband says ‘Goblin Mode activated’ when we start to have sex, growls and acts like a caveman, and then says ‘Goblin Mode off’ when we stop, and then pretends not to remember afterward.'
text = '''
Love's vast ocean, a realm where emotions soar
If words were notes, our love's the score,
The irresistible call of the siren, beckoning evermore
Seas torn asunder, the world from Moussa’s lore.

A heart set sail, without compass or oar
Waves and wind sang to rich and poor
Sirens silence along the shore,
Luring hearts to depths unknown.

A heart sets sail, guided by passion's core
If waves held stories, they'd be ones we’ve sung,
Sirens whisper tales from ancient lore,
Their silence deafening as the nilpotent tongue.

The sea, initially calm beneath the moon's glow
A sailor's tale of work and woe,
Yet within its depths, a storm begins to grow
Transformed by love's enduring glow.

Anticipation rises, a tempestuous flow
Should he resist, or should he bend,
A whirlwind fueled by longing for you, I know
To the maiden's call, where paths extend?

We race against time, the tide, to seize the day
He chose her love, the siren's spell,
The ship of love cannot forever in harbor stay
A harmony he knows so well.

Like rain, we cherish the moments, fleeting though they may be
No longer lost in ocean's foam,
The winds of time, never held at bay
In love and land, he's found his home.'''
key_obj = key.Key('c#')  # or any other key you want
scale = get_scale_from_key(key_obj)
rhythm_pattern = ['eighth', 'quarter', 'half']

notes_sequence = parse_text_to_notes_modular(text, scale, rhythm_pattern)

create_music_xml(notes_sequence, key_obj, time_sig = '3/4', file_path='music_g.xml')