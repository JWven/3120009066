import jieba
import gensim
import re

#��ȡָ��·�����ļ�����
def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        str = str + line
        line = f.readline()
    f.close()
    return str

#����ȡ�����ļ������Ƚ���jieba�ִʣ�Ȼ���ٰѱ����š�ת����ŵ�������Ź��˵�
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

#�������֮������ݣ�ͨ������gensim.similarities.Similarity�����������ƶ�
def calc_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

if __name__ == '__main__':
    path1 = "C:\\Users\\86178\\Desktop\\test\\orig.txt"  #����ԭ�ĵ��ļ��ľ���·������ҵҪ��
    path2 = "C:\\Users\\86178\\Desktop\\test\\orig_0.8_add.txt"  #��Ϯ�����ĵ��ļ��ľ���·��
    save_path = "C:\\Users\\86178\\Desktop\\test\\output.txt"   #����������·��
    str1 = get_file_contents(path1)
    str2 = get_file_contents(path2)

    text1 = filter(str1)
    text2 = filter(str2)
    similarity = calc_similarity(text1, text2)
    print("�������ƶȣ� %.4f"%similarity)
    #�����ƶȽ��д��ָ���ļ�
    f = open(save_path, 'w', encoding="utf-8")
    f.write("�������ƶȣ� %.4f"%similarity)
    f.close()

