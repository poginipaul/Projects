#!/usr/bin/python3
# Purpose: To check and monitor servers
# OS: Ubuntu

try:
    import psutil, subprocess, os

except ImportError as i_err:
    print(i_err)

# Check the ip address text file from the current folder.
def ip_addr(ip_addr):
    with open(ip_addr, 'r') as ip_add:
        ip_address = ip_add.readlines() # read each line.

        ip_addr_strip = [ip.strip('\n') for ip in ip_address] # remove newline.
        return ip_addr_strip
    
        
def check_ip_conn():
    '''Send ICMP message to the servers'''
    ip_txt = 'ip_addr.txt'

    ip_address = ip_addr(ip_txt)
    
    # Check the list of the ip address from the text file.
    for ip in ip_address:
            ping = subprocess.Popen(['ping', ip, '-c', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = ping.communicate() # ping.stdout - returns output | ping.stderr - returns error
            str_out = out.decode('utf-8')
            
            if out:
                 print(f"{ip} - Ok")
                 load1, load5, load15 = psutil.getloadavg()

                 cpu_util = (load15/os.cpu_count()) * 100
                
                 mem_util = psutil.virtual_memory()[3]

                 utils = [cpu_util, mem_util]

                 print(utils)
    

if __name__ == "__main__":
    check_ip_conn()

