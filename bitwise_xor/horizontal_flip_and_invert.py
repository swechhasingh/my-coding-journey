def flip_and_invert_image(img):
    row = len(img)
    col = len(img[0])
    for i in range(row):
        l, r = 0, col-1
        while l <= r:
            img[i][l], img[i][r] = img[i][r]^1, img[i][l]^1
            l += 1
            r -= 1

    return img
    
def main():
    print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()