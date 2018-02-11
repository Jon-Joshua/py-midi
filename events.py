def _process(file, event, track):

    if event == 0x8:
        pass
    elif event == 0x9:
        pass
    elif event == 0xA:
        pass
    elif event == 0xB:
        pass
    elif event == 0xC:
        meta_data = _read_byte(file)
        # print(meta_data)
        track.instrument = meta_data
    elif event == 0xD:
        pass
    elif event == 0xE:
        pass

def _read_byte(file):
    return int(file.read(1).hex(), 16)