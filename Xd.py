import subprocess

def give_storage_permission():
    # Request storage permission
    subprocess.run(["termux-setup-storage"])

    # Check if storage permission is granted
    result = subprocess.run(["termux-setup-storage", "-n"], capture_output=True, text=True)
    if "Permission granted" in result.stdout:
        print("Storage permission granted.")
    else:
        print("Storage permission not granted.")

# Call the function to give storage permission
give_storage_permission()
