# 写入文档
def write_file(path,text):
    with open(path,'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n')

# 清空文档
def make_empty_file(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()


# 读取文档
def read_file(path):
    n=1
    with open(path, 'r', encoding='utf-8') as f:
        list = []
        for s in f.readlines():
            list.append(s.strip())
    return list


#将单列表内的元素进行分割并去除‘/’

def segmented(lists):
    target=' '
    for list in lists:
        if str(list) != '/':
            target = target + ' ' + list
    return target