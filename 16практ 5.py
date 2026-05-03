# IP-адреса
ip1_line = "1.1.1.1 8.8.8.8"
ip2_line = "8.8.8.8 2.2.2.2"
ip3_line = "1.1.1.1 8.8.8.8 3.3.3.3"

ip1 = set(ip1_line.split())
ip2 = set(ip2_line.split())
ip3 = set(ip3_line.split())

suspicious_ips = (ip1 | ip2 | ip3) - (ip1 & ip2 & ip3)

print(' '.join(sorted(suspicious_ips)))