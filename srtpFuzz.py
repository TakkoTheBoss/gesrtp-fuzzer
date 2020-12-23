import os, sys, argparse, datetime, binascii, pyradamsa
from time import sleep
from lib.pySRTP import pySrtp

def raw():
    rad = pyradamsa.Radamsa()
    runs = int(args.runs)
    rcount = 0
    for i in range(runs):
        rcount += 1
        dt = datetime.datetime.now()
        seed = input("Input Raw Input: ")
        #seed = "0300ec7f0a01000000000000000000000002000000000000000000000000eb94200a0000203201a000000a01001800000101ff0220007c01"
        seedHex = bytes.fromhex(seed)
        rfuzz = plc.sendSocketCommand(seedHex)
        foutput = "FUZZ RUN #: " + str(rcount) + "\n" + "TIMESTAMP: " + str(dt) + "\n" + "FUZZ BYTESTRING: \n" + str(seedHex) + "\n"
        print(foutput)
    plc.closeConnection()

def atomic_bomb():
    rad = pyradamsa.Radamsa()
    runs = int(args.runs)
    rcount = 0
    for i in range(runs):
        rcount += 1
        dt = datetime.datetime.now()
        seed = "02005979000000000001000000000000000100000000000000000000000058c000000000200a000001010454060001000000000000000000"
        seedHex = bytes.fromhex(seed)
        fValue = rad.fuzz(seedHex)
        rfuzz = plc.sendSocketCommand(fValue)
        foutput = "FUZZ RUN #: " + str(rcount) + "\n" + "TIMESTAMP: " + str(dt) + "\n" + "FUZZ BYTESTRING: \n" + str(fValue) + "\n"
        print(foutput)
        sleep(0.08)
    plc.closeConnection()

def smart():
    runs = int(args.runs)
    rcount = 0
    for i in range(runs):
        rcount += 1
        dt = datetime.datetime.now()
        rfuzz = plc.srtpSmartFuzz()
        foutput = "FUZZ RUN #: " + str(rcount) + "\n" + "TIMESTAMP: " + str(dt) + "\n" + "FUZZ BYTESTRING: \n" + str(rfuzz) + "\n"
        print(foutput)
        sleep(0.08)
    plc.closeConnection()

def dumb():
    runs = int(args.runs)
    rcount = 0
    for i in range(runs):
        #plc.initConnection()
        rcount += 1
        dt = datetime.datetime.now()
        ts = dt.timestamp()
        rfuzz = plc.srtpDumbFuzz()
        #foutput = "FUZZ RUN #: " + str(rcount) + "\n" + "TIMESTAMP: " + str(dt) + "\n" + "FUZZ BYTESTRING: \n" + str(rfuzz) + "\n"
        foutput = "\n" + "TIMESTAMP: " + str(dt) + "\n" + "FUZZ BYTESTRING: \n" + str(rfuzz) + "\n"
        print(foutput)
        #plc.closeConnection()
        #sleep(0.5)
        sleep(0.08)
    plc.closeConnection()

def main():
    try:
        plc.initConnection()
        #print("SUCCESSFULLY CONNECTED")
        pass
    except Exception as err:
        print("HIGH LEVEL SYSTEM EXCEPTION.")
        print(err)
        return(1)
    if args.type == "s": # Smart Fuzz
        smart()
    elif args.type == "d": # Dumb Fuzz
        dumb()
    elif args.type == "a": # Atomic Fuzz
        atomic_bomb()
    elif args.type == "r": # Raw Input
        raw()

if __name__ == "__main__":
    # Parse Arguments - Global
    parser = argparse.ArgumentParser(description='GE SRTP PLC COMMUNICATION TEST.')
    parser.add_argument(action="store", dest='ip', help='IP address of PLC')
    parser.add_argument(action="store", dest='port', help='Port of PLC')
    parser.add_argument(action="store", dest='type', help='s = Smart Fuzz, d = Dumb Fuzz, a = Atomic Fuzz, r = Raw input')
    parser.add_argument(action="store", dest='runs', help='# of runs to perform')
    #parser.add_argument(action="store", dest='bmsg', help='Message to')
    args = parser.parse_args()
    # Global PLC init
    plc = pySrtp(args.ip, args.port)
    resp = main()
    sys.exit(resp)