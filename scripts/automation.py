import logging
import os
import shutil
from config.config import LOG_FILE
from scripts.instagram_downloader import InstagramDownloader
from scripts.video_editor import VideoEditor
from scripts.facebook_uploader import FacebookUploader
from scripts.database import Database

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add console logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

class Automation:
    def __init__(self):
        self.downloader = InstagramDownloader()
        self.editor = VideoEditor()
        self.uploader = FacebookUploader()
        self.db = Database()

    def process_reel(self, reel_url, description=""):
        try:
            logging.info(f"Starting processing for {reel_url}")

            # Download
            video_path, caption = self.downloader.download_reel(reel_url)
            logging.info(f"Downloaded: {video_path}")

            # Use caption as description if no description provided
            if not description:
                description = caption

            # Edit
            edited_path = self.editor.modify_video(video_path)
            logging.info(f"Edited: {edited_path}")

            # Upload
            results = self.uploader.upload_to_all_pages(edited_path, description)
            logging.info(f"Uploaded: {results}")

            # Save to DB
            self.db.insert_upload(reel_url, video_path, edited_path, results)
            logging.info("Saved to database")

            # Clean up files
            target_dir = os.path.dirname(video_path)
            shutil.rmtree(target_dir)
            os.remove(edited_path)
            logging.info("Cleaned up files")

            return {"status": "success", "results": results}

        except Exception as e:
            logging.error(f"Error processing {reel_url}: {e}")
            return {"status": "failed", "error": str(e)}

if __name__ == "__main__":
    automation = Automation()
    result = automation.process_reel("https://www.instagram.com/reel/example/")
    print(result)