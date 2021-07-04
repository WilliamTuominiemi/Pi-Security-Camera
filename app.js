const express = require('express')
var fs = require('fs');
var path = require('path');
const { exec } = require('child_process');
const https = require('https')

const app = express()

app.use('/static', express.static(path.join(__dirname, 'public')))
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  // const options = {
  //   hostname: 'http://127.0.0.1:5000/',
  //   method: 'GET'
  // }

  // const _req = https.request(options, _res => {
  //   console.log(`statusCode: ${_res.statusCode}`)

  //   _res.on('data', d => {
  //     process.stdout.write(d)
  //   })
  // })

  // _req.on('error', error => {
  //   console.error(error)
  // })

  // _req.end()

  res.render('index.ejs');
})

app.get('/image', (req, res) => {
  console.log('request received')
  exec(`raspistill -o ${path.resolve(__dirname, 'images/image.jpg')}`, (err, stdout, stderr) => {
    if (err) {
      console.log("node couldn't execute the command")
      return;
    }

    console.log('Success')

    res.writeHead(200, { "Content-Type": "image/jpg" });

    fs.createReadStream(path.resolve(__dirname, 'images/image.jpg'))
      .pipe(res);
  });
})

app.listen(3000)