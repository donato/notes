import ffmpeg


def concat(head, tail, output):

    head_file = ffmpeg.input(head)
    tail_file = ffmpeg.input(tail)
    (ffmpeg
        .concat(
            head_file,
            tail_file
        )
        .output(output)
        .run()
     )

