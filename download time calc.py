redo = "Yes"

while redo in ("Yes","yes"):
    download_size = float(input("Enter your download size in GB. "))

    download_speed = float(input("Enter your download speed in Mbit/s. "))

    download_time_seconds = round(float((download_size*1024)/(download_speed/8)), 2)
    download_time_minutes = round(float(download_time_seconds/60), 2)
    download_time_hours = round(float(download_time_minutes/60), 2)
    download_time_minutes_remainder = round(float(download_time_minutes % 60), 2)

    print(download_size,"will take",download_time_seconds,"seconds,",download_time_minutes,"minutes or",int(download_time_hours),
          "hours and",int(download_time_minutes_remainder),"minutes.")

    redo = input("Type Yes to redo.")
