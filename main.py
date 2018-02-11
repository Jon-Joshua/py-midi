from midi import Midi

file = open('midi n shit/runescape-sea shanty 2.mid', 'rb')
midi = Midi()
midi_file = midi.decode(file)

print(midi_file.tracks[1].title)

# print(midi.header.getlength())

# print('Format: {}'.format(midi.header.getformat()))
# print('Tracks: {}'.format(midi.header.gettracks()))
# print('Divisions: {}'.format(midi.header.getdivision()))

# print(midi.header.getdata())
