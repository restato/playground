import argparse
import os
import pysrt
import pandas as pd

from utils import LANGCODES
from googletrans import Translator


def srt_translator(subs, language_code, filename):
    print('processing %s...' % language_code)
    text_list = []
    for sub in subs:
        text_list.append(sub.text)

    translator = Translator()
    translations = translator.translate(text_list, dest=language_code)
    # for translation in translations:
    # print(translation.origin, ' -> ', translation.text)

    for sub, translation in zip(subs, translations):
        sub.text = translation.text
    subs.save('%s' % (filename), encoding='utf-8')


def main(args):

    # print(LANGCODES)
    subs = pysrt.open(args.input)
    translator = Translator()
    for sub in subs[:3]:
        print(sub.text)
        print(translator.translate(sub.text, dest="en").text)
        print(translator.translate(sub.text, dest="ko").text)

    dirpath = ('/').join(args.input.split('/')[:-1])
    print('directory:%s' % dirpath)
    eng_sub_path = os.path.join(dirpath, 'eng.srt')
    srt_translator(subs, language_code='en',
                   filename=eng_sub_path)
    subs = pysrt.open(eng_sub_path)
    for sub in subs[:3]:
        print(sub.text)

    df = pd.read_csv('code.csv')
    df = df[df['code'].isin(args.lang.split(','))]
    print(df['kor_name'].values)

    for row in df.iterrows():
        subs = pysrt.open(eng_sub_path)
        _, code, kor_name = row[1]
        srt_translator(subs, language_code=code, filename=os.path.join(
            dirpath, code + '_' + kor_name + '.srt'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', help='input *.srt file')
    parser.add_argument('--lang', help='translated lang sep:, (ex: en,ja)')
    args = parser.parse_args()
    main(args)
