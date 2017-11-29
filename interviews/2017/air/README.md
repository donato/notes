# Airlabs Coding Challenge

### Scope
*Goal:* Demonstrate ability to manipulate video in the cloud.

*Task:*
Write a web service which:
- Accepts an HTTP request to the service with paths to two publicly accessible input MP4 files
- Accepts an access token for security
- Concatenates two video files into one
- Provides a response indicating that the job has completed
- Provides a link to the outputted MP4 file once the job has completed
- Write the resulting video file to a configurable destination (local or remote)
- Don't worry about concurrency or error-handling


### API

```sh
POST \<api\>/concat/
POST BODY {
    head: {
        path: 'path to publicly accessible mp4 file',
        location: 'web' # or 'local'
    },
    tail: {
        path: 'path to publicly accessible mp4 file',
        location: 'web'
    },
    output: {
        type: 'web' # or 'local'
    },
    authorization: 'YOUR_SECRET_HERE'
}

POST Response {
    "output": "path to your concatted video file"
}
```

### How to run

Setup:
```sh
# First we need to have ffmpeg installed
brew install ffmpeg

# Then get these files
mkdir -p ~/git/
cd ~/git/
git clone git@github.com:donato/notes.git
cd notes/interviews/2017/air

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Now update your secrets in the secrets.yml file
cp secrets.yml.template secrets.yml

# Download test videos
curl https://s3.amazonaws.com/donato/lake.mp4 > ~/git/notes/interview/2017/air/test/lake.mp4
curl https://s3.amazonaws.com/donato/prom.mp4 > ~/git/notes/interview/2017/air/test/prom.mp4
```

To test it:
```sh
# In one terminal start the api
cd ~/git/notes/interviews/2017/air
source/venv/bin/activate
python run.py

# In a separate terminal run these test commands
## To test local files with local output
curl \
    -H "Content-Type: application/json" \
    -X POST -d \
    '{"head": {"path": "test/prom.mp4", "location": "local"}, 
      "tail": {"path": "test/lake.mp4", "location": "local"}, 
      "output": { 
          "type": "local"
      },
    "authorization":"abc"}' \
    localhost:9009/concat/
    
## To test files in the cloud, uploaded to the cloud
curl \
    -H "Content-Type: application/json" \
    -X POST -d \
    '{"head": {"path": "https://s3.amazonaws.com/donato/lake.mp4", "location": "web"}, 
      "tail": {"path": "https://s3.amazonaws.com/donato/prom.mp4", "location": "web"}, 
      "output": { 
          "type": "web"
      },
    "authorization":"abc"}' \
    localhost:9009/concat/
```


## Things I googled
*Round 1*
* https://stackoverflow.com/questions/43069780/how-to-create-virtual-env-with-python3
* https://bitmovin.com/webhooks-encoding-api/
* https://superuser.com/questions/1059245/ffmpeg-join-two-mp4-files-with-ffmpeg-on-command-line
* https://stackoverflow.com/questions/7172784/how-to-post-json-data-with-curl-from-terminal-commandline-to-test-spring-rest
* http://flask-restful.readthedocs.io/en/latest/quickstart.html

*Round 2*
* https://github.com/kkroening/ffmpeg-python
* https://trac.ffmpeg.org/wiki/Concatenate#differentcodec
* https://github.com/opencoconut/ffmpeg

*Round 3*
* https://github.com/boto/boto3/issues/330
* https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
* http://docs.python-requests.org/en/master/user/quickstart/

