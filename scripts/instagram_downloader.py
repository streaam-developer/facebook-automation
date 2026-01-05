import instaloader
import os
import re
from config.config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, VIDEO_OUTPUT_DIR

class InstagramDownloader:
    def __init__(self):
        self.loader = instaloader.Instaloader()
        # No login needed for public reels
        # dirname_pattern will be set per download

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

        target_dir = os.path.join(VIDEO_OUTPUT_DIR, shortcode)
        try:
            self.loader.dirname_pattern = target_dir
            post = instaloader.Post.from_shortcode(self.loader.context, shortcode)
            self.loader.download_post(post, target='.')
            # Find the downloaded video file
            for file in os.listdir(target_dir):
                if file.endswith('.mp4'):
                    return os.path.join(target_dir, file)
            return None
        except Exception as e:
            raise Exception(f"Failed to download reel: {e}")

if __name__ == "__main__":
    downloader = InstagramDownloader()
    url = "https://www.instagram.com/reel/example_shortcode/"
    video_path = downloader.download_reel(url)
    print(f"Downloaded to: {video_path}")