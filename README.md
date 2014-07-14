TinySegmenter
----------

TinySegmenter -- Super compact Japanese tokenizer was originally created by 
(c) 2008 Taku Kudo <taku@chasen.org> for javascript under the terms of a new BSD licence.
For details, see [here](http://lilyx.net/pages/tinysegmenter_licence.txt)

tinysegmenter for python2.x was written by Masato Hagiwara.
for his information see [here](http://lilyx.net/pages/tinysegmenterp.html)

This tinysegmenter is modified a bit for python3.x and for distribution by Tatsuro Yasukawa.

See info about [tinysegmenter](https://github.com/SamuraiT/tinysegmenter)

Installation
------------

```
pip install tinysegmenter3
```

Usage
----------

```
from tinysegmenter import TinySegmenter
segmenter = TinySegmenter()
statement = '私はpython大好きStanding Engineerです．'
tokenized_statement = segmenter.tokenize(statement)
print(tokenized_statement)
# ['私', 'は', 'python', '大好き', 'Standing', ' Engineer', 'です', '．']
```

