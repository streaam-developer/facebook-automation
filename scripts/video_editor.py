from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import os
from config.config import EDITED_VIDEO_DIR

class VideoEditor:
    def __init__(self):
        os.makedirs(EDITED_VIDEO_DIR, exist_ok=True)

    def add_watermark(self, video_path, watermark_text="Edited", output_path=None):
        if not output_path:
            base_name = os.path.basename(video_path)
            output_path = os.path.join(EDITED_VIDEO_DIR, f"edited_{base_name}")

        clip = VideoFileClip(video_path)

        # Create text clip for watermark
        txt_clip = TextClip(watermark_text)
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(clip.duration)

        # Composite the video with watermark
        video_with_watermark = CompositeVideoClip([clip, txt_clip])

        # Write the result to a file
        video_with_watermark.write_videofile(output_path, codec='libx264', audio_codec='aac')

        return output_path

    def modify_video(self, video_path, output_path=None):
        # For copyright prevention, add watermark and perhaps speed up slightly or add effects
        return self.add_watermark(video_path, output_path=output_path)

if __name__ == "__main__":
    editor = VideoEditor()
    edited_path = editor.modify_video("data/videos/example.mp4")
    print(f"Edited video: {edited_path}")