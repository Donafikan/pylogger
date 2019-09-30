"""
___author   : Dona F.

__desc      : Python Logger

"""

import logging
import logging.handlers
import sys

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


logger = logging.getLogger()

logformatter = logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer, filename):
        self.observer = observer
        self.filename = filename

    def on_created(self, event):
        logging.info("File %s - created" % event.src_path)

    def on_modified(self, event):
        logging.info("File %s - modified" % event.src_path)

    def on_moved(self, event):
        if not event.is_directory and event.src_path.endswith(self.filename):
            logging.info("File %s - was just moved to - %s ", event.src_path, event.dest_path)
        else:
            logging.info("Folder %s - was just moved to - %s ", event.src_path, event.dest_path)

    def on_deleted(self, event):
        logging.info("File %s - deleted" % event.src_path)

def main():
    paths = ["C:/Users/User/Music", "D:/Python/Program"]
    filename = ""
    filehandler = logging.FileHandler("D:/Python/Program/file.log")
    filehandler.setFormatter(logformatter)
    logger.addHandler(filehandler)
    consolehandler = logging.StreamHandler()
    consolehandler.setFormatter(logformatter)
    logger.addHandler(consolehandler)
    observer = Observer()
    event_handler = MyEventHandler(observer, filename)
    for i in paths:
        targetpath = str(i)
        observer.schedule(event_handler, targetpath, recursive=True)
    observer.start()
    observer.join()
    return 0


if __name__ == "__main__":
    sys.exit(main())