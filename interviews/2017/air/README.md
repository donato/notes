# Airlabs Coding Challenge

*Goal:* Demonstrate ability to manipulate video in the cloud.

*Task:*
Write a web service which:
- Accepts an HTTP request to the service with paths to two publicly accessible input MP4 files
- Accepts an access token for security
- Concatenates two video files into one
- Provides a response indicating that the job has completed
- Provides a link to the outputted MP4 file once the job has completed
- Write the resulting video file to a configurable destination (local or remote)

### Scope
- Don't worry about concurrency or error-handling

Start time: 7pm EST
Stop at 9:10pm
Resume at 9:50pm

### API
```json
POST \<api\>/concat/
POST BODY {
    head: {
        url: 'path to publicly accessible mp4 file'
    },
    tail: {
        url: 'path to publicly accessible mp4 file'
    },
    output: {
        type: 'local', # or s3
        path: '~/hi/'
    },
    authorization: 'YOUR_SECRET_HERE',
    webhooks: {
        url: 'abc'
    }
}

Response 200
```

## How to run

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
python run.py

# In a separate terminal
curl \
    -H "Content-Type: application/json" \
    -X POST -d \
    '{"head": {"url": "lake.mp4"}, 
      "tail": {"url": "lake.mp4"}, 
      "output": { 
          "type": "local", 
          "location": "output.mp4" 
      },
    "authorization":"xyz",
    "webhook_url": "url"}' \
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
https://github.com/kkroening/ffmpeg-python
https://trac.ffmpeg.org/wiki/Concatenate#differentcodec
https://github.com/opencoconut/ffmpeg
