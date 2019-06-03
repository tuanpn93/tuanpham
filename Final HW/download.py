import requests
import sys
import tempfile
import itertools as IT
import os

#print(r.status_code == requests.codes.ok)


def uniquify(path, sep = ''):
    def name_sequence():
        count = IT.count()
        yield ''
        while True:
            yield '{s}{n:d}'.format(s = sep, n = next(count))
    orig = tempfile._name_sequence
    with tempfile._once_lock:
        tempfile._name_sequence = name_sequence()
        path = os.path.normpath(path)
        print("Path : ", path)
        basename = os.path.split(path)[1]
        print("Base: ", basename)
        filename, ext = os.path.splitext(basename)
        print("Filename: ", filename)
        print("Ext: ", ext)
        fd, filename = tempfile.mkstemp(dir = os.getcwd(), prefix = filename, suffix = ext)
        tempfile._name_sequence = orig
    return filename


def downloader():
    url = format(sys.argv[1])
    data = requests.get(url).content

    if url[-1:] == '/':
        with open(uniquify("index.html"), 'wb') as handler:
            handler.write(data)
    else:
        filename = uniquify(url)
        print("Filename : ", filename)
        with open(filename, 'wb') as handler:
            handler.write(data)


downloader()
