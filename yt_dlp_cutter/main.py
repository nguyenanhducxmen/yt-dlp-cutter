import os
from .downloader import download
from .utils import select_path
from .cutter import cut_video

def main():
    video_link = input("Enter video URL: ")
    output_name = input("Enter output filename (default: output.mp4): ") or "output.mp4"
    output_path = select_path("Select output directory")
    
    os.system(f'yt-dlp "{video_link}" -o "input.mp4" --merge-output-format mp4')
    
    if os.path.isfile("input.mp4"):
        start_time = input("Enter start time (hh:mm:ss): ")
        end_time = input("Enter end time (hh:mm:ss): ")
        cut_video("ffmpeg.exe", "input.mp4", start_time, end_time, os.path.join(output_path, output_name))
    
    print(f"Exported video: {output_path}{output_name}")

if __name__ == "__main__":
    main()
