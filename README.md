# py-midi

Work in progress.

Example:

```python
from decoder import MidiDecoder

file = open('test.mid', 'rb')
midi = MidiDecoder()
midi_file = midi.decode(file)

for x in midi.tracks[1].events:
	print('{: <5} {: <5} {: <6} {}    {}'.format(x.delta, hex(x.event), x.channel, x.message, x.get_name()))

```

Result:

```
0     0x9   0      [72, 64]    note_on
120   0x8   0      [72, 64]    note_off
0     0x9   0      [72, 64]    note_on
120   0x8   0      [72, 64]    note_off
0     0x9   0      [79, 64]    note_on
120   0x8   0      [79, 64]    note_off
0     0x9   0      [79, 64]    note_on
120   0x8   0      [79, 64]    note_off
0     0x9   0      [81, 64]    note_on
120   0x8   0      [81, 64]    note_off
0     0x9   0      [81, 64]    note_on
120   0x8   0      [81, 64]    note_off
0     0x9   0      [79, 64]    note_on
241   0x8   0      [79, 64]    note_off
0     0x9   0      [77, 64]    note_on
120   0x8   0      [77, 64]    note_off
0     0x9   0      [77, 64]    note_on
120   0x8   0      [77, 64]    note_off
0     0x9   0      [76, 64]    note_on
120   0x8   0      [76, 64]    note_off
0     0x9   0      [76, 64]    note_on
120   0x8   0      [76, 64]    note_off
0     0x9   0      [74, 64]    note_on
120   0x8   0      [74, 64]    note_off
0     0x9   0      [74, 64]    note_on
120   0x8   0      [74, 64]    note_off
0     0x9   0      [72, 64]    note_on
241   0x8   0      [72, 64]    note_off
0     0xff  47     None    None
```