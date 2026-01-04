import instaloader
import os
import re
from config.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, VIDEO_OUTPUT_DIR

class InstagramDownloader:
    def __init__(self):
        self.loader = instaloader.Instaloader()
        if INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD:
            try:
                self.loader.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            except Exception as e:
                print(f"Login failed: {e}")
        # Set download directory
        self.loader.dirname_pattern = VIDEO_OUTPUT_DIR

    def extract_shortcode(self, url):
        # Extract shortcode from Instagram URL
        match = re.search(r'/reel/([A-Za-z0-9_-]+)', url)
        if match:
            return match.group(1)
        return None

    def download_reel(self, url):
        shortcode = self.extract_shortcode(url)
        if not shortcode:
            raise ValueError("Invalid Instagram reel URL")

        try:
            post = instaloader.Post.from_shortcode(self.loader.context, shortcode)
            self.loader.download_post(post, target=VIDEO_OUTPUT_DIR)
            # Find the downloaded video file
            for file in os.listdir(VIDEO_OUTPUT_DIR):
                if file.endswith('.mp4') and shortcode in file:
                    return os.path.join(VIDEO_OUTPUT_DIR, file)
            return None
        except Exception as e:
            raise Exception(f"Failed to download reel: {e}")

if __name__ == "__main__":
    downloader = InstagramDownloader()
    url = "https://www.instagram.com/reel/example_shortcode/"
    video_path = downloader.download_reel(url)
    print(f"Downloaded to: {video_path}")