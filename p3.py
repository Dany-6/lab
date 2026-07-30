import pyshark

# Load the packet capture file
capture = pyshark.FileCapture("capture.pcapng")

syn_packets = 0
icmp_packets = 0
ports = set()

print("===== Network Threat Detection =====")

for packet in capture:
    try:
        # Check TCP packets
        if 'TCP' in packet:
            if packet.tcp.flags_syn == '1' and packet.tcp.flags_ack == '0':
                syn_packets += 1

            ports.add(packet.tcp.dstport)

        # Check ICMP packets
        if 'ICMP' in packet:
            icmp_packets += 1

    except:
        pass

capture.close()

print("\nAnalysis Report")
print("---------------------------")
print("TCP SYN Packets :", syn_packets)
print("ICMP Packets    :", icmp_packets)
print("Ports Accessed  :", len(ports))

# Threat Detection
if syn_packets > 20:
    print("\nWarning: Possible SYN Flood Attack!")

if len(ports) > 15:
    print("Warning: Possible Port Scanning!")

if icmp_packets > 30:
    print("Warning: Possible ICMP Flood Attack!")

if syn_packets <= 20 and len(ports) <= 15 and icmp_packets <= 30:
    print("\nNo major network threats detected.")


