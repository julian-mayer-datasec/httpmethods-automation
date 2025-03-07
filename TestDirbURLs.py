import re
import subprocess
import os
from typing import List

#os.path.dirname(os.path.realpath(__file__))

# Defining main function
def getURLSfromDirbResults(path:str):
    urls = []
    file = open(path, "r")
    for line in file:
        if "401" in line or "403" in line:
            #print(line)
            match = re.search(r'(https?:\/\/.*) \(', line)
            url = match.group(1)
            urls.append(url)
    file.close()
    return urls


def startHTTP_Methods_Tester(urls: list[str]):
    for url in urls:
        print(f"--- Test {url} ---\n")
        try:
            output = subprocess.check_output(["python3", "httpmethods.py", "-k", "-au", url], text=True)
            print(output)

        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")


if __name__=="__main__":
    dirbfile = input("Enter path to dirb result file: ")
    urls = getURLSfromDirbResults(dirbfile)
    print(f"Following URLs will be probed: {urls}\n")
    startHTTP_Methods_Tester(urls)