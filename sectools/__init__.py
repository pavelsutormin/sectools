def readsec(disc='/dev/sda1', sec=0):
    disc = str(disc)
    sec = int(sec)
    read = None
    with open(disc, 'rb') as fp:
    fp.seek(sec * 512)
    read = fp.read(512)
    return read
def writesec(disc='/dev/sda1', sec=0, data='\x00XX\x98\xaa'):
    disc = str(disc)
    sec = int(sec)
    read = None
    with open(disc, 'rb') as fp:
    fp.seek(sec * 512)
    fp.write(data)
