# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))