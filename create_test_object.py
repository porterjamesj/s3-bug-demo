from boto.s3.connection import OrdinaryCallingFormat
from boto import connect_s3

import random
import string

from cStringIO import StringIO


def main():
    conn = connect_s3(
        "fake_access", "fake_secret",
        host="localhost", port=5000,
        is_secure=False,
        calling_format=OrdinaryCallingFormat()
    )
    buck = conn.create_bucket("test")
    print "created bucket {}".format(buck)
    mp = buck.initiate_multipart_upload("test")
    print "started multipart upload {}".format(mp)
    print "generating random test data"
    sio = StringIO(''.join(random.choice(string.ascii_uppercase + string.digits)
                           for _ in range(10000000)))
    for i in range(1, 101):
        sio.seek(0)
        print "uploading part {}/100".format(i)
        mp.upload_part_from_file(sio, i)
    print "completing upload"
    mp.complete_upload()


if __name__ == "__main__":
    main()
