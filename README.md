# Facebook Automation - Instagram Reel Uploader

This project automates the process of downloading Instagram reels, editing them to prevent copyright issues, and uploading them to multiple Facebook pages. It includes a web interface for easy management and MongoDB for tracking uploads.

## Features

- Download Instagram reels from URLs
- Automatic video editing (watermark addition) for copyright prevention
- Upload edited videos to multiple Facebook pages
- Web dashboard to input reel links and view upload history
- MongoDB integration for tracking upload status
- Logging for debugging and monitoring

## Setup

1. **Clone the repository and navigate to the directory**

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Fill in your credentials:
     - `MONGO_URI`: MongoDB connection string
     - `FACEBOOK_ACCESS_TOKEN`: Facebook access token with publish_video permission
     - `FACEBOOK_PAGE_IDS`: Comma-separated list of Facebook page IDs
     - `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD`: Optional, for Instagram login
     - `SECRET_KEY`: Flask secret key

4. **Install MongoDB** (if not already installed)
   - Start MongoDB service

5. **Install FFmpeg** (required for video processing)
   - Download from https://ffmpeg.org/download.html

6. **Run the web application**
   ```
   python web/app.py
   ```
   - Open http://localhost:5000 in your browser

## Usage

1. Open the web interface
2. Enter an Instagram reel URL and optional description
3. Click "Upload to Facebook"
4. View the upload history and status on the dashboard

## API Permissions

- **Facebook**: Ensure your access token has `publish_video` permission for the pages
- **Instagram**: Login credentials are optional but may help with rate limits

## Project Structure

- `scripts/`: Core automation modules
  - `automation.py`: Main automation logic
  - `instagram_downloader.py`: Instagram reel downloader
  - `video_editor.py`: Video editing for copyright prevention
  - `facebook_uploader.py`: Facebook upload handler
  - `database.py`: MongoDB operations
- `web/`: Flask web application
  - `app.py`: Flask app
  - `templates/`: HTML templates
- `config/`: Configuration files
- `data/`: Downloaded and edited videos
- `logs/`: Application logs

## Notes

- Videos are edited by adding a watermark to help prevent copyright claims
- All uploads are logged in MongoDB with status tracking
- The system handles multiple Facebook pages simultaneously
- Error handling is implemented throughout for robustness