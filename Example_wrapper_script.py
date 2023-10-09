# Import the subprocess module, which allows us to spawn new processes,
# connect to their input/output/error pipes, and obtain their return codes.
import subprocess

def main():
    # The main function that will be the entry point for our script.

    while True:
        # A continuous loop that will keep our script running indefinitely.
        
        print("Starting api_script.py")
        # Print a message indicating that we are attempting to start the main script.

        # Use the subprocess.call() method to run our main script. 
        # The first argument is a list where the first item is the command (in this case, 'python3') 
        # and the subsequent items are arguments passed to the command.
        # In this case, we're running 'python3 /path/to/your/api_script.py'.
        subprocess.call(["python3", "/path/to/your/api_script.py"])

        # If the main script (api_script.py) terminates for any reason, the subprocess.call() will return,
        # and the next iteration of the loop will attempt to restart the script.

if __name__ == "__main__":
    # This construct ensures that the following code only executes if this script is run directly 
    # (i.e., not imported as a module into another script).

    main()
    # Call the main function to start our script.

