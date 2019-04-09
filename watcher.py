
import time
import os
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

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            filename = event.src_path.split(os.sep)
            print(filename[len(filename) - 1])

            api = API(
                api_root_url='http://localhost:8000',
                json_encode_body=True,
                append_slash=True,
            )

            api.add_resource(resource_name='pipeline')
            api.pipeline.create(
                body = {
                    'image_name': filename,
                    'image_path': event.src_path,
                }
            )

if __name__ == '__main__':
    w = Watcher()
    w.run()