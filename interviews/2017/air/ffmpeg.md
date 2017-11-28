
# Faster, avoids re-encoding but only works on files of the same type
ffmpeg -i "concat:lake.mp4|lake.mp4" -c copy output.mp4


# Slower, re-encodes files but works for any combination of file types
## Note that n=#, where # is the number of items
ffmpeg -i lake.mp4 -i prom.mp4 \
-filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]" \
-map "[outv]" -map "[outa]" output.mp4