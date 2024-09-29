import schedule
import time
from datetime import datetime

'''
A Time-Based Nitrogen Wallpaper Swapper for Linux

Author: Edison Modesto
Description: This script will automatically change your desktop wallpaper to a desired image based on the time of day using Nitrogen.
'''

# Paths of the images that i used for this script
morningImagePath = "/home/a4meta/Pictures/tropic_island_morning.jpg"
dayImagePath = "/home/a4meta/Pictures/tropic_island_day.jpg"
eveningImagePath = "/home/a4meta/Pictures/tropic_island_evening.jpg"
nightImagePath = "/home/a4meta/Pictures/tropic_island_night.jpg"

def swapWallpaper(pathToImage):
    print("Swapping wallpaper using nitrogen...")
    # TODO: Add code to swap wallpaper using nitrogen

def monitor_time():
    # will monitor if there are tasks scheduled, and run them if there are any
    while True:
        schedule.run_pending()
        # Sleep for 60 seconds before checking again to avoid a busy loop
        time.sleep(60)
        

def check_time():
    # TODO: Add code to check if the current time is within the specified time range and run the swapWallpaper function with the appropriate image path
    pass
        
# Schedule the swapWallpaper function to run on the specified time with the specified image path to be used
schedule.every().day.at("6:00").do(swapWallpaper(morningImagePath))
schedule.every().day.at("12:00").do(swapWallpaper(dayImagePath))
schedule.every().day.at("17:00").do(swapWallpaper(eveningImagePath))
schedule.every().day.at("22:00").do(swapWallpaper(nightImagePath))


if __name__ == "__main__":
    check_time()
    monitor_time()
    


