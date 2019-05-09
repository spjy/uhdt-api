import argparse
import pysftp
import piexif
from PIL import Image
from simple_rest_client.api import API
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from simple_rest_client.api import API

class Watcher:
    DIRECTORY_TO_WATCH = "C:\watcher_directory"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username
        self.password

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            filepath = event.src_path.split(os.sep)
            sep = os.sep
            print(filepath[len(filepath) - 1])

            filename = filepath[len(filepath) - 1]

            filepath.pop(len(filepath) - 1)

            filepath = os.sep.join(filepath)
            print(filepath)

            # Connect to mavlink and get gps coordinate
            # write exif data to image
            # connect to IP laptop from pi via ssh
            # transfer image via sftp to C:\watcher_directory
            # close connection

            exif_dict = piexif.load(event.src_path)
            exifObj["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "N";
            exifObj["GPS"][piexif.GPSIFD.GPSLatitude] = [366132304, 10000000],
            exifObj["GPS"][piexif.GPSIFD.GPSLongitudeRef] = "W";
            exifObj["GPS"][piexif.GPSIFD.GPSLongitude] = [1219323420, 10000000];

            exif_bytes = piexif.dumb(exif_dict)
            piexif.insert(exif_bytes, event.src_path)

            for ifd_name in exif_dict:
                print("\n{0} IFD:".format(ifd_name))
                for key in exif_dict[ifd_name]:
                    try:
                        print(key, exif_dict[ifd_name][key][:10])
                    except:
                        print(key, exif_dict[ifd_name][key])

            sftp = pysftp.Connection(host=self.ip, port=self.port, username=self.username, password=self.password)

            sftp.put()


# from pipeline.models import Metadata

# Script to communicate from the CPP script to python and save the object to the database

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="IP of the image processing laptop")
    parser.add_argument("--port", help="Port of the image processing laptop")
    parser.add_argument("--username", help="Username of the image processing laptop")
    parser.add_argument("--password", help="Password of the image processing laptop")
    args = parser.parse_args()

    Watcher().run(args.ip, args.port, args.username, args.password)

if __name__ == "__main__":
    main()
