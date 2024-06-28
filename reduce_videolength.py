import os
from moviepy.editor import VideoFileClip

# Define the folder containing the videos
folder_path = r"C:\Users\The Elder\Downloads\Airplanes\reduce_length" # Add folder directory

# Function to trim video length to 40 seconds if it's longer than 59 seconds
def trim_video_length(video_path, max_length=59, target_length=40):
    clip = VideoFileClip(video_path)
    if clip.duration > max_length:
        trimmed_clip = clip.subclip(0, target_length)
        output_path = os.path.join(folder_path, f'trimmed_{os.path.basename(video_path)}')
        trimmed_clip.write_videofile(output_path, codec="libx264")
        print(f"Trimmed {video_path} to {output_path}")
    else:
        print(f"{video_path} is not longer than {max_length} seconds.")

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add more video extensions if needed
        video_file = os.path.join(folder_path, filename)
        
        # Check and trim the video length if needed
        trim_video_length(video_file)

print("All videos have been processed.")
