# Reloop-RP-8000-MIDI

Proof of concept of updating the tempo on the LCD screen on the Reloop RP-8000 and Reloop RP-8000 MK2 DJ turntables

## Synopsis

```python
from rp8000 import midi

rp = midi.SysEx('RP8000mk2')
rp.set_tempo(123.4)

# MK1 only - switch the display to BPM
rp.tempo_mode()
```

## Goals

* Further reverse engieer the RP-8000. How much control is available through MIDI SysEx? How much control is possible through firmware?

* Extract individual deck tempo from Traktor

* Create a full mapping interface into Mixxx

* Decode the time elapsed / time remaining SysEx update messages for MK2

* Decode any other SysEx messages the RP-8000 is sending or receiving

## Updates

MIDI/SysEx updates will be pushed here. I'll also have a RP-8000 page on the Mixxx hardware wiki detailing my findings

## MK1 vs MK2

### RP-8000 MK1

You must send a tempo to the turntable before you are able to select "bpm" mode for the display. The tempo is automatically set to '00.0' at object instantiation when the model is set to "RP8000"

### RP-8000 MK2

You must send a startup sequence to the turntable before you are able to select "bpm" mode for the display. This happens automatically at object instantiation when the model is set to "RP8000mk2"

## Acknowledgements

Shouts to Bavi_H for [helping](https://reverseengineering.stackexchange.com/questions/25162/construct-a-number-from-0-999-9-using-5-data-bytes-of-a-midi-sysex-message) with the bitwise maths!

