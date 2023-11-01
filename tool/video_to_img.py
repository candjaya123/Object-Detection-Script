import cv2
import os
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Split a video into individual frames')
parser.add_argument('video_path', help='Path to the input video file')
parser.add_argument('output_folder', help='Path to the output folder for frames')
args = parser.parse_args()

# Input video file path
video_path = args.video_path

# Output folder to save frames
output_folder = args.output_folder

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the frames per second (fps) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the frame interval to capture 2 frames per second
frame_interval = int(fps / 2)

# Get the total number of frames in the video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Read and save each frame
frame_number = 0
frame_count_per_second = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_number % frame_interval == 0:
        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count_per_second:04d}.png")
        cv2.imwrite(frame_filename, frame)

        frame_count_per_second += 1

        # Display progress
        if frame_count_per_second % 2 == 0:
            print(f"Processed {frame_count_per_second} frames (2 images per second)")

    frame_number += 1

# Release the video capture object
cap.release()

print("Video frames extracted and saved to", output_folder)
