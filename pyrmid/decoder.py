import struct
import io
from pyrmid.midifile import MidiFile, MidiTrack, MidiEvent
import pyrmid.events as events
import pyrmid.midiutil as midiutil

class Pyrmid:

    def __init__(self, file):
        self.file = file
        self.running_event = None
        self.running_status = False


    def read(self):
        byte_s = io.BytesIO(self.file.read())
        format, tracks, division = self._read_header(byte_s)
        midi_file = MidiFile(format, division)
        tracks_l = self._get_tracks(self.file, tracks)

        for x in tracks_l:
            track = self._read_track(x)
            midi_file.tracks.append(track)
        
        return midi_file


    def _read_header(self, file):
        header, length = midiutil._get_chunkb(file)

        if header != b'MThd':
            raise EOFError

        data = midiutil._read_bytes(file, length)
        return struct.unpack('>3h', data)


    """ Gets track from 'MTrk' start to 0xFF 0x2F 0x00 end. 
        Ugly as hell... Need to change this as soon as I can be bothered.
    """
    def _get_tracks(self, file, tracks):

        tracks_list = []

        for x in range(tracks):
            mtrk_bytes = []

            start = None
            end = None

            file.seek(0)
            cycle = 0

            while True:
                if start == None:
                    byte = file.read(1)

                    if len(mtrk_bytes) == 4:
                        mtrk_bytes.pop(0)
                    mtrk_bytes.append(byte)

                    if b''.join(mtrk_bytes) == b'MTrk':
                        if x == cycle:
                            start = file.tell() - 4
                        else:
                            cycle += 1
                else:
                    byte = midiutil._read_byte_i(file)

                    if byte == 0xFF:
                        if midiutil._read_byte_i(file) == 0x2F:
                            end = file.tell() + 1
                            break

            length = end - start
            file.seek(start)
            tracks_list.append(io.BytesIO(file.read(length)))

        return tracks_list


    def _read_track(self, bytes):
        header, length = midiutil._get_chunkb(bytes)

        if header != b'MTrk':
            return

        track = MidiTrack()
        start = bytes.tell()

        while True:
            delta = midiutil._read_vlenb(bytes)
            next_val = midiutil._read_byte_i(bytes)

            if next_val == 0xFF: # Meta Event
                track.events.append(self._decode_meta_event(bytes, next_val, delta))
            else:
                track.events.append(self._decode_midi_event(bytes, next_val, delta))
 
            # If current pos - start pos equals specified track length, break.
            eot = (bytes.tell() - start) == length
            if eot:
                break

        return track


    def _decode_midi_event(self, file, value, delta):
        event, channel = value >> 4, value & 0xF

        # List of valid events
        event_l = [ 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE ]

        # If event isn't in list of events process the next event as a continuation of the previous event.
        # Aka Running Status.
        self.running_status = False

        if event not in event_l:
            event, channel = self.running_event
            self.running_status = True
        
        self.running_event = [ event, channel ]

        # If running status seek one back in the file. 
        if self.running_status:
            file.seek(file.tell() - 1)

        message = midiutil._read_bytes_l(file, events.get_event_len(event))

        return MidiEvent(delta, channel, event, message, events.MIDI_EVENT)        


    def _decode_meta_event(self, file, track, delta):
        meta_event = midiutil._read_byte_i(file)
        meta_length = midiutil._read_vlenb(file)
        meta_data = None

        ret_type = events.get_track_event_type(meta_event)

        if ret_type == 'string':
            meta_data = midiutil._read_bytes_s(file, meta_length)
        elif ret_type == 'int':
            meta_data = midiutil._read_bytes_l(file, meta_length)
        elif ret_type == None:
            meta_data = None

        return MidiEvent(delta, meta_event, track, meta_data, events.META_EVENT)
