# UHDT API

The UHDT API, built on the Django Framework, primarily acts as the middleware between the recognition systems and the interoperability server to ensure efficient and smooth operation of the image processing pipeline. For instance, the API has the ability to observe the directory of the Raspberry Pi to watch for new images, then sends a request to the API, and it autonomously runs the object detection, color and alphanumeric recognition scripts and finally saves the data into a database to be staged for sending to the interoperability server. In addition, it has the advantage of being able to simultaneously run multiple tests at a time due to being built on the REST paradigm.

## Requirements

1. Python 3.6 +
2. Django 2.1.7

## Installation

1. Clone the repository:
```bash
git clone https://github.com/spjy/uhdt-api.git
cd uhdt-api
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

`/src/alphanumeric` - This is where the alphanumeric recognition script is held, along with the endpoint declarations.

`/src/color` - This is where the color recognition script is held, along with the endpoint declarations.

`/src/object` - This is where the object detection script is held, along with the endpoint declarations.

`/src/pipeline` - This is where the data culminates after all of the image data is stored.

### Common files in app folders

These are the essential file names you should know about. If you want to read more about them, refer to the [Django Docs](https://docs.djangoproject.com/en/2.2/).

`urls.py` - This contains the definitions for the request URLs.

`views.py` - This contains the functionality for each type of REST method.

## HTTP Endpoints

HTTP Endpoints are how you initialize each script. You can "hit" an HTTP endpoint similar to how you enter a URL into a web browser. There are three types of endpoints and those are GET, POST, PUT, PATCH and DELETE. GET is the act of receiving a record from the server. POST is the act of sending a record to the server and the server saves the said record. PUT is the replacing of a whole record. PATCH is the editing of a certain key in a record. Finally, DELETE is the deletion of a record.

In order to test out the endpoints, use a REST client such as Insomnia. Simply enter the URL of the server and append the endpoint you want to initialize. For example, if I wanted to access the GET endpoint called "pipeline" on my local computer, I would specify I wanted to use the GET protocol and enter the URL as http://localhost:3000/pipeline.

This is one method of how to deal with data transfer across various nodes.

All endpoints take the payload of:

```
{
  "image_name": "name"
  "image_path": "path/to/image"
}
```

`/pipeline` POST - This initializes an entry into a database for a specific image and initializes the object detection script.

`/alphanumeric` POST - This endpoint initializes the alphanumeric recognition script and saves the result to a database.

`/color` POST - This endpoint initializes the color recognition script and saves the result to a database.

`/object` POST - This endpoint initializes the object recognition script and saves the result to a database.

## Watcher

To start the recognition process, we need to know when new files are created. Polling and watching for a directory is expensive and inefficient, especially if we are running multiple detection scripts. By using Watchdog, a file watcher, we can send an event only when new files are created, thus reducing computer resources. Watchdog works by interfacing with the kernal of the operating system and listens for changes in a certain directory with the file watcher API. In this way, we are able to allocate resources to other, more important tasks.

## How it works

It starts on the Raspberry Pi; there will be an observer watching for new files being written to a certain file directory using the Python framework Watchdog. From there, a POST request will be made to the object detection script to detect at what location the shape is. Then, if object detection is confident enough, it will save the bounding box coordinates and send a cropped image via a POST request off to color and alphanumeric recognition. It will then save the outcomes of the color and alphanumeric recognition scripts into the database. Finally, it will send off the results to the interoperatbility network.
