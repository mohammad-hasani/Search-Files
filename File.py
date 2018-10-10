from Database import Database
import os
from threading import Thread

drives = ['E:/', 'F:/', 'G:/', 'H:/', 'I:/']


def main():
    t = Thread(target=start)
    t.start()

def start():
    for drivename in drives:
        for root, dirs, files in os.walk(drivename):
            if len(files) > 0:
                for name in files:
                    name = name.strip()
                    addr = root + '/' + name
                    addr = addr.strip()
                    split = name.split('.')
                    type = split[len(split) - 1]
                    type = type.strip()
                    if len(split) == 1:
                        type = ''
                    query = """
                    INSERT INTO tbl_files
                    (addr,
                    name,
                    type)
                    VALUES
                    ('%s',
                    '%s',
                    '%s');
                """ % (addr, name, type)
                    db = Database()
                    db.insert(query=query)
                    db.close()
        print('Finished ' + drivename)
