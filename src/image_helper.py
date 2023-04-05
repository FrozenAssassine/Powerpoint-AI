from bing_image_downloader import downloader

def get_image_topic(topic):
    downloader.download(topic, limit=5,  output_dir='images', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)