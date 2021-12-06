import socket


def get_hostname_ip():
    hostname = input("输入网址:")
    try:
        print(f'主机名:{hostname}')
        print(f'IP:{socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')

get_hostname_ip()