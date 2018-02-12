import sys
sys.path.append(b'C:\Users\Jon\Documents\Projects\py-midi\py-midi')

from main.py-midi.decoder import MidiDecoder


# file = open('runescape-sea shanty 2.mid', 'rb')
file = open('test.mid', 'rb')
midi = MidiDecoder().decode(file)

for x in midi.tracks[1].events:
	print('{: <5} {: <5} {: <6} {}    {}'.format(x.delta, hex(x.event), x.channel, x.message, x.get_name()))
