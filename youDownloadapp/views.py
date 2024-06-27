from django.shortcuts import render
from django.http import HttpResponse
import time
import pytube
import speedtest

# Create your views here.
def index(request):
    return render(request,'index.html')


def download(request):
    if request.method == 'POST':
        url = request.POST.get('video')
        if url:
            yt = pytube.YouTube(url)
            stream = yt.streams.get_highest_resolution()

            # Get the file size
            file_size = stream.filesize  # in bytes
            file_size_mb = file_size / (1024 * 1024)  # convert to megabytes

            # Get the download speed
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / 8  # convert to bytes per second
            download_speed_mbps = download_speed * 8 / (1024 * 1024)  # convert to megabits per second

            # Estimate download time
            estimated_time = file_size / download_speed  # in seconds

            # Download the video and measure the actual time taken
            start_time = time.time()
            stream.download(output_path= 'C:/Users/wekes/Downloads')
            end_time = time.time()

            actual_time = end_time - start_time

            # return HttpResponse(f'''
            #     <p>File size: {file_size_mb:.2f} MB</p>
            #     <p>Download speed: {download_speed_mbps:.2f} Mbps</p>
            #     <p>Estimated download time: {estimated_time:.2f} seconds</p>
            #     <p>Actual download time: {actual_time:.2f} seconds</p>
            #         ''')

            context = {
            'size': f"{file_size_mb:.2f}",
            'speed': f"{download_speed_mbps:.2f}",
            'estTime': f"{estimated_time:.2f}",
            'time': f"{actual_time:.2f}",}


            return render(request,'downPage.html',)