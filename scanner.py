import socket

common_ports = {
    21: "FTP (File Transfer)",
    22: "SSH (Secure Con)",
    23: "Telnet (Unturested Con)",
    25: "SMTP (E-posta Service)",
    53: "DNS (DNS resolve)",
    80: "HTTP (Web Trafice)",
    443: "HTTPS (Secure Web)",
    445: "SMB (Share File)",
    3306: "MySQL (Database)",
    8080: "HTTP-Proxy / Test"
}

def port_scanner(target_ip, ports):
    print(f"\nTarget: {target_ip} is scanning...\n" + "-"*40)
    
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) 
            
            result = s.connect_ex((target_ip, port))
            
            service = common_ports.get(port, "Unkown Service")
            
            if result == 0:
                print(f"[+] Port {port} ({service}): OPEN")
            else:
                print(f"[-] Port {port}: CLOSED")
                
                
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] User stopped the scan.")
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")

    print("-"*40 + "\nScan completed.")

target = input("Enter target IP (Ex: 127.0.0.1): ")
target_ports = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 8080]

port_scanner(target, target_ports)