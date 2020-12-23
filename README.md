# GE-SRTP Input Fuzzer
A fuzzer for testing GE's Service Request Transport Protocol (SRTP), which is an industrial protocol native to their FANUC/Intelligent Platforms PLCs. Documentation on this protocol are not made public by GE, but anyone with a computer, WireShark, and a GE FANUC PLC can disect requests from HMI to the PLC and visa versa.

[GE-SRTP Research Paper](https://www.sciencedirect.com/science/article/pii/S1742287617301925). 

This tool has 4 modes:
1. Dumb Fuzz - Fuzzing performed with no consideration to the SRTP convention. Byte randmization with no care to what byte space it is.
2. Smart Fuzz - Fuzzing performed with consideration to the SRTP convention, ensuring dynamic byte spaces are being randomized.
3. Atomic Bomb Fuzz - Fuzzing using mutational randomization capabilities of [PyRadamsa](https://pypi.org/project/pyradamsa/) (a python module that calls [libradamsa](https://github.com/andreafioraldi/libradamsa) methods from within Python, allowing one to perform mutations on byte blocks, a.k.a. Fuzzing)
4. Raw Input - Handles raw input in form of hexstring, which lets you test specific inputs. (I.e. : 02005979000000000001000000000000000100000000000000000000000058c000000000200a000001010454060001000000000000000000). Use of this mode is intended for replaying any captured requests.
## Setup: ##
`pip3 install -r requirements.txt`
## Use: ##
Running this module in it's various modes has the same convention. 
`python3 srtpFuzz.py $TARGET_IP $TARGET_PORT $TYPE $RUNS`
### Modes ###
#### - Dumb
Type = `d`
` python3 srtpFuzz.py 0.0.0.0 18245 d 100000 `
#### - Smart
Type = `s`
` python3 srtpFuzz.py 0.0.0.0 18245 s 100000 `
#### - Atomic
Type = `a`
` python3 srtpFuzz.py 0.0.0.0 18245 a 100000 `
#### - Raw Input
Type = `r`
` python3 srtpFuzz.py 0.0.0.0 18245 r 100000 `

### Output ###
#### Save to File ####
Appending `>> $FILENAME` to any of the above run commands will save it to a file of your choice.
E.g.
`python3 srtpFuzz.py 0.0.0.0 18245 d 100000 >> DumbfuzzyWuzzy-Output_12-22-20.txt`
#### Responses ####
- Successful responses are returned with **x03** as the first byte (byte[0])
- Errors are returned with **x05** as the first byte (byte[0])
- Initial connection replies start with **x01** as the first byte (byte[0])
#### Standard ####
```
##################
FUZZ RUN: 1000
##################
ESTABLISHING CONNECTION TO 0.0.0.0:18245... SUCCESSFULLY CONNECTED TO 0.0.0.0:18245
SENDING INIT_MSG to 0.0.0.0:18245

b'\x01\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
INIT RESPONSE: 01 00 00 00 00 00 00 00 0f... (DISPLAYING 7 OF 56 BYTES)
INIT SUCCESSFUL
SENDING COMMAND TO 0.0.0.0
RECEIVED REPLY
PLC COMPLETE REPLY: 
b'\x05\x002\xf3\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

PLC STATUS CODES (42,43): 0x00 0x00
REGISTER DATA (HEX): 00

TIMESTAMP: 2020-12-18 12:27:10.475807
FUZZ BYTESTRING: 
b'\xd682\xf3IV\xc0Q\x95]\x01\xbf)\xa2\xbc\xfd^\x10[x\xa55\x11C\xe9\x07F<\xe4\x19\x0cH&\x03}\xd0\x92X\x0c3\xeb\x00X:v\xe0\x9b\xdb\x93\xb6K2\xd4y
\xe3$'

CONNECTION CLOSED
```