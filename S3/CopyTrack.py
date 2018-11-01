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
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            sys.stdout.write(
                "\r%s --> %s bytes transferred" % (
                    self._filename, self._seen_so_far))
            sys.stdout.flush()

# Get the service client
s3 = boto3.client('s3')

# Copies object located in mybucket at mykey
# to the location otherbucket at otherkey
copy_source = {
    'Bucket': s3_bucket,
    'Key': s3_file
}
s3.copy(copy_source, "test-uala2", s3_file,
        Callback=ProgressPercentage("test-uala2"))
# Note that the granularity of these callbacks will be much larger than the upload and download methods
# because copies are all done server side and so there is no local file to track the streaming of data.
