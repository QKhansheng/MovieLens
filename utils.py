#!/usr/bin/python3.8

import paramiko
import subprocess
import logging
import os
import sys
import socket
import hashlib
import fileinput
import json
from openpyxl import load_workbook
from openpyxl import workbook
import csv
import time

def utilFilepath(file):
    path = os.path.join(sys.path[0], file)
    return path

def utiltimestamptodatetime(timestamp):
    date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    return date_time

def utilLog():
    logger = logging.getLogger('updateNotice')
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.formatter = formatter
    logger.addHandler(console_handler)
    logFileAbsPath = os.path.join(sys.path[0], "access.log")
    file_handler = logging.FileHandler(logFileAbsPath)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def utilgetymlFile(dir):
    filelist = []
    for home, dirs, files in os.walk(dir):
        # for dir in dirs:
        #     print(dir)
        for file in files:
            if file.endswith(('yml', 'yaml')):
                fullname = os.path.join(home, file)
                filelist.append(fullname)
    return filelist

def utilgetIPhostname():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

def utilHashmd5(filepath):
    if not os.path.isfile(filepath):
        return
    myHash = hashlib.md5()
    f = open(filepath, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myHash.update(b)
    f.close()
    return myHash.hexdigest()

def utilSubprocess(ip):
    p = subprocess.Popen(['ping', '-c', '3'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout, strerr = p.communicate(input=ip)
    if p.returncode == 0:
        print("pong!")
    else:
        print("pang!")
    # while True:
    #     testSubprocess(input("test ping host ip:"))

    #Popen???????????????????????????????????????????????????????????????
    #call??????Popen,???????????????0??????????????????1
    #check_call??????call,???????????????0??????????????????????????????traceback
    #check_output??????run???run??????Popen,?????????????????????????????????????????????traceback
    print(subprocess.Popen(["cat", "hosts"], cwd="/etc"))
    hostname = subprocess.check_output("hostname")
    print(hostname)
    print(subprocess.check_output("netstat -ntlp| grep ssh", shell=True))
    retcode = subprocess.call("ping -c 1 www.baidu.com", shell=True)
    print(retcode)
    print(subprocess.check_call(["ping", "www.baidu.com", "-c", "3"]))

def utilParamikoShell(hostIP, port, username, password):
    #????????????shell??????
    shell = paramiko.SSHClient()
    shell.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    shell.connect(hostname=hostIP, port=port, username=username, password=password,
                    look_for_keys=False, allow_agent=False)
    return shell

def utilParamikoSftp(hostIP, port, username, password):
    # ????????????sftp??????
    trans = paramiko.Transport((hostIP, port))
    trans.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(trans)
    return sftp, trans

if __name__ == '__main__':
    print("????????????")
    # shell = utilParamikoShell("192.168.110.128", 22, "root", "111111")
    # stdin, stdout, stderr = shell.exec_command("hostname")
    # print(stdout.read().decode('utf-8'))
    # shell.close()

    # sftp, trans = utilParamikoSftp("192.168.110.128", 22, "root", "111111")
    # path = os.path.join(sys.path[0], 'utils.py')
    # sftp.put(path, '/usr/local/utils.py')


