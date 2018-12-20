import os
import jieba
import wordcloud
import re
from zhon.hanzi import punctuation

def clear_text(file):
    fj=open(file,'r',encoding='utf8')
    read=fj.read()

    sub=re.sub("[{}]+".format(punctuation),' ',read)
    sub2=re.sub(r"[a-zA-Z\d,\.，。?~→\" '\"/+\-*/#☆★\[\]@!%^&*()]+",' ',sub)
    #print(sub2)
    words=jieba.cut(sub2,cut_all=False)
    result=""
    for word in words:
        result=word+' '+result
    #print(result)
    fj.close()

    return result

if __name__ == '__main__':
    path = "short_comment"
    names = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1] == '.txt':
            names.append(file_path)
    for name in names:
        result=clear_text(name)
        picture=re.findall(r'[\d]',name)
        s = ''
        for i in picture:
            s = s + i
        font = 'C:\Windows\Fonts\STZHONGS.TTF'
        w = wordcloud.WordCloud(width=1920, height=1080, font_path=font, margin=2, background_color='white')
        w.generate(result)
        w.to_file('short_comment\\'+s+'.png')
        print("--------"+name+"---------")
        #exit()



