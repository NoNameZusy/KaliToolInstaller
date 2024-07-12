import os
import subprocess
import time

# Check if colorama is installed, if not, install it
try:
    import colorama
except ImportError:
    subprocess.run(["pip", "install", "colorama"], check=True)
    import colorama

from colorama import Fore, Style

os.system('clear')
time.sleep(3)
print(Fore.LIGHTBLUE_EX + "[MESSAGE]" + Fore.WHITE + " Downloading Kali Linux tools...")
time.sleep(5)
print(Fore.LIGHTBLUE_EX + "[MESSAGE]"+ Fore.WHITE + " This may take some time...")
time.sleep(3)

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear')
    
def get_package_manager():
    """Identify the current package manager."""
    try:
        subprocess.check_output(["apt-get", "--version"])
        return "apt"
    except subprocess.CalledProcessError:
        pass

    try:
        subprocess.check_output(["yum", "--version"])
        return "yum"
    except subprocess.CalledProcessError:
        pass

    return None

def install_kali_tools():
    """Install Kali Linux tools."""
    subprocess.run(["apt-get", "update"], check=True)
    subprocess.run(["apt-get", "install", "-y", "kali-linux-large"], check=True)

def get_kali_tools():
    """Get list of Kali Linux tools from kali-linux-large."""
    kali_tools_output = subprocess.check_output(["apt-cache", "depends", "kali-linux-large"], text=True)
    kali_tools = [line.split()[1] for line in kali_tools_output.splitlines() if line.startswith("  Depends:")]
    return kali_tools

def check_and_install_tools():
    """Check and install Kali Linux tools."""
    tools = subprocess.check_output(["dpkg", "--get-selections"], text=True).splitlines()
    installed_tools = {line.split()[0]: "OK" for line in tools}

    kali_tools = get_kali_tools()
    tools_to_install = []

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
    print(Fore.LIGHTBLUE_EX + "[MESSAGE]"+ Fore.WHITE + " Checking installed tools...\n")
    for tool in kali_tools:
        time.sleep(1)
        if tool in installed_tools:
            print(f"{tool.ljust(27)}[" + Fore.LIGHTGREEN_EX + "OK" + Style.RESET_ALL + "]")
        else:
            print(f"{tool.ljust(27)}[" + Fore.RED + "Not found" + Style.RESET_ALL + "]")
            tools_to_install.append(tool)

    if tools_to_install:
        print("\nDownloading missing tools...")
        for tool in tools_to_install:
            time.sleep(1)
            try:
                subprocess.run(["apt-get", "install", "-y", tool], check=True)
                print(f"{tool.ljust(27)}[" + Fore.LIGHTGREEN_EX + "OK" + Style.RESET_ALL + "]")
            except subprocess.CalledProcessError:
                print(f"{tool.ljust(27)}[" + Fore.RED + "Failed to install" + Style.RESET_ALL + "]")
    
    print(Fore.LIGHTBLUE_EX + "[MESSAGE]" + Fore.WHITE + " Finished")
    time.sleep(3)
    print("Exiting...")
    time.sleep(3)
    clear_screen()

def main():
    original_pm = get_package_manager()

    if original_pm is None:
        print(Fore.LIGHTRED + "[ERROR]" + Style.RESET_ALL + " Unsupported package manager.")
        return

    clear_screen()
    
    subprocess.run(["apt-get", "update"], check=True)
    clear_screen()
    
    install_kali_tools()
    clear_screen()
    
    check_and_install_tools()

    if original_pm != "apt":
        subprocess.run(["apt-get", "remove", "-y", "kali-linux-large"], check=True)
        if original_pm == "yum":
            subprocess.run(["yum", "update"], check=True)
            subprocess.run(["yum", "install", "-y", "yum-utils"], check=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
