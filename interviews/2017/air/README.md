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


