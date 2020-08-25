import argparse
import os
import pysrt
import pandas as pd

from utils import LANGCODES
from googletrans import Translator


def main(args):

    # print(LANGCODES)
    lines = [x[:-1] for x in open(args.input, 'r').readlines()]
    # title, desc = parse_tnd(lines)

    translator = Translator()
    for l in lines[:3]:
        print(l)
        print(translator.translate(l, dest="en").text)
        print(translator.translate(l, dest="ja").text)

    dirpath = ('/').join(args.input.split('/')[:-1])
    print('directory:%s' % dirpath)
    eng_path = os.path.join(dirpath, 'eng.tnd')

    lines.append("자막은 번역기를 통해 생성했습니다.")
    lines.append("매끄럽지 않아도 이해 부탁드려요. 🙏")
    # ko -> en
    translations = translator.translate(lines, language_code='en',
                                        filename=eng_path)
    translations = [x.text for x in translations]

    df = pd.read_csv('code.csv')
    df = df[df['code'].isin(args.lang.split(','))]
    print(df)
    print(df['kor_name'].values)

    # en -> any language
    results = []
    for row in df.iterrows():
        _, code, kor_name = row[1]
        print(code, kor_name)
        translated = translator.translate(translations, src='en', dest=code)
        print([x.text for x in translated])
        results.append(kor_name + '\n')
        results.append('\n'.join([x.text for x in translated]) + '\n\n')

    with open(os.path.join(dirpath, 'tnd.preprocessed'), 'w') as file:
        file.writelines(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', help='tnd file')
    parser.add_argument('--lang', help='translated lang sep:, (ex: en,ja)')
    args = parser.parse_args()
    main(args)
