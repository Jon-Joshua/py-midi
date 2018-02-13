META_EVENT = 0
MIDI_EVENT = 1

midi_event = {
    0x8: { 'name': 'note_off', 'length': 2 },
    0x9: { 'name': 'note_on', 'length': 2 },
    0xA: { 'name': 'note_aftertouch', 'length': 2 },
    0xB: { 'name': 'controller', 'length': 2 },
    0xC: { 'name': 'program_change', 'length': 1 },
    0xD: { 'name': 'channel_aftertouch', 'length': 1 },
    0xE: { 'name': 'pitch_bend', 'length': 2 }
}

meta_event = {
    0x0: { 'type': 'string' },
    0x1: { 'type': 'int' },
    0x2: { 'type': 'string' },
    0x3: { 'type': 'string' },
    0x4: { 'type': 'string' },
    0x5: { 'type': 'string' },
    0x6: { 'type': 'string' },
    0x7: { 'type': 'string' },
    0x20: { 'type': 'int' },
    0x2F: { 'type': None },
    0x51: { 'type': 'int' },
    0x54: { 'type': 'int' },
    0x58: { 'type': 'int' },
    0x59: { 'type': 'int' },
    0x7F: { 'type': 'string' }
}


def get_event_name(event, type):
    if type == MIDI_EVENT:
        return midi_event[event]['name']
    # elif type == META_EVENT:
    #     return meta_event[event]['name']


def get_event_len(event):
    return midi_event[event]['length']


def get_track_event_type(event):
    return meta_event[event]['type']
