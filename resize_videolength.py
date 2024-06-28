import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define the folder containing the videos
folder_path = r"C:\Users\The Elder\Downloads\Airplanes" # Add folder directory

# Function to extend video length to at least 15 seconds
def extend_video_length(video_path, min_length=15):
    clip = VideoFileClip(video_path)
    if clip.duration < 10:
        # Loop the video until it reaches the desired length
        loops = int(min_length // clip.duration) + 1
        extended_clip = concatenate_videoclips([clip] * loops)
        extended_clip = extended_clip.subclip(0, min_length)
        output_path = os.path.join(folder_path, f'extended_{os.path.basename(video_path)}')
        extended_clip.write_videofile(output_path, codec="libx264")
        print(f"Extended {video_path} to {output_path}")
    else:
        print(f"{video_path} is already longer than 10 seconds.")

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add more video extensions if needed
        video_file = os.path.join(folder_path, filename)
        
        # Check and extend the video length if needed
        extend_video_length(video_file)

print("All videos have been processed.")
