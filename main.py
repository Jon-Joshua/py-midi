from midi import Midi

file = open('runescape-sea shanty 2.mid', 'rb')
midi = Midi(file)

# print(midi.header.getlength())

# print('Format: {}'.format(midi.header.getformat()))
# print('Tracks: {}'.format(midi.header.gettracks()))
# print('Divisions: {}'.format(midi.header.getdivision()))

# print(midi.header.getdata())
