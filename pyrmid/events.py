META_EVENT = 0
MIDI_EVENT = 1

midi_event = [
    { 'event': 0x8, 'name': 'note_off', 'length': 2 },
    { 'event': 0x9, 'name': 'note_on', 'length': 2 },
    { 'event': 0xA, 'name': 'note_aftertouch', 'length': 2 },
    { 'event': 0xB, 'name': 'controller', 'length': 2 },
    { 'event': 0xC, 'name': 'program_change', 'length': 1 },
    { 'event': 0xD, 'name': 'channel_aftertouch', 'length': 1 },
    { 'event': 0xE, 'name': 'pitch_bend', 'length': 2 },
]

meta_event = [
    { 'event': 0x0, 'type': 'string' },
    { 'event': 0x1, 'type': 'int' },
    { 'event': 0x2, 'type': 'string' },
    { 'event': 0x3, 'type': 'string' },
    { 'event': 0x4, 'type': 'string' },
    { 'event': 0x5, 'type': 'string' },
    { 'event': 0x6, 'type': 'string' },
    { 'event': 0x7, 'type': 'string' },
    { 'event': 0x20, 'type': 'int' },
    { 'event': 0x2F, 'type': None },
    { 'event': 0x51, 'type': 'int' },
    { 'event': 0x54, 'type': 'int' },
    { 'event': 0x58, 'type': 'int' },
    { 'event': 0x59, 'type': 'int' },
    { 'event': 0x7F, 'type': 'string' },
]


def get_event_name(event, type):
    if type == MIDI_EVENT:
        for e in midi_event:
            if e['event'] == event:
                return e['name']


def get_event_len(event):
    for e in midi_event:
        if e['event'] == event:
            return e['length']


def get_track_event_type(event):
    for e in meta_event:
        if e['event'] == event:
            return e['type']
