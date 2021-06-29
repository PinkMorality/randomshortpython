def download_time_calc():
    size = int(input("Enter download size in GB: "))

    speed_choice = int(input("""For speed in mBit, press 1:
For speed in mByte, press 2: """))

    if speed_choice == 1:
        speed_b = int(input("Enter download speed in mBit: "))
    elif speed_choice == 2:
        speed_b = int(input("Enter download speed in mByte: "))
    else:
        print("Error")


    def d_time_mbit(gigabyte, speed):
        time_s = (gigabyte*8*1024)/speed
        return time_s, size

    def d_time_mbyte(gigabyte, speed):
        time_s = (gigabyte*1024)/speed
        return time_s, size

    if speed_choice == 1:
        x = d_time_mbit(size, speed_b)
        s_time = int(x[0])
        m_time = s_time // 60
        h_time = m_time // 60
        mr_time = m_time % 60
        print(f"""It will take
{s_time} seconds OR
{m_time} minutes OR
{h_time} hours and {mr_time} minutes
to download {x[1]}GB""")

    elif speed_choice == 2:
        x = d_time_mbyte(size, speed_b)
        s_time = int(x[0])
        m_time = s_time // 60
        h_time = m_time // 60
        mr_time = m_time % 60
        print(f"""It will take
{s_time} seconds OR
{m_time} minutes OR
{h_time} hours and {mr_time} minutes
to download {x[1]}GB""")

    else:
        print("Error")



while True:
    download_time_calc()

    redo = input("Enter 'Y' to redo: ")
    if redo != "Y":
        break