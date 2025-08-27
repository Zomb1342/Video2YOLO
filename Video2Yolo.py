import cv2
import os

def prepare_yolo_dataset(
    video_path,
    output_folder,
    skip_frames=1
):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % skip_frames == 0:
            base_filename = f"frame_{saved_count:05d}"
            
            # Save image without resizing
            image_path = os.path.join(output_folder, base_filename + ".jpg")
            cv2.imwrite(image_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            
            # Create empty YOLO annotation file
            label_path = os.path.join(output_folder, base_filename + ".txt")
            open(label_path, 'w').close()

            saved_count += 1

        frame_count += 1

    cap.release()
    print(f" Prepared {saved_count} frames and empty YOLO labels in '{output_folder}'.")

# Example usage
prepare_yolo_dataset("your_video.mp4", "yolo_dataset", skip_frames=1)
