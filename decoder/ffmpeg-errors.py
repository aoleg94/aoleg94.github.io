#!/usr/bin/env python

import json

def FFERRTAG(a,b,c,d):
	r = 0
	for x in (d,c,b,a):
		r <<= 8
		if isinstance(x, int):
			r |= x
		elif isinstance(x, str):
			r |= ord(x.encode())
		else:
			raise RuntimeError
	return -r

#print(hex(FFERRTAG( 'I','N','D','A')))

CODE = {}

CODE['AVERROR_BSF_NOT_FOUND'] = FFERRTAG(0xF8,'B','S','F')
CODE['AVERROR_BUG'] = FFERRTAG( 'B','U','G','!')
CODE['AVERROR_BUFFER_TOO_SMALL'] = FFERRTAG( 'B','U','F','S')
CODE['AVERROR_DECODER_NOT_FOUND'] = FFERRTAG(0xF8,'D','E','C')
CODE['AVERROR_DEMUXER_NOT_FOUND'] = FFERRTAG(0xF8,'D','E','M')
CODE['AVERROR_ENCODER_NOT_FOUND'] = FFERRTAG(0xF8,'E','N','C')
CODE['AVERROR_EOF'] = FFERRTAG( 'E','O','F',' ')
CODE['AVERROR_EXIT'] = FFERRTAG( 'E','X','I','T')
CODE['AVERROR_EXTERNAL'] = FFERRTAG( 'E','X','T',' ')
CODE['AVERROR_FILTER_NOT_FOUND'] = FFERRTAG(0xF8,'F','I','L')
CODE['AVERROR_INVALIDDATA'] = FFERRTAG( 'I','N','D','A')
CODE['AVERROR_MUXER_NOT_FOUND'] = FFERRTAG(0xF8,'M','U','X')
CODE['AVERROR_OPTION_NOT_FOUND'] = FFERRTAG(0xF8,'O','P','T')
CODE['AVERROR_PATCHWELCOME'] = FFERRTAG( 'P','A','W','E')
CODE['AVERROR_PROTOCOL_NOT_FOUND'] = FFERRTAG(0xF8,'P','R','O')

CODE['AVERROR_STREAM_NOT_FOUND'] = FFERRTAG(0xF8,'S','T','R')
CODE['AVERROR_BUG2'] = FFERRTAG( 'B','U','G',' ')
CODE['AVERROR_UNKNOWN'] = FFERRTAG( 'U','N','K','N')
CODE['AVERROR_EXPERIMENTAL'] = (-0x2bb2afa8)
CODE['AVERROR_INPUT_CHANGED'] = (-0x636e6701)
CODE['AVERROR_OUTPUT_CHANGED'] = (-0x636e6702)

CODE['AVERROR_HTTP_BAD_REQUEST'] = FFERRTAG(0xF8,'4','0','0')
CODE['AVERROR_HTTP_UNAUTHORIZED'] = FFERRTAG(0xF8,'4','0','1')
CODE['AVERROR_HTTP_FORBIDDEN'] = FFERRTAG(0xF8,'4','0','3')
CODE['AVERROR_HTTP_NOT_FOUND'] = FFERRTAG(0xF8,'4','0','4')
CODE['AVERROR_HTTP_OTHER_4XX'] = FFERRTAG(0xF8,'4','X','X')
CODE['AVERROR_HTTP_SERVER_ERROR'] = FFERRTAG(0xF8,'5','X','X')

STR = {}

STR['AVERROR_BSF_NOT_FOUND'] = "Bitstream filter not found"
STR['AVERROR_BUG'] = "Internal bug, should not have happened"
STR['AVERROR_BUG2'] = "Internal bug, should not have happened"
STR['AVERROR_BUFFER_TOO_SMALL'] = "Buffer too small"
STR['AVERROR_DECODER_NOT_FOUND'] = "Decoder not found"
STR['AVERROR_DEMUXER_NOT_FOUND'] = "Demuxer not found"
STR['AVERROR_ENCODER_NOT_FOUND'] = "Encoder not found"
STR['AVERROR_EOF'] = "End of file"
STR['AVERROR_EXIT'] = "Immediate exit requested"
STR['AVERROR_EXTERNAL'] = "Generic error in an external library"
STR['AVERROR_FILTER_NOT_FOUND'] = "Filter not found"
STR['AVERROR_INPUT_CHANGED'] = "Input changed"
STR['AVERROR_INVALIDDATA'] = "Invalid data found when processing input"
STR['AVERROR_MUXER_NOT_FOUND'] = "Muxer not found"
STR['AVERROR_OPTION_NOT_FOUND'] = "Option not found"
STR['AVERROR_OUTPUT_CHANGED'] = "Output changed"
STR['AVERROR_PATCHWELCOME'] = "Not yet implemented in FFmpeg, patches welcome"
STR['AVERROR_PROTOCOL_NOT_FOUND'] = "Protocol not found"
STR['AVERROR_STREAM_NOT_FOUND'] = "Stream not found"
STR['AVERROR_UNKNOWN'] = "Unknown error occurred"
STR['AVERROR_EXPERIMENTAL'] = "Experimental feature"
STR['AVERROR_INPUT_AND_OUTPUT_CHANGED'] = "Input and output changed"
STR['AVERROR_HTTP_BAD_REQUEST'] = "Server returned 400 Bad Request"
STR['AVERROR_HTTP_UNAUTHORIZED'] = "Server returned 401 Unauthorized (authorization failed)"
STR['AVERROR_HTTP_FORBIDDEN'] = "Server returned 403 Forbidden (access denied)"
STR['AVERROR_HTTP_NOT_FOUND'] = "Server returned 404 Not Found"
STR['AVERROR_HTTP_OTHER_4XX'] = "Server returned 4XX Client Error, but not one of 40{0,1,3,4}"
STR['AVERROR_HTTP_SERVER_ERROR'] = "Server returned 5XX Server Error reply"

o = {}
f = o['FFMPEG'] = {}

u = lambda x: x if x >= 0 else (2**32 + x)

for name in CODE:
	code = CODE[name]
	desc = STR[name]
	f[str(u(code))] = [f'{code} {name} {desc}']

print(json.dumps(o, indent=2))
