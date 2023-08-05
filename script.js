var fs = require('fs');
var plist = require('plist');

if (process.argv.length <= 2) {
    console.log('Usage: <input-file>');
    return;
}

var obj = plist.parse(fs.readFileSync(process.argv[2], 'utf8'));
console.log(JSON.stringify(obj));
