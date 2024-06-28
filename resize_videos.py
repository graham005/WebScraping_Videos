import os
import subprocess

# Define the folder containing the videos
folder_path = r"C:\Users\The Elder\Downloads\Airplanes"

# Define the output resolution
width = 720
height = 720

# Function to resize a video
def resize_video(input_path, output_path, width, height):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', f'scale={width}:{height}',
        output_path
    ]
    subprocess.run(command, check=True)

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add more video extensions if needed
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(folder_path, f'resized_{filename}')
        resize_video(input_file, output_file, width, height)

print("All videos have been resized.")
