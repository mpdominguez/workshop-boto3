#To track the progress of a transfer, a progress callback can be provided such that the callback gets invoked each time progress is made on the transfer:

import sys
import threading

import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt.large"

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single.large filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            sys.stdout.write(
                "\r%s --> %s bytes transferred" % (
                    self._filename, self._seen_so_far))
            sys.stdout.flush()

# Get the service client
s3 = boto3.client('s3')

# Download object at s3_bucket with key-name to tmp.txt
s3.download_file(
    s3_bucket, s3_file, s3_file,
    Callback=ProgressPercentage(s3_file))
