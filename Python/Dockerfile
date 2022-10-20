FROM python:3.10

RUN mkdir -p /src
COPY src /src
WORKDIR /src

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir -r requirements.txt

# CMD python /src/string1.py
# CMD python /src/string2.py
# CMD python /src/list1.py
# CMD python /src/list2.py
# CMD python /src/wordcount/wordcount.py --count /src/wordcount/small.txt
# CMD python /src/wordcount/wordcount.py --topcount /src/wordcount/alice.txt
# CMD python /src/wordcount/mimic.py /src/wordcount/alice.txt
# CMD python /src/babynames/babynames.py /src/babynames/baby2006.html
# CMD python /src/babynames/babynames.py --summaryfile /src/babynames/baby2006.html
# CMD python /src/copyspecial/copyspecial.py copyspecial
# CMD python /src/copyspecial/copyspecial.py --todir /tmp copyspecial
# CMD python /src/copyspecial/copyspecial.py --tozip myzip.zip copyspecial
# CMD python /src/logpuzzle/logpuzzle.py /src/logpuzzle/animal_code.google.com
# CMD python /src/logpuzzle/logpuzzle.py --todir output /src/logpuzzle/animal_code.google.com
# CMD python /src/logpuzzle/logpuzzle.py --todir output /src/logpuzzle/place_code.google.com 
# CMD python /src/random1.py
# CMD python /src/tree.py
# CMD python /src/image1.py
# CMD python /src/wip.py
# CMD python /src/knapsack.py
CMD python /src/coding.py
