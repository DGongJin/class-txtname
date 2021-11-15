import os

fpath = r"C:\Users\gongjin\Desktop\bq"  # 读取文件夹路径


def filechanger(path):
    # 读取文件夹中的文件（包括子文件夹、子文件）
    filenames = os.listdir(path)
    for filename in filenames:
        domain = os.path.abspath(path)
        filename = os.path.join(domain, filename)
        if os.path.isdir(filename):
            filechanger(filename)
            continue
        fread = open(filename, 'r')
        fwrite = open("%s.backup" % filename, 'w')
        while True:
            line = fread.readline()
            if len(line) > 0:
                content = line.split()
                # 按照需要修改下面代码
                if content[0] == 'nofall':
                    content[0] = '1'
                '''elif content[0] == '1':
                    content[0] =='fall'
                elif content[0] == '2':
                    content[0] = str(1)
                elif content[0] == '3':
                    content[0] = str(0)
                else:
                    content[0] = content[0]'''
                newcont = content[0] + ' ' + content[1] + ' ' + content[2] + ' ' + content[3] + ' ' + content[4] + '\r'
                fwrite.write(newcont)  # 修改后写入新文件
            else:
                break
        fread.close()
        fwrite.close()
        os.remove(filename)
        os.rename("%s.backup" % filename, filename)


filechanger(fpath)