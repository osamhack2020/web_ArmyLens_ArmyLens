from google_images_download import google_images_download 

response = google_images_download.googleimagesdownload() 

arguments = {"keywords":"MM-1 Minimore","limit":200,"print_urls":True, "format": "png"}   #creating list of arguments
paths = response.download(arguments) 
print(paths) 