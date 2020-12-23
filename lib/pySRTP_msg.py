INIT_MSG = bytearray(56)

# Sample Transmit message.
# With this standard message format,
# you'll likely need to update
# some fields before sending.
BASE_MSG = [
    b'\x02',        # 00 - Type (03 is Return, 02 is Transmit)
    b'\x00',        # 01 - Reserved/Unknown
    b'\x06',        # 02 - Seq Number - FILL AT RUNTIME
    b'\x00',        # 03 - Reserved/Unknown
    b'\x00',        # 04 - Text Length - FILL AT RUNTIME ???
    b'\x00',        # 05 - Reserved/Unknown
    b'\x00',        # 06 - Reserved/Unknown
    b'\x00',        # 07 - Reserved/Unknown
    b'\x00',        # 08 - Reserved/Unknown
    b'\x01',        # 09 - Reserved/Unknown
    b'\x00',        # 10 - Reserved/Unknown
    b'\x00',        # 11 - Reserved/Unknown
    b'\x00',        # 12 - Reserved/Unknown
    b'\x00',        # 13 - Reserved/Unknown
    b'\x00',        # 14 - Reserved/Unknown
    b'\x00',        # 15 - Reserved/Unknown
    b'\x00',        # 16 - Reserved/Unknown
    b'\x01',        # 17 - Reserved/Unknown
    b'\x00',        # 18 - Reserved/Unknown
    b'\x00',        # 19 - Reserved/Unknown
    b'\x00',        # 20 - Reserved/Unknown
    b'\x00',        # 21 - Reserved/Unknown
    b'\x00',        # 22 - Reserved/Unknown
    b'\x00',        # 23 - Reserved/Unknown
    b'\x00',        # 24 - Reserved/Unknown
    b'\x00',        # 25 - Reserved/Unknown
    b'\x00',        # 26 - Time Seconds - FILL AT RUNTIME
    b'\x00',        # 27 - Time Minutes - FILL AT RUNTIME
    b'\x00',        # 28 - Time Hours   - FILL AT RUNTIME
    b'\x00',        # 29 - Reserved/Unknown
    b'\x06',        # 30 - Seq Number (Repeated) - FILL AT RUNTIME ???? 0x06 always?
    b'\xc0',        # 31 - Message Type
    b'\x00',        # 32 - Mailbox Source
    b'\x00',        # 33 - Mailbox Source
    b'\x00',        # 34 - Mailbox Source
    b'\x00',        # 35 - Mailbox Source
    b'\x10',        # 36 - Mailbox Destination
    b'\x0e',        # 37 - Mailbox Destination
    b'\x00',        # 38 - Mailbox Destination
    b'\x00',        # 39 - Mailbox Destination
    b'\x01',        # 40 - Packet Number
    b'\x01',        # 41 - Total Packet Number
    b'\x00',        # 42 - Service Request Code - (Operation Type SERVICE_REQUEST_CODE)
    b'\x00',        # 43 - Request Dependent Space (For Reading: set MEMORY_TYPE_CODE)
    b'\x00',        # 44 - Request Dependent Space (For Reading: set to Address - 1)(LSB)
    b'\x00',        # 45 - Request Dependent Space (For Reading: set to Address - 1)(MSB)
    b'\x00',        # 46 - Request Dependent Space (For Reading: Data Size Bytes)(LSB)
    b'\x00',        # 47 - Request Dependent Space (For Reading: Data Size Bytes)(MSB)
    b'\x00',        # 48 - Reserved/Unknown
    b'\x00',        # 49 - Reserved/Unknown
    b'\x00',        # 50 - Reserved/Unknown
    b'\x00',        # 51 - Reserved/Unknown
    b'\x00',        # 52 - Reserved/Unknown
    b'\x00',        # 53 - Reserved/Unknown
    b'\x00',        # 54 - Reserved/Unknown
    b'\x00'         # 55 - Reserved/Unknown
]

ANY_MSG = [
    b'\x00',        # 00
    b'\x00',        # 01
    b'\x00',        # 02
    b'\x00',        # 03
    b'\x00',        # 04
    b'\x00',        # 05
    b'\x00',        # 06
    b'\x00',        # 07
    b'\x00',        # 08
    b'\x00',        # 09
    b'\x00',        # 10
    b'\x00',        # 11
    b'\x00',        # 12
    b'\x00',        # 13
    b'\x00',        # 14
    b'\x00',        # 15
    b'\x00',        # 16
    b'\x00',        # 17
    b'\x00',        # 18
    b'\x00',        # 19
    b'\x00',        # 20
    b'\x00',        # 21
    b'\x00',        # 22
    b'\x00',        # 23
    b'\x00',        # 24
    b'\x00',        # 25
    b'\x00',        # 26
    b'\x00',        # 27
    b'\x00',        # 28
    b'\x00',        # 29
    b'\x00',        # 30
    b'\x00',        # 31
    b'\x00',        # 32
    b'\x00',        # 33
    b'\x00',        # 34
    b'\x00',        # 35
    b'\x00',        # 36
    b'\x00',        # 37
    b'\x00',        # 38
    b'\x00',        # 39
    b'\x00',        # 40
    b'\x00',        # 41
    b'\x00',        # 42
    b'\x00',        # 43
    b'\x00',        # 44
    b'\x00',        # 45
    b'\x00',        # 46
    b'\x00',        # 47
    b'\x00',        # 48
    b'\x00',        # 49
    b'\x00',        # 50
    b'\x00',        # 51
    b'\x00',        # 52
    b'\x00',        # 53
    b'\x00',        # 54
    b'\x00'         # 55
    ]

ALLBYTES_MSG = [
    b'\x00', # 00
    b'\x01', # 01
    b'\x02', # 02
    b'\x03', # 03
    b'\x04', # 04
    b'\x05', # 05
    b'\x06', # 06
    b'\x07', # 07
    b'\x08', # 08
    b'\x09', # 09
    b'\x0A', # 10
    b'\x0B', # 11
    b'\x0C', # 12
    b'\x0D', # 13
    b'\x0E', # 14
    b'\x0F', # 15
    b'\x10', # 16
    b'\x11', # 17
    b'\x12', # 18
    b'\x13', # 19
    b'\x14', # 20
    b'\x15', # 21
    b'\x16', # 22
    b'\x18', # 23
    b'\x19', # 24
    b'\x1A', # 25
    b'\x1B', # 26
    b'\x1C', # 27
    b'\x1D', # 28
    b'\x1E', # 29
    b'\x1F', # 30
    b'\x20', # 31
    b'\x21', # 32
    b'\x22', # 33
    b'\x23', # 34
    b'\x24', # 35
    b'\x25', # 36
    b'\x26', # 37
    b'\x27', # 38
    b'\x28', # 39
    b'\x29', # 40
    b'\x2A', # 41
    b'\x2B', # 42
    b'\x2C', # 43
    b'\x2D', # 44
    b'\x2E', # 45
    b'\x2F', # 46
    b'\x30', # 47
    b'\x32', # 48
    b'\x33', # 49
    b'\x34', # 50
    b'\x35', # 51
    b'\x36', # 52
    b'\x37', # 53
    b'\x38', # 54
    b'\x39', # 55
    b'\x3A', # 56
    b'\x3B', # 57
    b'\x3C', # 58
    b'\x3D', # 59
    b'\x3E', # 60
    b'\x3F', # 61
    b'\x40', # 62
    b'\x41', # 63
    b'\x42', # 64
    b'\x43', # 65
    b'\x44', # 66
    b'\x45', # 67
    b'\x46', # 68
    b'\x47', # 69
    b'\x48', # 70
    b'\x49', # 72
    b'\x4A', # 73
    b'\x4B', # 74
    b'\x4C', # 75
    b'\x4D', # 76
    b'\x4E', # 77
    b'\x4F', # 78
    b'\x50', # 79
    b'\x51', # 80
    b'\x52', # 81
    b'\x53', # 82
    b'\x54', # 83
    b'\x55', # 84
    b'\x56', # 85
    b'\x57', # 86
    b'\x58', # 87
    b'\x59', # 88
    b'\x5A', # 89
    b'\x5B', # 90
    b'\x5C', # 91
    b'\x5D', # 92
    b'\x5E', # 93
    b'\x5F', # 94
    b'\x60', # 95
    b'\x62', # 96, ah fuck it.
    b'\x63', # 106
    b'\x64', # 107
    b'\x65', # 108
    b'\x66', # 109
    b'\x67', # 110
    b'\x68', # 111
    b'\x69', # 112
    b'\x6A', # 113
    b'\x6B', # 114
    b'\x6C', # 115
    b'\x6D', # 116
    b'\x6E', # 117
    b'\x6F', # 118
    b'\x70', # 119
    b'\x71', # 120
    b'\x72', # 121
    b'\x73', # 122
    b'\x74', # 123
    b'\x75', # 124
    b'\x76', # 125
    b'\x77', # 126
    b'\x78', # 127
    b'\x79', # 128
    b'\x7A', # 129
    b'\x7B', # 130
    b'\x7C', # 131
    b'\x7D', # 132
    b'\x7E', # 133
    b'\x7F', # 134
    b'\x80', # 135
    b'\x81', # 136
    b'\x82', # 137
    b'\x83', # 138
    b'\x84', # 139
    b'\x85', # 140
    b'\x86', # 141
    b'\x87', # 142
    b'\x88', # 143
    b'\x89', # 144
    b'\x8A', # 145
    b'\x8B', # 146
    b'\x8C', # 147
    b'\x8D', # 148
    b'\x8E', # 149
    b'\x8F', # 150
    b'\x90', # 151
    b'\x91', # 152
    b'\x92', # 153
    b'\x93', # 154
    b'\x94', # 155
    b'\x95', # 156
    b'\x96', # 157
    b'\x97', # 158
    b'\x98', # 159
    b'\x99', # 160
    b'\x9A', # 161
    b'\x9B', # 162
    b'\x9C', # 163
    b'\x9D', # 164
    b'\x9E', # 165
    b'\x9F', # 166
    b'\xA0', # 167
    b'\xA2', # 168
    b'\xA3', # 169
    b'\xA4', # 170
    b'\xA5', # 171
    b'\xA6', # 172
    b'\xA7', # 173
    b'\xA8', # 174
    b'\xA9', # 175
    b'\xAA', # 176
    b'\xAB', # 177
    b'\xAC', # 178
    b'\xAD', # 179
    b'\xAE', # 180
    b'\xAF', # 181
    b'\xB0', # 182
    b'\xB1', # 183
    b'\xB2', # 184
    b'\xB3', # 185
    b'\xB4', # 186
    b'\xB5', # 187
    b'\xB6', # 188
    b'\xB7', # 189
    b'\xB8', # 190
    b'\xB9', # 191
    b'\xBA', # 192
    b'\xBB', # 193
    b'\xBC', # 194
    b'\xBD', # 195
    b'\xBE', # 196
    b'\xBF', # 197
    b'\xC0', # 198 
    b'\xC1', # 199
    b'\xC2', # 200
    b'\xC3', # 201
    b'\xC4', # 202
    b'\xC5', # 203
    b'\xC6', # 204
    b'\xC7', # 205
    b'\xC8', # 206
    b'\xC9', # 207
    b'\xCA', # 208
    b'\xCB', # 209
    b'\xCC', # 210
    b'\xCD', # 211
    b'\xCE', # 212
    b'\xCF', # 213
    b'\xD0', # 214
    b'\xD1', # 215
    b'\xD2', # 216
    b'\xD3', # 217
    b'\xD4', # 218
    b'\xD5', # 219
    b'\xD6', # 220
    b'\xD7', # 221
    b'\xD8', # 222
    b'\xD9', # 223
    b'\xDA', # 224
    b'\xDB', # 225
    b'\xDC', # 226
    b'\xDD', # 227
    b'\xDE', # 228
    b'\xDF', # 229
    b'\xE0', # 230
    b'\xE1', # 231
    b'\xE2', # 232
    b'\xE3', # 233
    b'\xE4', # 234
    b'\xE5', # 235
    b'\xE6', # 236
    b'\xE7', # 237
    b'\xE8', # 238
    b'\xE9', # 239
    b'\xEA', # 240
    b'\xEB', # 241
    b'\xEC', # 242
    b'\xED', # 243
    b'\xEE', # 244
    b'\xEF', # 245
    b'\xF0', # 246
    b'\xF1', # 247
    b'\xF2', # 248
    b'\xF3', # 249
    b'\xF4', # 250
    b'\xF5', # 251
    b'\xF6', # 252
    b'\xF7', # 253
    b'\xF8', # 254
    b'\xF9', # 255
    b'\xFA', # 256
    b'\xFB', # 257
    b'\xFC', # 258
    b'\xFD', # 259
    b'\xFE', # 260
    b'\xFF'  # 261
]

# Used at byte locaiton 42
SERVICE_REQUEST_CODE = {
    "PLC_STATUS"             : b'\x00',
    "RETURN_PROG_NAME"       : b'\x03',
    "READ_SYS_MEMORY"        : b'\x04',    # Used to read general memory register (Example: %R12344)
    "READ_TASK_MEMORY"       : b'\x05',
    "READ_PROG_MEMORY"       : b'\x06',
    "WRITE_SYS_MEMORY"       : b'\x07',
    "WRITE_TASK_MEMORY"      : b'\x08',
    "WRITE_PROG_MEMORY"      : b'\x09',
    "PROGRAMMER_LOGON"       : b'\x20',
    "CHANGE_PLC_PRIV"        : b'\x21',
    "SET_CTL_ID"             : b'\x22',
    "SET_PLC"                : b'\x23',
    "SET_PLC_DATETIME"       : b'\x24',
    "RETURN_DATETIME"        : b'\x25',
    "RETURN_FAULT_TABLE"     : b'\x38',
    "CLEAR_FAULT_TABLE"      : b'\x39',
    "PROGRAM_STORE"          : b'\x3f',     # Upload to PLC
    "PROGRAM_LOAD"           : b'\x40',     # Download to PLC
    "RETURN_CONTROLLER_TYPE" : b'\x43',
    "TOGGLE_FORCE_SYSTEM_MEM": b'\x44'
}

# Used at byte locaiton 43
MEMORY_TYPE_CODE = {
    "R"  :   b'\x08',    # Register (Str)
    "AI" :   b'\x0a',    # Analog Input (Str)
    "AQ" :   b'\x0c',    # Analog Output (Str)
    "I"  :   b'\x10',    # Discrete Input (Byte)
    "Q"  :   b'\x12',    # Discrete Output (Byte)
}

