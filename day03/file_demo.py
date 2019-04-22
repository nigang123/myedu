if __name__ == '__main__':
    text_io = open('test.text','w+')
    text_io.write('啊啊啊啊啊啊')

    text_io = open('test.text', 'a+')
    text_io.write('哦哦哦哦哦哦')

    text_io = open('test.text', 'r')
    # readlines = text_io.readlines()
    print(readlines[2])