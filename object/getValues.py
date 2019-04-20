import argparse
from pipeline.models import Metadata

# Script to communicate from the CPP script to python and save the object to the database

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--object"), help="object")
    parser.add_argument("--i", help="image file")
    parser.add_argument("--p", help="image path")
    args = parser.parse_args()

    Metadata.objects.get(image_name=body['image_name']).update(object=object)

    # return {
    #     'image_path': args.p,
    #     'image_file': args.i,
    #     'object': args.object
    # }



