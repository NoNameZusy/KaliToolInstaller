import os
import time

try:
    import colorama
except ImportError:
    subprocess.run(["pip", "install", "colorama"], check=True)
    import colorama

from colorama import Fore, Style

os.system("clear")

logo = """
    
 _   __      _ _ _____           _ _____          _        _ _           
| | / /     | (_)_   _|         | |_   _|        | |      | | |          
| |/ /  __ _| |_  | | ___   ___ | | | | _ __  ___| |_ __ _| | | ___ _ __ 
|    \ / _` | | | | |/ _ \ / _ \| | | || '_ \/ __| __/ _` | | |/ _ \ '__|
| |\  \ (_| | | | | | (_) | (_) | |_| || | | \__ \ || (_| | | |  __/ |   
\_| \_/\__,_|_|_| \_/\___/ \___/|_|\___/_| |_|___/\__\__,_|_|_|\___|_|   
                                                                         
          ------------------{By Zusy}------------------                          
    
    """
print(logo)
time.sleep(2)

try:
    output = os.popen("dpkg-query -W -f='${Package}\n'").read().splitlines()

    for package in output:
        result = os.system(f"dpkg -s {package} > /dev/null 2>&1")
        if result == 0:
            print(f"{package.ljust(30)}[" + Fore.LIGHTGREEN_EX + "OK" + Style.RESET_ALL + "]")
        else:
            print(f"{package.ljust(30)}[" + Fore.RED + "Not found" + Style.RESET_ALL + "]")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

print("\nCheck completed.")
