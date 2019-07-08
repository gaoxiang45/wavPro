
#  将文本信息处理为拼音列表
from pypinyin import pinyin,pinyin_dict,lazy_pinyin,Style
import argparse
import os

#  处理文本信息并将其中文字符转化为英文字符形式
def chs_pinyin(text):
    pys = lazy_pinyin(text, style=Style.TONE3)
    results = []
    sentence = []
    for i in range(len(pys)):
        if pys[i] == "，" or pys[i] == "、" or pys[i] == '·':
            pys[i] = ','
        elif pys[i] == '。' or pys[i] == "…":
            pys[i] = '.'
        elif pys[i] == '―' or pys[i] == "――" or pys[i] == '—' or pys[i] == '——':
            pys[i] = ','
        elif pys[i] == "；":
            pys[i] = ';'
        elif pys[i] == "：":
            pys[i] = ':'
        elif pys[i] == "？":
            pys[i] = '?'
        elif pys[i] == "！":
            pys[i] = '!'
        elif pys[i] == "《" or pys[i] == '》' or pys[i] == '（' or pys[i] == '）':
            continue
        elif pys[i] == '“' or pys[i] == '”' or pys[i] == '‘' or pys[i] == '’' or pys[i] == '＂':
            continue
        elif pys[i] == '(' or pys[i] == ')' or pys[i] == '"' or pys[i] == '\'':
            continue
        elif pys[i] == ' ' or pys[i] == '/' or pys[i] == '<' or pys[i] == '>' or pys[i] == '「' or pys[i] == '」':
            continue

        sentence.append(pys[i])
        if pys[i] in ",.;?!:":
            results.append(' '.join(sentence))  # 如果拼音后出现标点符号，则将其append到列表当中
            sentence = []

    if len(sentence) > 0:
        results.append(' '.join(sentence))

    # for i, res in enumerate(results):
    #     print(res)

    return results

#  读取txt文件的文本信息并将其分组转化为列表的形式


def main():
    base_path = "/home/gaoxiang"
    sentences=[]
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="1.txt", help='the name of the required file')  # 输入想要处理的文本名字
    args = parser.parse_args()
    target_path = os.path.join(base_path, args.filename)
    try:
        with open(target_path) as f:
            text = f.readlines()  # 读取文本的所有信息
    except:
        raise RuntimeError('Failed to load file at {}'.format(target_path))
    str = ' '.join(text)
    temp_str = chs_pinyin(str)
    temp = []
    for i, res in enumerate(temp_str):
        if i == len(temp_str)-1:  # 列表末尾
            temp.append(res)
            sentences.append(' '.join(temp))
            temp.clear()
        elif i % 5 != 0 or i == 0:  # 五个一组对列表分组
            temp.append(res)
        else:  # 扩充列表
            sentences.append(' '.join(temp))
            temp.clear()
            temp.append(res)
    print(sentences)


if __name__ == '__main__':
    main()
