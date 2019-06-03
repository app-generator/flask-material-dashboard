var FtpDeploy = require('ftp-deploy');
var ftpDeploy = new FtpDeploy();
 
var config = {
    user: "FTP_USER", 
    password: "FTP_PASS",                            
    host: "FTP_HOST",
    port: 21,
    localRoot: __dirname + '/app/build',
    remoteRoot: '/',
    include: ['*', '**/*'],      // this would upload everything except dot files
    //include: ['*.php', 'dist/*'],
    exclude: ['dist/**/*.map'],     // e.g. exclude sourcemaps - ** exclude: [] if nothing to exclude **
    deleteRemote: false,              // delete ALL existing files at destination before uploading, if true
    forcePasv: false                 // Passive mode is forced (EPSV command is not sent)
}
 
// use with promises
ftpDeploy.deploy(config)
    .then(res => console.log('finished:', res))
    .catch(err => console.log(err))

ftpDeploy.on('uploading', function(data) {
    data.totalFilesCount;       // total file count being transferred
    data.transferredFileCount; // number of files transferred
    data.filename;             // partial path with filename being uploaded
});

ftpDeploy.on('uploaded', function(data) {
    console.log(data);         // same data as uploading event
});

ftpDeploy.on('log', function(data) {
    console.log(data);         // same data as uploading event
});

ftpDeploy.on('upload-error', function (data) {
    console.log(data.err); // data will also include filename, relativePath, and other goodies
});
