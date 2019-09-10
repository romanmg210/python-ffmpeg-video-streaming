import os
import sys
import ffmpeg_streaming
from ffmpeg_streaming import Representation


def progress(percentage, line, all_media):
    # You can update a field in your database
    # You can also create a socket connection and show a progress bar to users
    sys.stdout.write("\r Transcoding... (%s%%)[%s%s]" % (percentage, '#' * percentage, '-' * (100 - percentage)))
    sys.stdout.flush()


def create_dash_files(_input, _output, __progress=None):
    rep1 = Representation(width=256, height=144, kilo_bitrate=200)
    rep2 = Representation(width=426, height=240, kilo_bitrate=500)
    rep3 = Representation(width=640, height=360, kilo_bitrate=1000)

    (
        ffmpeg_streaming
            .dash(_input, adaption='"id=0,streams=v id=1,streams=a"')
            .format('libx265')
            .add_rep(rep1, rep2, rep3)
            .package(_output, __progress)
    )


if __name__ == "__main__":
    create_dir = os.path.basename(__file__).split('.')[0]
    current_dir = os.path.dirname(os.path.abspath(__file__))

    _input = os.path.join(current_dir, '_example.mp4')
    _output = os.path.join(current_dir, create_dir, 'output')

    _progress = progress

    create_dash_files(_input, _output, _progress)
