const express = require('express')

const app = express()

const port = 3000

const videoStream = require('./util/videoStream')

videoStream.acceptConnections(app, {
  width: 1280,
  height: 720,
  fps: 24,
  encoding: 'JPEG',
  quality: 10
},
  '/stream.mjpg', true
)

app.use(express.static(__dirname + '/public'))

app.listen(port, "0.0.0.0", () => console.log(`Listening on port ${port}`))