TinySegmenter
----------

TinySegmenter -- Super compact Japanese tokenizer was originally created by
(c) 2008 Taku Kudo for javascript under the terms of a new BSD licence.
For details, see [here](http://lilyx.net/pages/tinysegmenter_licence.txt)

tinysegmenter for python2.x was written by Masato Hagiwara.
for his information see [here](http://lilyx.net/pages/tinysegmenterp.html)

This tinysegmenter is modified for python3.x and python2.x for distribution by Tatsuro Yasukawa.
Additionaly, this tinysegmenter is modified for being more faster - thanks to
@chezou, @cocoatomo and @methane.

See info about [tinysegmenter](https://github.com/SamuraiT/tinysegmenter)

Installation
------------

```
pip install tinysegmenter3
```

Usage
----------

```
import tinysegmenter
statement = '私はpython大好きStanding Engineerです．'
tokenized_statement = tinysegmenter.tokenize(statement)
print(tokenized_statement)
# ['私', 'は', 'python', '大好き', 'Standing', ' Engineer', 'です', '．']
```

Test Text
----------

The [test text](http://www.genpaku.org/timemachine/timemachineu8j.txt) (in the `tests` directory) was [The Time Machine](https://en.wikipedia.org/wiki/The_Time_Machine) by H.G. Wells, translated to Japanese by Hiroo Yamagata under the CC BY-SA 2.0 License.
