import argparse
import speedtest
import threading
import sys
import time

def loading_animation():
    chars = "/—\\"  # Characters for the loading animation
    while not loading_complete.is_set():
        for char in chars:
            sys.stdout.write(f"\rTesting Internet Speed {char}")
            sys.stdout.flush()
            time.sleep(0.2)  # Adjust the duration of each character's display

def check_internet_speed():
    global loading_complete
    loading_complete = threading.Event()

    print("Checking internet speed...")
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert from bits to Megabits
    upload_speed = st.upload() / 1_000_000  # Convert from bits to Megabits

    loading_complete.set()  # Signal the loading animation thread to complete
    loading_thread.join()  # Wait for the loading animation thread to finish

    sys.stdout.write('\r' + ' ' * 30 + '\r')  # Clear the loading animation
    print(f"\n{'-'*30}\n")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"\n{'-'*30}\n")

def main():
    parser = argparse.ArgumentParser(description="Check internet speed.")
    parser.add_argument("-c", "--check", action="store_true", help="Check internet speed")

    args = parser.parse_args()

    if args.check:
        confirmation = input("Do you want to check your internet speed? (yes/no): ").lower()
        if confirmation == "yes":
            check_internet_speed()
        else:
            print("Internet speed check aborted.")

if __name__ == "__main__":
    main()

