# main_script.py
import time

def main():
    try:
        while True:
            print("Running the main script...")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Main script terminated. Restarting...")

if __name__ == "__main__":
    main()
