import json
import pytube
import speedtest
import time
from channels.generic.websocket import WebsocketConsumer


class ProgressConsumer(WebsocketConsumer):
    
    def connect(self):
        # Accept the WebSocket connection
        self.accept()

    def disconnect(self, close_code):
        # Handle WebSocket disconnection
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        url = text_data_json.get('url')

        if url:
            try:
                # Fetch YouTube video details
                yt = pytube.YouTube(url)
                stream = yt.streams.get_highest_resolution()


                 # Get YouTube video thumbnail URL
                thumbnail_url = yt.thumbnail_url

                # Send thumbnail URL
                self.send(text_data=json.dumps({
                    'type': 'thumbnail',
                    'message': thumbnail_url,
                }))



                # send title
                title = yt.title
                # send title
                self.send(text_data=json.dumps({
                    'type': 'title',
                    'message': title,
                }))


                # Get the file size
                file_size = stream.filesize  # in bytes
                file_size_mb = file_size / (1024 * 1024)  # convert to megabytes

                # Send file size
                self.send(text_data=json.dumps({
                    'type': 'size',
                    'message': f" File Size : {file_size_mb:.2f} MB",
                }))



                # Get the download speed
                st = speedtest.Speedtest()
                st.get_best_server()
                download_speed = st.download() / 8  # convert to bytes per second
                download_speed_mbps = download_speed * 8 / (1024 * 1024)  # convert to megabits per second

                # Send download speed
                self.send(text_data=json.dumps({
                    'type': 'speed',
                    'message': f' Download speed : {download_speed_mbps:.2f} Mbps',
                }))



                # Estimate download time
                estimated_time = file_size / download_speed  # in seconds

                # Send estimated download time
                self.send(text_data=json.dumps({
                    'type': 'est',
                    'message': f" Est Download time : {estimated_time:.2f} seconds.Please wait for the download to complete",
                }))

                # Download the video and measure the actual time taken
                start_time = time.time()
                stream.download()
                end_time = time.time()

                actual_time = end_time - start_time

                # Send complete message
                self.send(text_data=json.dumps({
                    'type': 'update',
                    'message': f"Download complete in time {actual_time:.2f} Seconds ",
                }))



            except Exception as e:
                # Handle exceptions
                self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': str(e),
                }))

    def size(self, event):
        self.send(text_data=json.dumps(event))

    def speed(self, event):
        self.send(text_data=json.dumps(event))

    def est(self, event):
        self.send(text_data=json.dumps(event))

    def error(self, event):
        self.send(text_data=json.dumps(event))

    def thumbnail(self, event):
        self.send(text_data=json.dumps(event))

    def update(self, event):
        self.send(text_data=json.dumps(event))

    def title(self, event):
        self.send(text_data=json.dumps(event))
