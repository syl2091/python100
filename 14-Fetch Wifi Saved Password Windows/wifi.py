import subprocess

data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("gbk")
    .split("\r\n")
)

profiles = [i.split(":")[1] for i in data if "所有用户配置文件" in i]
for i in profiles:
    results = (
        subprocess
        .check_output(["netsh", "wlan", "show", "profile", "HUAWEI Mate 30 5G", "key=clear"])
        .decode("gbk")
        .split("\r\n")
    )
    print(results)