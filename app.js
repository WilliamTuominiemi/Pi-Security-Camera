const express = require('express')
var fs = require('fs');
var path = require('path');

const app = express()

const port = 3000

const videoStream = require('./videoStream');
videoStream.acceptConnections(app, {
  width: 1280,
  height: 720,
  fps: 16,
  encoding: 'JPEG',
  quality: 7
},
  '/stream.mjpg', true
);

app.use(express.static(__dirname + '/public'));
app.listen(3000, "0.0.0.0", () => console.log(`Example app listening on port ${port}! In your web browser, navigate to http://<IP_ADDRESS_OF_THIS_SERVER>:3000`));