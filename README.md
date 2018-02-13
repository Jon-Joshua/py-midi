# pyrmid

Work in progress do not expect much.

Parses MIDI files and returns a list of tracks with events processed into Delta, Event, Modifier and Message.

## Todo:
```
- Fix header parsing.
- Processing track meta events.
```

## Example

### Code
```python
from pyrmid import Pyrmid

file = open('test.mid', 'rb')
midi = Pyrmid(file)
midi_file = midi.read()

print('{:<6} {:<6} {:<7} {:10} {:<6}'.format('Delta', 'Event', 'Channel', 'Message')
for x in midi.tracks[1].events:
	print('{:<6} {:<6} {:<7} {:10} {:<6}'.format(x.delta, hex(x.event), x.channel, repr(x.message)))
```

### Result

```
Delta  Event  Channel Message
0      0x9    0       [72, 64]
120    0x8    0       [72, 64]
0      0x9    0       [72, 64]
120    0x8    0       [72, 64]
0      0x9    0       [79, 64]
120    0x8    0       [79, 64]
0      0x9    0       [79, 64]
120    0x8    0       [79, 64]
0      0x9    0       [81, 64]
120    0x8    0       [81, 64]
0      0x9    0       [81, 64]
120    0x8    0       [81, 64]
0      0x9    0       [79, 64]
241    0x8    0       [79, 64]
0      0x9    0       [77, 64]
120    0x8    0       [77, 64]
0      0x9    0       [77, 64]
120    0x8    0       [77, 64]
0      0x9    0       [76, 64]
120    0x8    0       [76, 64]
0      0x9    0       [76, 64]
120    0x8    0       [76, 64]
0      0x9    0       [74, 64]
120    0x8    0       [74, 64]
0      0x9    0       [74, 64]
120    0x8    0       [74, 64]
0      0x9    0       [72, 64]
241    0x8    0       [72, 64]
0      0xff   47      None
```