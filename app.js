const express = require('express')
var fs = require('fs');
var path = require('path');
const { exec } = require('child_process');
const https = require('https')

const app = express()

const port = 3000

// app.use('/static', express.static(path.join(__dirname, 'public')))
// app.set('view engine', 'ejs');

// start capture
const videoStream = require('./videoStream');
videoStream.acceptConnections(app, {
  width: 1280,
  height: 720,
  fps: 16,
  encoding: 'JPEG',
  quality: 7 // lower is faster, less quality
},
  '/stream.mjpg', true
);

// app.get('/image', (req, res) => {
//   console.log('request received')
//   exec(`raspistill -o ${path.resolve(__dirname, 'images/image.jpg')}`, (err, stdout, stderr) => {
//     if (err) {
//       console.log("node couldn't execute the command")
//       return;
//     }

//     console.log('Success')

//     res.writeHead(200, { "Content-Type": "image/jpg" });

//     fs.createReadStream(path.resolve(__dirname, 'images/image.jpg'))
//       .pipe(res);
//   });
// })

app.use(express.static(__dirname + '/public'));
app.listen(port, () => console.log(`Example app listening on port ${port}! In your web browser, navigate to http://<IP_ADDRESS_OF_THIS_SERVER>:3000`));