### Usage

- Create srt(`ex: directory_name_SRT_Korean.srt`) file and tnd(`ex: tnd`) file.
- Put srt and tnd files in the `./data/directory`
- Use `directory` name as variable

```
./run.sh {directory} {language_codes}
ex) ./run.sh KingCrab ja,en,ko
```

```
#/bin/bash

# Python VirtualEnv
. ~/Desktop/Project/venv/bin/activate

echo $1
echo $2

python srt_translator.py --input ./data/$1/$1_SRT_Korean.srt --lang $2
python tnd_translator.py --input ./data/$1/tnd --lang \$2

rm eng.srt
```

### Note

- Directory name is used as SRT file name
