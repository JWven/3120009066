import os
import jieba
import gensim
import re

#获取指定路径的文件内容
def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        str = str + line
        line = f.readline()
    f.close()
    return str

#将读取到的文件内容先进行jieba分词，然后再把标点符号、转义符号等特殊符号过滤掉
# def filter(str):
#     str = jieba.lcut(str)
#     result = []
#     for tags in str:
#         if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
#             result.append(tags)
#         else:
#             pass
#     return result
def filter(string):
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = pattern.sub("", string)
    result = jieba.lcut(string)
    return result

#传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

if __name__ == '__main__':
    # path1 = "C:\\Users\\86178\\Desktop\\test\\orig.txt"  #论文原文的文件的绝对路径（作业要求）
    # path2 = "C:\\Users\\86178\\Desktop\\test\\orig_0.8_add.txt"  #抄袭版论文的文件的绝对路径
    # save_path = "C:\\Users\\86178\\Desktop\\test\\output.txt"   #输出结果绝对路径
    # str1 = get_file_contents(path1)
    # str2 = get_file_contents(path2)
    path1 = input("输入论文原文的文件的绝对路径：")
    path2 = input("输入抄袭版论文的文件的绝对路径：")
    if not os.path.exists(path1):
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文文件不存在！")
        exit()
    save_path = input("输入结果保存到文件的绝对路径：")
    str1 = get_file_contents(path1)
    str2 = get_file_contents(path2)
    text1 = filter(str1)
    text2 = filter(str2)
    similarity = calc_similarity(text1, text2)
    print("文章相似度： %.4f"%similarity)
    #将相似度结果写入指定文件
    f = open(save_path, 'w', encoding="utf-8")
    f.write("文章相似度： %.4f"%similarity)
    f.close()

# def main_test():
#     path1 = input("输入论文原文的文件的绝对路径：")
#     path2 = input("输入抄袭版论文的文件的绝对路径：")
#     str1 = get_file_contents(path1)
#     str2 = get_file_contents(path2)
#
#     result=round(similarity.item(),2)  #借助similarity.item()转化为<class 'float'>，然后再取小数点后两位
#     return result
#
# if __name__ == '__main__':
#     main_test()