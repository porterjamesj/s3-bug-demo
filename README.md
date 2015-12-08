# S3 bug demo

A demo of the bug described in an upcoming blog post of mine.

To reproduce:

1. Make a new virtualenv and activate it
2. `pip install -r requirements.txt`
3. Start a moto server in the background: `moto_server s3bucket_path &`. Moto is a library that implements a fake s3 for use in testing.
4. Run `python create_test_object.py`. This will write a gigabyte of random data to a test key in the moto s3 (in memory, so make sure you have a least a GB of memory available)
5. Run `python app.py &` to start the flask server in the background.
6. `curl http://127.0.0.1:5001/test > /dev/null` to retrieve the GB of random test data and send it to /dev/null. Everything will be fine
7. `curl http://127.0.0.1:5001/test | head -c 10` and watch the memory usage of the server balloon to roughly a gigabyte just *after* the command returns.
