#launches the webapp on a specified host and port
from flask import Flask
from ssapp import app

if __name__=='__main__':
    app.run(
        host='0.0.0.0',
        port=5065,
        threaded=True
    )

