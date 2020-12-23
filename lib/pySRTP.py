import os, sys, re, struct, socket, random
from . import pySRTP_msg
from .pySRTP_msg import ALLBYTES_MSG, ANY_MSG

class pySrtp:
    def __init__(self, ip, port):
        if port == 0:
            self.port = 18245
        else:
            self.port = port
        self.ip = ip
        self.SERVICE_REQUEST_CODE = pySRTP_msg.SERVICE_REQUEST_CODE
        self.socket_conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not ip:
            raise Exception("MISSING TARGET IP")
    def __del__(self):
        try:
            self.socket_conn.close()
            print("CONNECTION CLOSED")
        except:
            pass
    # Creates inital socket connection and sends 56 Byte init string to target PLC.
    # Return msgs: 0 = ok, else error number.
    def initConnection(self):
        try:
            print("ESTABLISHING CONNECTION TO {}:{}... ".format(self.ip, self.port), end='')
            self.socket_conn.connect((self.ip, int(self.port)))
            print("SUCCESSFULLY CONNECTED TO {}:{}".format(self.ip, self.port))
            # Sending the init msg start request
            print("SENDING INIT_MSG to {}:{}\n\n".format(self.ip,self.port), end='')
            self.socket_conn.send(pySRTP_msg.INIT_MSG)
            self.socket_conn.settimeout(2)
            response = self.socket_conn.recv(1024)
            print(response)
            self.printLimitedBin("INIT RESPONSE:",response, end=0)
            # Verify success. (First byte of message is 0x01).
            if response[0] == 1:
                print("INIT SUCCESSFUL")
            else:
                print("INIT FAILED. EXPECTED 0x01, RECEIVED {} INSTEAD\n".format(response[0]))
            return(0)
        except Exception as err:
            print("\nPLC CONNECTION FAILED")
            print("EXCEPTION:" + str(err))
            self.socket_conn.close()
            return(1)
    def closeConnection(self):
        try:
            self.socket_conn.close()
        except Exception as err:
            print("EXCEPTION:" + str(err))
    def sendSocketCommand(self, msg):
        try:
            if not type(msg) == bytes:
                print("NOT BYTES!")
                msg = str.encode(msg)
                print("WARNING, NOT BYTES")
            print("SENDING COMMAND TO {}".format(self.ip), end='')
            self.socket_conn.send(msg)
            self.socket_conn.settimeout(2)
            reply = self.socket_conn.recv(1024)
            print("\nRECEIVED REPLY")
            #print("PLC Response: 0x" + ' 0x'.join(format(x, '02x') for x in reply))
            #self.printLimitedBin("PLC REPLY:", reply)
            print("PLC COMPLETE REPLY: ")
            print(reply)
            #self.socket_conn.close()
            self.fastDecodeResponseMessage(reply)
            return(0)
        except Exception as err:
            print("\nEXCEPTION:" + str(err))
            self.socket_conn.close()
            return(2)
        return(3)

#####################################
# Dumb Fuzzer. It essentially       #
# sends random bytestrings for      #
# each bytespace which SRTP expects.#
#####################################
    def srtpDumbFuzz(self):
        b_all = pySRTP_msg.ALLBYTES_MSG
        any = pySRTP_msg.ANY_MSG
        any[0] = random.choice(b_all) # Type
        any[1] = random.choice(b_all) # Unknown/Reserved
        any[2] = random.choice(b_all) # Sequence Number
        any[3] = random.choice(b_all) # Unknown/Reserved
        any[4] = random.choice(b_all) # Text Length
        any[5] = random.choice(b_all) # Unknown/Reserved
        any[6] = random.choice(b_all) # Unknown/Reserved
        any[7] = random.choice(b_all) # Unknown/Reserved
        any[8] = random.choice(b_all) # Unknown/Reserved
        any[9] = random.choice(b_all) # Unknown/Reserved
        any[10] = random.choice(b_all) # Unknown/Reserved
        any[11] = random.choice(b_all) # Unknown/Reserved
        any[12] = random.choice(b_all) # Unknown/Reserved
        any[13] = random.choice(b_all) # Unknown/Reserved
        any[14] = random.choice(b_all) # Unknown/Reserved
        any[15] = random.choice(b_all) # Unknown/Reserved
        any[16] = random.choice(b_all) # Unknown/Reserved
        any[17] = random.choice(b_all) # Unknown/Reserved
        any[18] = random.choice(b_all) # Unknown/Reserved
        any[19] = random.choice(b_all) # Unknown/Reserved
        any[20] = random.choice(b_all) # Unknown/Reserved
        any[21] = random.choice(b_all) # Unknown/Reserved
        any[22] = random.choice(b_all) # Unknown/Reserved
        any[23] = random.choice(b_all) # Unknown/Reserved
        any[24] = random.choice(b_all) # Unknown/Reserved
        any[25] = random.choice(b_all) # Unknown/Reserved
        any[26] = random.choice(b_all) # Time - Seconds
        any[27] = random.choice(b_all) # Time - Minutes
        any[28] = random.choice(b_all) # Time - Hours
        any[29] = random.choice(b_all) # Unknown/Reserved
        any[30] = random.choice(b_all) # Sequence Number
        any[31] = random.choice(b_all) # Message Type
        any[32] = random.choice(b_all) # Mailbox Source
        any[33] = random.choice(b_all) # Mailbox Source
        any[34] = random.choice(b_all) # Mailbox Source
        any[35] = random.choice(b_all) # Mailbox Source
        any[36] = random.choice(b_all) # Mailbox Destination
        any[37] = random.choice(b_all) # Mailbox Destination
        any[38] = random.choice(b_all) # Mailbox Destination
        any[39] = random.choice(b_all) # Mailbox Destination
        any[40] = random.choice(b_all) # Unknown/Reserved
        any[42] = random.choice(b_all) # Service Request
        any[43] = random.choice(b_all) # Memory Type
        any[44] = random.choice(b_all) # Memory Type
        any[45] = random.choice(b_all) # Memory Type
        any[46] = random.choice(b_all) # Memory Type
        any[47] = random.choice(b_all) # Memory Type
        any[48] = random.choice(b_all) # Unknown/Reserved
        any[49] = random.choice(b_all) # Unknown/Reserved
        any[50] = random.choice(b_all) # Unknown/Reserved
        any[51] = random.choice(b_all) # Unknown/Reserved
        any[52] = random.choice(b_all) # Unknown/Reserved
        any[53] = random.choice(b_all) # Unknown/Reserved
        any[54] = random.choice(b_all) # Unknown/Reserved
        any[55] = random.choice(b_all) # Unknown/Reserved
        bytes_to_send = b''.join(any)
        # print(bytes_to_send)
        self.sendSocketCommand(bytes_to_send)
        return(bytes_to_send)
####################################
# Smart Fuzzer. Sends bytestrings  #
# with consideration of what SRTP  #
# expects to recieve (fixed values)#
####################################
    def srtpSmartFuzz(self):
        b0 = pySRTP_msg.ALLBYTES_MSG[0]
        b1 = pySRTP_msg.ALLBYTES_MSG[1]
        b2 = pySRTP_msg.ALLBYTES_MSG[2]
        b198 = pySRTP_msg.ALLBYTES_MSG[198]
        b14 = pySRTP_msg.ALLBYTES_MSG[14]
        b16 = pySRTP_msg.ALLBYTES_MSG[16]
        any = pySRTP_msg.ANY_MSG
        any[0] = b2 # Type
        any[1] = b0 # Unknown/Reserved
        any[2] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Sequence Number
        any[3] = b0 # Unknown/Reserved
        any[4] = b0 # Text Length
        any[5] = b0 # Unknown/Reserved
        any[6] = b0 # Unknown/Reserved
        any[7] = b0 # Unknown/Reserved
        any[8] = b0 # Unknown/Reserved
        any[9] = b1 # Unknown/Reserved
        any[10] = b0 # Unknown/Reserved
        any[11] = b0 # Unknown/Reserved
        any[12] = b0 # Unknown/Reserved
        any[13] = b0 # Unknown/Reserved
        any[14] = b0 # Unknown/Reserved
        any[15] = b0 # Unknown/Reserved
        any[16] = b0 # Unknown/Reserved
        any[17] = b1 # Unknown/Reserved
        any[18] = b0 # Unknown/Reserved
        any[19] = b0 # Unknown/Reserved
        any[20] = b0 # Unknown/Reserved
        any[21] = b0 # Unknown/Reserved
        any[22] = b0 # Unknown/Reserved
        any[23] = b0 # Unknown/Reserved
        any[24] = b0 # Unknown/Reserved
        any[25] = b0 # Unknown/Reserved
        any[26] = b0 # Time - Seconds
        any[27] = b0 # Time - Minutes
        any[28] = b0 # Time - Hours
        any[29] = b0 # Unknown/Reserved
        any[30] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Sequence Number
        any[31] = b198 # Message Type
        any[32] = b0 # Mailbox Source
        any[33] = b0 # Mailbox Source
        any[34] = b0 # Mailbox Source
        any[35] = b0 # Mailbox Source
        any[36] = b14 # Mailbox Destination
        any[37] = b16 # Mailbox Destination
        any[38] = b0 # Mailbox Destination
        any[39] = b0 # Mailbox Destination
        any[40] = b1 # Unknown/Reserved
        any[42] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Service Request
        any[43] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Memory Type
        any[44] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Memory Type
        any[45] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Memory Type
        any[46] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Memory Type
        any[47] = random.choice(pySRTP_msg.ALLBYTES_MSG) # Memory Type
        any[48] = b0 # Unknown/Reserved
        any[49] = b0 # Unknown/Reserved
        any[50] = b0 # Unknown/Reserved
        any[51] = b0 # Unknown/Reserved
        any[52] = b0 # Unknown/Reserved
        any[53] = b0 # Unknown/Reserved
        any[54] = b0 # Unknown/Reserved
        any[55] = b0 # Unknown/Reserved
        '''send_bytes = b''.join(any)
        print(send_bytes)'''
        #print(pySRTP_msg.ANY_MSG)
        #print(random.choice(pySRTP_msg.ALLBYTES_MSG))
        bytes_to_send = b''.join(any)
        #print(bytes_to_send)
        # print("FUZZ MSG: " + bytes_to_send + "\n")
        self.sendSocketCommand(bytes_to_send)
        return(bytes_to_send)
    ###########################################################
    # Decodes message response printing basic info.
    ###########################################################
    def fastDecodeResponseMessage(self, msg):
        try:
            status_code         = struct.unpack('B', bytes([msg[42]]))[0]
            status_code_minor   = struct.unpack('B', bytes([msg[43]]))[0]
            reg_data            = struct.unpack('H', bytearray(msg[44:46]))[0] # Danger, 16 bit word only! TODO
            print("")
            print("PLC STATUS CODES (42,43): 0x{:02x} 0x{:02x}".format(status_code, status_code_minor))
            print("REGISTER DATA (HEX): {:02x}".format(reg_data))
        except Exception as err:
            print(err)
            return(None)
    def printArrDebug(self, arr):
        for idx,b in enumerate(arr):
            if idx not in range(6,24):
                print("{:02d}=>0x{:s}".format(idx, b.hex()) )
    ###########################################################
    # Prints sample of binary data.
    ###########################################################
    def printLimitedBin(self, pre_msg, msg, start=7, end=7):
        hex_resp_start = ""
        hex_resp_end = ""
        iter_len = sum(1 for _ in enumerate(msg))
        for idx,x in enumerate(msg):
            hex_resp_start += " {:02x}".format(x)
            if idx > start: break
        for idx,x in enumerate(msg):
            if iter_len - idx <= end:
                hex_resp_end += " {:02x}".format(x)
        print("{}{}...{} (DISPLAYING {} OF {} BYTES)".format(pre_msg, hex_resp_start, hex_resp_end, start + end, len(msg)))