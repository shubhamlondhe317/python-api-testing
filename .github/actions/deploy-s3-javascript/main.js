const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');


function run(){

    const bucket = core.getInput('bucket', {required:true});
    const bucketRegion = core.getInput('bucket_region', {required:true});
    const distFolder = core.getInput('dist_folder', {required:true});

    const s3Uri = `s3://${bucket}`;
    exec.exec(`aws s3 sync ${}distFolder ${s3Uri} --region ${bucketRegion}`);

    core.notice('custom javascript actions');

}

run();