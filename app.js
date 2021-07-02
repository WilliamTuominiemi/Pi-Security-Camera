const express = require('express')
var fs = require('fs');
var path = require('path');
const { exec } = require('child_process');

const app = express()

app.get('/', function (req, res) {
  console.log('request received')
  console.log(`raspistill -o ${path.resolve(__dirname, 'image.jpg')}`)
  exec(`raspistill -o ${path.resolve(__dirname, 'image.jpg')}`, (err, stdout, stderr) => {
    if (err) {
      // node couldn't execute the command
      return;
    }

    res.writeHead(200, { "Content-Type": "image/jpg" });

    fs.createReadStream(path.resolve(__dirname, 'image.jpg'))
      .pipe(res);
  });
})

app.listen(3000)