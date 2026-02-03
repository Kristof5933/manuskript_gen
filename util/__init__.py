from .fakeService import FakeService

import re

def safeFilename(filename: str, extension: str = None) -> str:
    if extension is not None:
        filename = "%s.%s" % (filename, extension)

    name = filename.encode('ascii', 'replace').decode('ascii')
    filenamesToAvoid = list(["CON", "PRN", "AUX", "NUL"])

    for i in range(1, 9):
        filenamesToAvoid.append("COM" + str(i))
        filenamesToAvoid.append("LPT" + str(i))

    if name.upper() in filenamesToAvoid:
        name = "_" + name

    return re.sub(r"[^a-zA-Z0-9._\-+()]", "_", name)

def formatNumber(n, totalCount):
    width = len(str(totalCount))
    return f"{n:0{width}d}"
