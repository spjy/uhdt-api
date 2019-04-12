# UHDT API

The UHDT API, built on the Django Framework, primarily acts as the middleware between the recognition systems and the interoperability server to ensure efficient and smooth operation of the image processing pipeline. For instance, the API has the ability to observe the directory of the Raspberry Pi to watch for new images, then sends a request to the API, and it autonomously runs the object detection, color and alphanumeric recognition scripts and finally saves the data into a database to be staged for sending to the interoperability server. In addition, it has the advantage of being able to simultaneously run multiple tests at a time due to being built on the REST paradigm.

## Requirements

1. Python 3.6 +
2. Django 2.1.7

## Installation

1. Clone the repository:
```bash
$ git clone https://github.com/spjy/uhdtapi.git
```

2. Install Python 3.6 +
https://www.python.org/downloads/ 

3. Install Django 2.1.7
```bash
$ pip install Django
```

## Running

Simply run this command in the root project folder:

```bash
$ python ./src/manage.py runserver
```

## Directory Structure

`/src` - The main source code of the project.

### App folders

These folders contain the apps of the project.

`/src/alphanumeric` - This is where the alphanumeric recognition script is held.

`/src/color` - This is where the color recognition script is held.

`/src/object` - This is where the object detection script is held.

`/src/pipeline` - This is where the data culminates after all of the recognition scripts are run.


### Common files in app folders

`urls.py` - This contains the definitions for the request URLs.

`views.py` - This contains the functionality for each type of REST method.

## How it works

It starts on the Raspberry Pi; there will be an observer watching for new files being written to a certain file directory using the Python framework Watchdog. From there, a POST request will be made to the object detection script to detect at what location the shape is. Then, if object detection is confident enough, it will save the bounding box coordinates and send a cropped image via a POST request off to color and alphanumeric recognition. It will then save the outcomes of the color and alphanumeric recognition scripts into the database. Finally, it will send off the results to the interoperatbility network.
