# read input
with open('input.txt') as f:
    lines = [x.rstrip().replace('.', '0').replace('#', '1') for x in f.readlines()]
    algo = lines[0]
    empty, full = algo[0], algo[-1]
    padding = 2
    iw, ih = len(lines[2])+padding*2, len(lines[2:])+padding*2
    image = '0'*iw*padding
    for line in lines[2:]:
        image += padding*'0' + line + padding*'0'
    image += '0'*iw*padding


#----------part 1&2
def algo_idx(img: str, i: int):
    num = img[i-iw-1:i-iw+2] + img[i-1:i+2] + img[i+iw-1:i+iw+2]
    return int(num, base=2)

steps = 50
for step in range(steps):
    border = empty if image[0] == '0' else full
    out_img = border * iw
    for y in range(1, ih-1):
        out_img += border
        for x in range(y*iw+1, (y+1)*iw-1):
            new_algo_idx = algo_idx(image, x)
            out_img += algo[new_algo_idx]
        out_img += border
    out_img += border * iw

    image = border * (iw+2)
    for y in range(ih):
        new_line = border + out_img[y*iw : (y+1)*iw] + border
        image += new_line
    image += border * (iw+2)
    iw += 2
    ih += 2

print(image.count('1'))
#----------part 1&2