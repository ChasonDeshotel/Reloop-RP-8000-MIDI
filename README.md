# Reloop-RP-8000-MIDI

Update the LCD screen of the Reloop RP-8000 and Reloop RP-8000 MK2 DJ turntables. Currently only tempo/BPM is supported

## Synopsis

```python
from rp8000 import midi

rp = midi.SysEx('RP8000mk2')
rp.set_tempo(123.4)

# MK1 only - switch the display to BPM
rp.tempo_mode()
```

## MK1 vs MK2

### RP-8000 MK1

You must send a tempo to the turntable before you are able to select "bpm" mode for the display. The tempo is automatically set to '00.0' at object instantiation when the model is set to "RP8000"

### RP-8000 MK2

You must send a startup sequence to the turntable before you are able to select "bpm" mode for the display. This happens automatically at object instantiation when the model is set to "RP8000mk2"

## Acknowledgements

Shouts to [Robert Hart](https://rnhart.net/) for [helping](https://reverseengineering.stackexchange.com/questions/25162/construct-a-number-from-0-999-9-using-5-data-bytes-of-a-midi-sysex-message) with the bitwise maths!

