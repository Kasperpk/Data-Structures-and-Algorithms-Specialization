def network_package(s,n,packets):

    packet_output = []

    i = 0
    for packet in packets:
        if len(packet_output) <= s and not packet_output:
            packet_output.append(packet)
            i += 1
        elif len(packet_output) <= s and packet[0] >= packet_output[i-1][1]:
            packet_output.append(packet)
            i += 1
        else:
            packet_output.append(-1)
            i += 1

    for pack in packet_output:
        if type(pack) == tuple:
            print(pack[0])
        else:
            print(pack)

if __name__ == "__main__":
    s, n = map(int, input().strip().split())
    packets = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        packets.append((a, a+b))
    network_package(s,n,packets)