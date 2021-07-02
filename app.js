var http = require('http');
var fs = require('fs');
var path = require('path');
const { exec } = require('child_process');

http.createServer(function (req, res) {
    console.log('request received')
    console.log(`raspistill -o ${path.resolve(__dirname, 'image.jpg')}`)
    exec(`raspistill -o ${path.resolve(__dirname, 'image.jpg')}`, (err, stdout, stderr) => {
        if (err) {
          // node couldn't execute the command
          return;
        }

        res.writeHead(200, {"Content-Type": "image/jpg"});

        fs.createReadStream(path.resolve(__dirname, 'image.jpg')) 
        .pipe(res);
    });
}).listen(process.env.PORT || '3000'); // provide a default  