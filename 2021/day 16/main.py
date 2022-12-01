# read input
from os import read


with open('input.txt') as f:
    transmission = f.readline().rstrip()
    num_of_bits = len(transmission)*4
    b = str(bin(int(transmission, 16))[2:]).zfill(num_of_bits)

#----------part 1
# def parse(packet: str):
#     version = int(packet[:3], base=2)
#     typeid = int(packet[3:6], base=2)
#     if typeid == 4:  # literal packet
#         data = packet[6:]
#         idx = 0
#         groups = []
#         while True:
#             groups.append(data[idx+1:idx+5])
#             if data[idx] == '0':
#                 idx += 5
#                 break
#             idx += 5
#         val = int(''.join(groups), base=2)
#         return (version, idx+6)
    
#     version_sum = version
#     data = packet[7:]

#     if packet[6] == '0':  # length type ID
#         read_len = int(data[0:15], base=2)
#         read_data = data[15:15+read_len]
#         read_idx = 0
#         while read_idx < read_len:
#             return_val, reach_idx = parse(read_data[read_idx:])
#             version_sum += return_val
#             read_idx += reach_idx
#         return (version_sum, read_idx+7+15)
#     else:
#         packet_count = int(data[0:11], base=2)
#         read_data = data[11:]
#         read_idx = 0
#         for i in range(packet_count):
#             return_val, reach_idx = parse(read_data[read_idx:])
#             version_sum += return_val
#             read_idx += reach_idx
#         return (version_sum, read_idx+7+11)

# print(parse(b)[0])
#----------part 1

#----------part 2
def parse(packet: str):
    version = int(packet[:3], base=2)
    typeid = int(packet[3:6], base=2)
    if typeid == 4:  # literal packet
        data = packet[6:]
        idx = 0
        groups = []
        while True:
            groups.append(data[idx+1:idx+5])
            if data[idx] == '0':
                idx += 5
                break
            idx += 5
        val = int(''.join(groups), base=2)
        return (val, idx+6)
    
    data = packet[7:]
    vals = []

    if packet[6] == '0':  # length type ID
        read_offset = 22
        read_len = int(data[0:15], base=2)
        read_data = data[15:15+read_len]
        read_idx = 0
        while read_idx < read_len:
            return_val, reach_idx = parse(read_data[read_idx:])
            vals.append(return_val)
            read_idx += reach_idx
    else:
        read_offset = 18
        packet_count = int(data[0:11], base=2)
        read_data = data[11:]
        read_idx = 0
        for i in range(packet_count):
            return_val, reach_idx = parse(read_data[read_idx:])
            vals.append(return_val)
            read_idx += reach_idx
    
    if typeid == 0:
        ans = sum(vals)
    elif typeid == 1:
        ans = 1
        for e in vals:
            ans *= e
    elif typeid == 2:
        ans = min(vals)
    elif typeid == 3:
        ans = max(vals)
    elif typeid == 5:
        ans = 1 if vals[0] > vals[1] else 0
    elif typeid == 6:
        ans = 1 if vals[0] < vals[1] else 0
    elif typeid == 7:
        ans = 1 if vals[0] == vals[1] else 0
    return (ans, read_idx+read_offset)

print(parse(b)[0])
#----------part 2