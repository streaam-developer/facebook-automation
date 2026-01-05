import requests
import os
from config.config import FACEBOOK_ACCESS_TOKEN, FACEBOOK_PAGE_IDS

class FacebookUploader:
    def __init__(self):
        self.access_token = FACEBOOK_ACCESS_TOKEN
        self.page_ids = []
        self.page_tokens = self.get_page_tokens()

    def get_page_tokens(self):
        url = f"https://graph.facebook.com/v18.0/me/accounts?access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tokens = {}
            for page in data.get('data', []):
                page_id = page['id']
                tokens[page_id] = page['access_token']
                self.page_ids.append(page_id)
            return tokens
        else:
            raise Exception(f"Failed to get page tokens: {response.text}")

    def upload_to_page(self, page_id, video_path, description=""):
        if page_id not in self.page_tokens:
            raise Exception(f"No access token for page {page_id}")
        url = f"https://graph.facebook.com/v18.0/{page_id}/videos"
        files = {'source': open(video_path, 'rb')}
        data = {
            'access_token': self.page_tokens[page_id],
            'description': description
        }
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to upload: {response.text}")

    def upload_to_all_pages(self, video_path, description=""):
        results = {}
        for page_id in self.page_ids:
            try:
                result = self.upload_to_page(page_id, video_path, description)
                results[page_id] = {'status': 'success', 'id': result.get('id')}
            except Exception as e:
                results[page_id] = {'status': 'failed', 'error': str(e)}
        return results

if __name__ == "__main__":
    uploader = FacebookUploader()
    results = uploader.upload_to_all_pages("data/edited_videos/edited_example.mp4", "Test upload")
    print(results)