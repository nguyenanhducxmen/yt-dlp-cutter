import os
from .utils import convert_time

def cut_video(ffmpeg_path, input_file, start_time, end_time, output_file):
    start = convert_time(start_time)
    end = convert_time(end_time)
    duration = end - start
    os.system(f'"{ffmpeg_path}" -v quiet -stats -ss {start} -t {duration} -i "{input_file}" -y -c:v libx264 "{output_file}"')
