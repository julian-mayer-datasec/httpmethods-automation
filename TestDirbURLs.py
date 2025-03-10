import re
import subprocess
import pty


def getURLsFromDirbResults(path: str):
    urls = []
    file = open(path, "r")
    for line in file:
        if "401" in line or "403" in line:
            # print(line)
            match = re.search(r'(https?:\/\/.*) \(', line)
            url = match.group(1)
            urls.append(url)
    file.close()
    return urls


### Output is not colorized ###
def startHTTP_Methods_Tester(urls: list[str]):
    for url in urls:
        print(f"--- Test {url} ---\n")
        try:
            output = subprocess.check_output(["python3", "httpmethods.py", "-k", "-au", url], text=True)
            print(output)

        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")


def startHTTP_Methods_Tester_colorized(urls: list[str]):
    for url in urls:
        print(f"--- Test {url} ---\n")
        pty.spawn(["python3", "httpmethods.py", "-k", "-au", url])


if __name__ == "__main__":
    dirbFile = input("Enter path to dirb result file: ")
    urls = getURLsFromDirbResults(dirbFile)
    print(f"Following URLs will be probed: {urls}\n")
    startHTTP_Methods_Tester_colorized(urls)
