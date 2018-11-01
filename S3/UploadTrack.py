#To track the progress of a transfer, a progress callback can be provided such that the callback gets invoked each time progress is made on the transfer:

import os
import sys
import threading

import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt.large"

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


# Get the service client
s3 = boto3.client('s3')

# Upload tmp.txt to s3_bucket at key-name
s3.upload_file(
    s3_file, s3_bucket, s3_file,
    Callback=ProgressPercentage(s3_file))
