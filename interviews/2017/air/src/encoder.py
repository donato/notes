import uuid

import ffmpeg

def concat(head, tail):

    tmp_file= "/tmp/{salt}.mp4".format(salt=uuid.uuid4())
    head_file = ffmpeg.input(head)
    tail_file = ffmpeg.input(tail)
    (ffmpeg
        .concat(
            head_file,
            tail_file
        )
        .output(tmp_file)
        # https://github.com/kkroening/ffmpeg-python/blob/7669492575141c13b63fd89dde8b44ecf6bf31cb/ffmpeg/_ffmpeg.py#L28
        .overwrite_output() # -y option
        .run()
    )
    return tmp_file

