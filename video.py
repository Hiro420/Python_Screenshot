from pyffmpeg import FFmpeg
ff = FFmpeg()
ff.options("-i input.mp4 -i .\\images\\output-onlinepngtools.png -filter_complex overlay=0:0 output.mp4")