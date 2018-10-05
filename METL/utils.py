# -*- coding: utf-8 -*-
"""Utility functions for managing ETL hand writting dataset.

Reference:

- http://etlcdb.db.aist.go.jp/etlcdb/etln/form_m.htm
- http://etlcdb.db.aist.go.jp/etlcdb/etln/form_c.htm
- http://etlcdb.db.aist.go.jp/etlcdb/etln/form_e8g.htm
- http://etlcdb.db.aist.go.jp/etlcdb/etln/form_e9g.htm

/---[form_m.htm 2001-09.04]-------------------------------------------------------------------

                                M-Type Data Format      (ETL1, ETL6, ETL7)


1. File Format (Fixed Record Length without Control Words)

                   <----------> Logical record (2052 bytes) (1byte = 8bits)
     ------------------------------------------------------------------
     |  Sample 1  |  Sample 2  |  Sample 3  |    ....    |  Sample N  |  (No. of records = N)
     ------------------------------------------------------------------


2. Contents of Logical Record (2052 bytes)

 --------------------------------------------------------------------------------------------
|             |Number|        |                                                              |
|     Byte    |  of  |  Type  |            Contents of Logical Record                        |
|   Position  | Bytes|        |                                                              |
|============================================================================================|
|    1 -    2 |    2 | Integer| Data Number (greater than or equal to 1)                     |
|    3 -    4 |    2 | ASCII  | Character Code ( ex. "0 ", "A ", "$ ", " A", "KA" )          |
|    5 -    6 |    2 | Integer| Serial Sheet Number (greater than or equal to 0)             |
|I   7        |    1 | Binary | JIS Code (JIS X 0201)                                        |
|D   8        |    1 | Binary | EBCDIC Code                                                  |
|    9        |    1 | Integer| Evaluation of Individual Character Image (0=clean, 1, 2, 3)  |
|P  10        |    1 | Integer| Evaluation of Character Group (0=clean, 1, 2)                |
|a  11        |    1 | Integer| Male-Female Code ( 1=male, 2=female ) (JIS X 0303)           |
|r  12        |    1 | Integer| Age of Writer                                                |
|t  13 -   16 |    4 | Integer| Serial Data Number (greater than or equal to 1)              |
|   17 -   18 |    2 | Integer| Industry Classification Code (JIS X 0403)                    |
|   19 -   20 |    2 | Integer| Occupation Classification Code (JIS X 0404)                  |
|   21 -   22 |    2 | Integer| Sheet Gatherring Date (19)YYMM                               |
|   23 -   24 |    2 | Integer| Scanning Date (19)YYMM                                       |
|   25        |    1 | Integer| Sample Position Y on Sheet (greater than or equal to 1)      |
|   26        |    1 | Integer| Sample Position X on Sheet (greater than or equal to 1)      |
|   27        |    1 | Integer| Minimum Scanned Level (0 - 255)                              |
|   28        |    1 | Integer| Maximum Scanned Level (0 - 255)                              |
|   29 -   30 |    2 | Integer| (undefined)                                                  |
|   31 -   32 |    2 | Integer| (undefined)                                                  |
|-------------|------|--------|--------------------------------------------------------------|
|   33 - 2048 | 2016 | Packed | 16 Gray Level (4bit/pixel) Image Data                        |
|             |      |        | 64(X-axis size) * 63(Y-axis size) = 4032 pixels              |
|-------------|------|--------|--------------------------------------------------------------|
| 2049 - 2052 |    4 |        | (uncertain)                                                  |
 --------------------------------------------------------------------------------------------

------------------------------------------------------------[form_m.htm]---------------------/


/---[form_c.htm 2001-09.04]-------------------------------------------------------------------


                                C-Type Data Format      (ETL3, ETL4, ETL5)


1. File Format (Fixed Record Length without Control Words)

                   <----------> Logical record (2952 bytes) (1byte = 8bits)
     ------------------------------------------------------------------
     |  Sample 1  |  Sample 2  |  Sample 3  |    ....    |  Sample N  |  (No. of records = N)
     ------------------------------------------------------------------


2. Contents of Logical Record (3936 characters = 2952 bytes) (1character = 6bits)

 --------------------------------------------------------------------------------------------
|             |No. of|        |                                                              |
|   Character |Char- |  Type  |            Contents of Logical Record                        |
|   Position  |acters|        |                                                              |
|============================================================================================|
|    1 -    6 |    6 | Integer| Serial Data Number                                           |
|    7 -   12 |    6 | Integer| Serial Sheet Number                                          |
|   13 -   18 |    6 | Binary | JIS Code (Effective bits = Left 8 bits) (JIS X 0201)         |
|I  19 -   24 |    6 | Binary | EBCDIC Code (Effective bits = Left 8 bits)                   |
|D  25 -   28 |    4 | T56Code| 4 Character Code ( ex. "N  0", "A  A", "S  +", "K KA" )      |
|   29 -   30 |    2 | T56Code| Spaces                                                       |
|P  31 -   36 |    6 | Integer| Evaluation of Individual Character Image (0=clean, 1, 2, 3)  |
|a  37 -   42 |    6 | Integer| Evaluation of Character Group (0=clean, 1, 2)                |
|r  43 -   48 |    6 | Integer| Sample Position Y on Sheet                                   |
|t  49 -   54 |    6 | Integer| Sample Position X on Sheet                                   |
|   55 -   60 |    6 | Integer| Male-Female Code ( 1=male, 2=female ) (JIS X 0303)           |
|   61 -   66 |    6 | Integer| Age of Writer                                                |
|   67 -   72 |    6 | Integer| Industry Classification Code (JIS X 0403)                    |
|   73 -   78 |    6 | Integer| Occupation Classification Code (JIS X 0404)                  |
|   79 -   84 |    6 | Integer| Sheet Gatherring Date                                        |
|   85 -   90 |    6 | Integer| Scanning Date                                                |
|   91 -   96 |    6 | Integer| Number of X-Axis Sampling Points                             |
|   97 -  102 |    6 | Integer| Number of Y-Axis Sampling Points                             |
|  103 -  108 |    6 | Integer| Number of Levels of Pixel                                    |
|  109 -  114 |    6 | Integer| Magnification of Scanning Lenz                               |
|  115 -  120 |    6 | Integer| Serial Data Number (old)                                     |
|  121 -  288 |  168 |        | (undefined)                                                  |
|-------------|------|--------|--------------------------------------------------------------|
|  289 - 3936 | 3648 | Packed | 16 Gray Level (4bit/pixel) Image Data                        |
|             |      |        | 72(X-axis size) * 76(Y-axis size) = 5472 pixels              |
 --------------------------------------------------------------------------------------------

------------------------------------------------------------[form_c.htm]---------------------/

/---[form_e8g.htm 2001-09.04]-----------------------------------------------------------------


                                G-Type Data Format      (ETL8)


1. File Format (Fixed Record Length without Control Words)

                   <----------> Logical record (8199 bytes) (1byte = 8bits)
     ------------------------------------------------------------------
     |  Sample 1  |  Sample 2  |  Sample 3  |    ....    |  Sample N  |  (No. of records = N)
     ------------------------------------------------------------------


2. Contents of Logical Record (8199 bytes)

 --------------------------------------------------------------------------------------------
|             |Number|        |                                                              |
|     Byte    |  of  |  Type  |            Contents of Logical Record                        |
|   Position  | Bytes|        |                                                              |
|============================================================================================|
|    1 -    2 |    2 | Integer| Serial Sheet Number (greater than or equal to 1)             |
|    3 -    4 |    2 | Binary | JIS Kanji Code (JIS X 0208)                                  |
|    5 -   12 |    8 | ASCII  | JIS Typical Reading ( ex. "AI.MEDER" )                       |
|I  13 -   16 |    4 | Integer| Serial Data Number (greater than or equal to 1)              |
|D  17        |    1 | Integer| Evaluation of Individual Character Image (>= 0)              |
|   18        |    1 | Integer| Evaluation of Character Group (greater than or equal to 0)   |
|P  19        |    1 | Integer| Male-Female Code ( 1=male, 2=female ) (JIS X 0303)           |
|a  20        |    1 | Integer| Age of Writer                                                |
|r  21 -   22 |    2 | Integer| Industry Classification Code (JIS X 0403)                    |
|t  23 -   24 |    2 | Integer| Occupation Classification Code (JIS X 0404)                  |
|   25 -   26 |    2 | Integer| Sheet Gatherring Date (19)YYMM                               |
|   27 -   28 |    2 | Integer| Scanning Date (19)YYMM                                       |
|   29        |    1 | Integer| Sample Position X on Sheet (greater than or equal to 0)      |
|   30        |    1 | Integer| Sample Position Y on Sheet (greater than or equal to 0)      |
|   31 -   60 |   30 |        | (undefined)                                                  |
|-------------|------|--------|--------------------------------------------------------------|
|   61 - 8188 | 8128 | Packed | 16 Gray Level (4bit/pixel) Image Data                        |
|             |      |        | 128(X-axis size) * 127(Y-axis size) = 16256 pixels           |
|-------------|------|--------|--------------------------------------------------------------|
| 8189 - 8199 |   11 |        | (uncertain)                                                  |
 --------------------------------------------------------------------------------------------


app. Contents of Files

--------------------------------------------------------------------------------------------
|  File    |  Number | No. of |  Number  |           | Number |                              |
|    Name  |    of   | Categ- |    of    |  Data Set |   of   |                              |
|          | Records |  ories | Data Sets|   Number  | Sheets |                              |
|============================================================================================|
| ETL8G-01 |   4780  |   956  |     5    |   1 -   5 |   50   |                              |
| ETL8G-02 |   4780  |   956  |     5    |   6 -  10 |   50   |                              |
|    :     |     :   |    :   |     :    |     :     |    :   |                              |
| ETL8G-32 |   4780  |   956  |     5    | 156 - 160 |   50   |                              |
| ETL8G-33 |    956  |   956  |     1    | uncertain |   10   |                              |
 --------------------------------------------------------------------------------------------

------------------------------------------------------------[form_e8g.htm]-------------------/

/---[form_e9g.htm 2001-09.04]-----------------------------------------------------------------


                                G-type Data Format      (ETL9)


1. File Format (Fixed Record Length without Control Words)

                   <----------> Logical record (8199 bytes) (1byte = 8bits)
     ------------------------------------------------------------------
     |  Sample 1  |  Sample 2  |  Sample 3  |    ....    |  Sample N  |  (No. of records = N)
     ------------------------------------------------------------------


2. Contents of Logical Record (8199 bytes)

 --------------------------------------------------------------------------------------------
|             |Number|        |                                                              |
|     Byte    |  of  |  Type  |            Contents of Logical Record                        |
|   Position  | Bytes|        |                                                              |
|============================================================================================|
|    1 -    2 |    2 | Integer| Serial Sheet Number (greater than or equal to 1)            n|
|    3 -    4 |    2 | Binary | JIS Kanji Code (JIS X 0208)                                  |
|    5 -   12 |    8 | ASCII  | JIS Typical Reading ( ex. "AI.MEDER" )                       |
|I  13 -   16 |    4 | Integer| Serial Data Number (greater than or equal to 1)             n|
|D  17        |    1 | Integer| Evaluation of Individual Character Image (>= 0)             n|
|   18        |    1 | Integer| Evaluation of Character Group (greater than or equal to 0)  n|
|P  19        |    1 | Integer| Male-Female Code ( 1=male, 2=female ) (JIS X 0303)          n|
|a  20        |    1 | Integer| Age of Writer                                               n|
|r  21 -   22 |    2 | Integer| Industry Classification Code (JIS X 0403)                   n|
|t  23 -   24 |    2 | Integer| Occupation Classification Code (JIS X 0404)                 n|
|   25 -   26 |    2 | Integer| Sheet Gatherring Date (19)YYMM                              n|
|   27 -   28 |    2 | Integer| Scanning Date (19)YYMM                                       |
|   29        |    1 | Integer| Sample Position X on Sheet (greater than or equal to 0)      |
|   30        |    1 | Integer| Sample Position Y on Sheet (greater than or equal to 0)      |
|   31 -   64 |   34 |        | (undefined)                                                 n|
|-------------|------|--------|--------------------------------------------------------------|
|   65 - 8192 | 8128 | Packed | 16 Gray Level (4bit/pixel) Image Data                        |
|             |      |        | 128(X-axis size) * 127(Y-axis size) = 16256 pixels           |
|-------------|------|--------|--------------------------------------------------------------|
| 8193 - 8199 |    7 |        | (uncertain)                                                 n|
 --------------------------------------------------------------------------------------------


app. Contents of Files

 --------------------------------------------------------------------------------------------
|  File    |  Number | No. of |  Number  |           | Number |                              |
|    Name  |    of   | Categ- |    of    |  Data Set |   of   |                              |
|          | Records |  ories | Data Sets|   Number  | Sheets |                              |
|============================================================================================|
| ETL9G-01 |  12144  |  3036  |     4    |   1 -   4 |   80   |                              |
| ETL9G-02 |  12144  |  3036  |     4    |   5 -   8 |   80   |                              |
|    :     |    :    |    :   |     :    |     :     |    :   |                              |
| ETL9G-50 |  12144  |  3036  |     4    | 197 - 200 |   80   |                              |
 --------------------------------------------------------------------------------------------

------------------------------------------------------------[form_e9g.htm]-------------------/


# Memorandom

url='http://etlcdb.db.aist.go.jp/?page_id=56'

When you type the blow commands,

```bash
> for file in ETL1.zip ETL3.zip ETL4.zip ETL5.zip ETL6.zip ETL7.zip ETL8G.zip ETL9G.zip; do  wget "http://etlcdb.db.aist.go.jp/etlcdb/data/${file}"
```

You would be able to get the files blow.

```
-rw-r--r--@ 1 asakawa  staff    9023413 Oct  1 17:09 ETL3.zip
-rw-r--r--@ 1 asakawa  staff  165893957 Oct  1 09:26 ETL6.zip
-rw-r--r--@ 1 asakawa  staff   37369093 Oct  1 09:25 ETL7.zip
-rw-r--r--@ 1 asakawa  staff    8423946 Oct  1 09:22 ETL5.zip
-rw-r--r--@ 1 asakawa  staff    4949352 Oct  1 09:19 ETL4.zip
-rw-r--r--@ 1 asakawa  staff  105028771 Sep 28 19:02 ETL1.zip
-rw-r--r--@ 1 asakawa  staff  587770429 Nov 15  2017 ETL9G.zip
-rw-r--r--@ 1 asakawa  staff  163692171 Nov 15  2017 ETL9B.zip
-rw-r--r--@ 1 asakawa  staff  141374316 Nov 15  2017 ETL8G.zip
-rw-r--r--@ 1 asakawa  staff   27760622 Nov 15  2017 ETL8B.zip
```



    フォーマット文字一覧
    文字	C言語型	標準サイズ
    --------------------------
    x	パティングバイト	1
    c	char	1
    b	signed char	1
    B	unsigned char, BYTE	1
    ?	_Bool	1
    h	short	2
    H	unsinged short, WORD	2
    i	int	4
    I	unsigned int, DWORD	4
    l	long, LONG	4
    L	unsigned long, ULONG	4
    q	long long, LONGLONG	8
    Q	unsigned long long, ULONGLONG	8
    n	ssize_t(Python3.3以降)	Nativeのみ
    N	size_t(Python3.3以降)	Nativeのみ
    f	float	4
    d	double	8
    s	char[]	-
    p	char[]	-
    P	void *	-
    --------------------------

"""

import numpy as np
import bitstring  # must be done in advance, `pip install bitstring`

import codecs
import h5py
import os
import pickle
from PIL import Image
import struct
import sys
from urllib import request

#Belows are required to manage zip files in memory
#See https://stackoverflow.com/questions/10908877/extracting-a-zipfile-to-memory
#import zipfile
if sys.version_info[0] == 2:
    import StringIO as io
else:
    import io


def get_data(filename, forceDownload=False):
    """Downloading word2vec models from Tokyo Women's Christian univ.

    Example:
        dataset.get_data('ETL8G_images.hdf5')
    """

    url = 'http://www.cis.twcu.ac.jp/~asakawa/ETL_handwriting'
    size_dict = {
        'ETL1_labels.pk': 1694682,
        'ETL3_labels.pk':  114269,
        'ETL4_labels.pk':   78711,
        'ETL5_labels.pk':   78815,
        'ETL6_labels.pk': 1894464,
        'ETL7_labels.pk':  402509,
        'ETL8G_labels.pk':2296214,
        'ETL9G_labels.pk':9094257,

        'ETL1_images.hdf5':  195959939,
        'ETL3_images.hdf5':   34910270,
        'ETL4_images.hdf5':   20536116,
        'ETL5_images.hdf5':   20669680,
        'ETL6_images.hdf5':  311835441,
        'ETL7_images.hdf5':   66066244,
        'ETL8G_images.hdf5': 183864914,
        'ETL9G_images.hdf5': 721916431}

    assert 'Invalid filename: {0}'.format(filename), filename in size_dict
    expected_size = size_dict[filename]
    path = os.getcwd()
    dest_filename = os.path.join(path, filename)

    if os.path.exists(dest_filename):
        statinfo = os.stat(dest_filename)
        if statinfo.st_size != expected_size:
            forceDownload = True
            print("File {0} not expected size, forcing download".format(filename))
        else:
            print("File '{0}' allready downloaded.".format(filename))

    if forceDownload == True or not os.path.exists(dest_filename):
        print('Attempting to download: {}'.format(filename)) 
        request.urlretrieve(url + '/' + filename, dest_filename)
        print("Downloaded '{}' successfully".format(filename))


#----------------------------------------------------------------------------------

def download_all():
    filenames = ('ETL1_images.hdf5', 'ETL1_labels.pk',
                 'ETL3_images.hdf5', 'ETL3_labels.pk',
                 'ETL4_images.hdf5', 'ETL4_labels.pk',
                 'ETL5_images.hdf5', 'ETL5_labels.pk',
                 'ETL6_images.hdf5', 'ETL6_labels.pk',
                 'ETL7_images.hdf5', 'ETL7_labels.pk',
                 'ETL8G_images.hdf5', 'ETL8G_labels.pk',
                 'ETL9G_images.hdf5', 'ETL9G_labels.pk')


    for filename in filenames:
        get_data(filename, forceDownload=False)
        #print(filename)

    for filename in filenames:
        if filename.split('.')[-1] == 'hdf5':
            a = load_images_hdf5(filename)
        else:
            a = load_labels_pickle(filename)
        print('file:{0:s}, len:{1:d}'.format(filename,len(a)), end=' ')
        print('shape:{}'.format(a.shape)) if filename.split('.')[-1] == 'hdf5' else print()


def save_images_hdf5(data, filename=None):
    """Save a numpy array into hdf5 format."""
    
    assert isinstance(data, np.ndarray), 'data must be a numpy array'
    assert filename, 'filename must be declared'
    f = h5py.File(filename,'w')
    f.create_dataset('Images',data=data,compression='gzip')
    f.close()


def load_images_hdf5(filename):
    """Load a numpy array of the hdf5 format into numpy array."""
    
    f = h5py.File(filename, 'r')
    ret = np.copy(f['Images'])
    f.close()
    return ret


def save_labels_pickle(data, filename=None):
    """Save any file into pickle file."""
    assert filename, 'filename must be declared'
    with codecs.open(filename,'wb') as f:
        pickle.dump(data,f)


def load_labels_pickle(filename):
    """Read a pickled file."""
        
    with codecs.open(filename, 'rb') as f:
        labels = pickle.load(f)
    return labels

#------------------------------------------------------------------------------

def fetch_ETL_Ctype(f,
                    pos=0,
                    dtype=np.int32,
                    white_background=True, 
                    verbose=False):
    """read an image form ETL C-type data such as ETL3, ETL4, and ETL5.
        
    Arguments:
        filename: Data file name to be extracted: string
        pos: position : integer
        dtype: for numpy array
        white_background: optional switch to be reversed the polarity: boolean
        verbose: optional switch to display redundant information
        
    Returns:
        data: numpy array
        img: image raw data: PIL.Image 
        jis_code: for label : string
        serial_number: the original number for ETL: integer
    """
    rec_size = 2952
    f = bitstring.ConstBitStream(filename=f)
    f.bytepos = pos * rec_size
    r = f.readlist('2*uint:36,uint:8,pad:28,uint:8,pad:28,4*uint:6,pad:12,15*uint:36,pad:1008,bytes:21888')
    serial_number = r[0]
    jis_code = r[2]
    if verbose:
        print('Serial Data Number:', r[0])
        print('Serial Sheet Number:', r[1])
        print('JIS Code:', r[2])
        print('EBCDIC Code:', r[3])
        print('4 Character Code:', ''.join([t56s[c] for c in r[4:8]]))
        print('Evaluation of Individual Character Image:', r[8])
        print('Evaluation of Character Group:', r[9])
        print('Sample Position Y on Sheet:', r[10])
        print('Sample Position X on Sheet:', r[11])
        print('Male-Female Code:', r[12])
        print('Age of Writer:', r[13])
        print('Industry Classification Code:', r[14])
        print('Occupation Classifiaction Code:', r[15])
        print('Sheet Gatherring Date:', r[16])
        print('Scanning Date:', r[17])
        print('Number of X-Axis Sampling Points:', r[18])
        print('Number of Y-Axis Sampling Points:', r[19])
        print('Number of Levels of Pixel:', r[20])
        print('Magnification of Scanning Lens:', r[21])
        print('Serial Data Number (old):', r[22])
        
    iF = Image.frombytes('F', (r[18], r[19]), r[-1], 'bit', 4)
    iL = iF.convert('L')
    if white_background:
        img = Image.eval(iL, lambda x: 255-x*16)  # Background: white, and foreground: black
    else:
        img = Image.eval(iL, lambda x: x*16)  # background: black, and foreground: white

    return np.asarray(img,dtype=dtype), img, jis_code, serial_number

#------------------------------------------------------------------------------

def make_data_ETL_Ctype(files_dict, verbose=True):
    """Read ETL C-type data and return numpy matrix such ask ETL3, ETL4, and ETL5.
    
    Also, this function resize images to (64, 64)
        
    Augments:
        files_dict: information of data files and number of records

    Returns:
        ret: numpy matrix of images (total_images,64,64)
        labels_list: list of labels
        labels_freq: frequncy tables of labels
    """
    grand_max, grand_min = 0, 255
    counter = 0
    white_image = Image.new('L', (76, 76))
    white_background = [255 for x in range(76 * 76)]  # for white background
    white_image.putdata(white_background)    
    #initialize return labels
    labels_freq = dict()
    labels_list = list()
    
    #initialize image data matrix
    total_images = np.sum(files_dict[i] for i in files_dict)
    ret = np.ndarray((total_images, 64, 64), dtype=np.int32)
    if verbose:
        print(ret.shape, ret.size)
    
    for filename in files_dict:
        if verbose:
            print('filename: {}'.format(filename))

        Min, Max = 255, 0
        local_count = 0

        for num in range(files_dict[filename]):
            data, img, jis_code, serial_number = fetch_ETL_Ctype(filename, \
                                                                 num, \
                                                                 white_background=True)
            min, max = np.min(data), np.max(data)
            white_image.paste(img, (0, 0))
            ret_image = white_image.resize((64,64), Image.ANTIALIAS)
            ret[counter] = ret_image
            label = str(jis_code)
            labels_list.append(label)
            if counter % (total_images>>3) == 0 and verbose:
                plt.imshow(ret[counter],cmap='gray')
                plt.show()
                print('jis code={}'.format(jis_code))
            counter += 1
            local_count += 1
            if label in labels_freq:
                labels_freq[label] += 1
            else:
                labels_freq[label] = 1

            if min < Min:
                Min = min
            if max > Max:
                Max = max
            if verbose:
                print('filename={:s}, '.format(filename), end='')
                print('record numbers={:d}, '.format(files_dict[filename]), end='')
                print('local_count={:d}'.format(local_count))

            if grand_max < Max:
                grand_max = Max
            if grand_min > Min:
                grand_min = Min
    if verbose:
        print('grand_min={}, grand_max={}'.format(grand_min, grand_max))
        print('counter={}'.format(counter))
    return ret, labels_list, labels_freq, counter == total_images

#------------------------------------------------------------------------------

def fetch_ETL_Mtype(num,
                    filename='ETL7/ETL7LC_1', 
                    rec_size=2052,    #ETL_Mtype_rec_size,
                    img_sizes=(64, 63),    #ETL_Mtye_image_sizes,
                    WhiteBackGround=True,
                    dtype=np.int32):
    """Get an image of ETL M-type. such as ETL1, ETL6, and ETL7"""
        
    #ETL_Mtype_rec_size = 2052
    ETL_Mtype_rec_size = rec_size
    ETL_Mtype_img_sizes = (64, 63)  #size = (width, hight), for ETL1, 6, and 7
    ETL_Mtype_record_format = '>H2sH6BI4H4B4x2016s4x'  # for ETL1, ETL6, and ETL7

    with open(filename, 'rb') as f:
        f.seek(num * rec_size)
        s = f.read(rec_size)
    r = struct.unpack(ETL_Mtype_record_format, s)
    jis_code = '{:x}'.format(r[3])
    iF = Image.frombytes('F', img_sizes, r[18], 'bit', 4)
    # 'bit', 4 above means that the data would be composed 16 Gray Level (4bit/pixel)
    iL = iF.convert('L')
    if WhiteBackGround:
        # Background: white, and foreground: black
        img = Image.eval(iL, lambda x: 255-x*16)
    else:
        # background: black, and foreground: white
        img = Image.eval(iL, lambda x: x*16)
    return np.asarray(img, dtype=dtype), img, jis_code



def make_data_ETL_Mtype(files_dict, verbose=True):
    """Read ETL Mtype data and return numpy matrix and so on.

    Augments:
        files_dict: information of data files and number of records

    Returns:
        ret: numpy matrix of images (total_images,64,64)
        labels_list: list of labels
        labels_freq: frequncy tables of labels
    """
    grand_max, grand_min = 0, 255
    counter = 0
    white_image = Image.new('L', (64, 64))
    white_background = [255 for x in range(64 * 64)]  # for white background
    white_image.putdata(white_background)
    
    #initialize return labels
    labels_freq = dict()
    labels_list = list()

    #initialize image data matrix
    total_images = np.sum(files_dict[i] for i in files_dict)
    ret = np.ndarray((total_images,64,64), dtype=np.int32)
    print(ret.shape, ret.size)
    
    for filename in files_dict:
        if verbose:
            print(filename)
        Min, Max = 255, 0
        local_count = 0

        for num in range(files_dict[filename]):
            data, img, jis_code = fetch_ETL_Mtype(num, filename, WhiteBackGround=True)
            min, max = np.min(data), np.max(data)
            white_image.paste(img, (0, 1))
            ret[counter] = white_image
            label = str(jis_code)
            labels_list.append(label)
            if counter % (total_images>>3) == 0 and verbose:
                plt.imshow(ret[counter],cmap='gray')
                plt.show()
                print('jis code={}'.format(jis_code))
            counter += 1
            local_count += 1
            if label in labels_freq:
                labels_freq[label] += 1
            else:
                labels_freq[label] = 1
                #print('{} was added.'.format(label), end=' ')
            if min < Min:
                Min = min
            if max > Max:
                Max = max
            if verbose:
                print('filename={:s}, '.format(filename), end='')
                print('record numbers={:d}, '.format(files_dict[filename]), end='')
                print('local_count={:d}'.format(local_count))

            if grand_max < Max:
                grand_max = Max
            if grand_min > Min:
                grand_min = Min
    if verbose:
        print('grand_min={}, grand_max={}'.format(grand_min, grand_max))
        print('counter={}'.format(counter))
    return ret, labels_list, labels_freq, counter == total_images


# In[9]:


def read_record_ETL8G(fd, rec_size=8199, verbose=False):
    """read a recode from a file."""
    rec_size = 8199
    s = fd.read(rec_size)
    r = struct.unpack('>2H8sI4B4H2B30x8128s11x', s)
    iF = Image.frombytes('F', (128, 127), r[14], 'bit', 4)
    #size = (width, hight)
    iL = iF.convert('L')
    if verbose:
        print('Serial: ', r[0])
        print('JIS X 0208 code: {:x}'.format(r[1]))
        print('JIS X 0208 code: {:s}'.format(hex(r[1])))
        print('JIS Typical Reading: {:s}'.format(r[2].decode('utf-8').strip()))
        print('JIS Typical Reading: len{:d}'.format(len(r[2].decode('utf-8').strip())))
        print('Serial Data Number : ', r[3])
        print('Evaluation of Individual Character Image :', r[4])
        print('Evaluation of Character Group: ', r[5])
        print('Male-Female Code ( 1=male, 2=female ):', 'male' if r[6] == 1 else 'female')
        print('Age of Writer: ', r[7])
        print('Industry Classification Code (JIS X 0403): ', r[8])
        print('Occupation Classification Code (JIS X 0404): ', r[9])
        print('Sheet Gatherring Date (19)YYMM: ', r[10])
        print('Scanning Date (19)YYMM: {:d}'.format(r[11]))
        print('Sample Position X on Sheet: ', r[12])
        print('Sample Position Y on Sheet: ', r[13])
        
    return r + (iL,)


def fetch_ETL8(filename, id_record, white_background=True, verbose=False):
    rec_size = 8199
    with open(filename, 'rb') as f:
        f.seek(id_record * rec_size)
        r = read_record_ETL8G(f)
    serial, jis_code = r[0], r[1]
    if white_background:
        iE = Image.eval(r[-1], lambda x: 255-x*16)  # Background: white, and foreground: black
    else:
        iE = Image.eval(r[-1], lambda x: x*16)  # background: black, and foreground: white
    return np.asarray(iE), iE, jis_code, serial

    
def make_data_ETL8(files_dict, verbose=True):
    """Read ETL Mtype data and return numpy matrix and so on.
    
    Augments:
        files_dict: information of data files and number of records
        
    Returns:
        ret: numpy matrix of images (total_images,64,64)
        labels_list: list of labels
        labels_freq: frequncy tables of labels
    """
    target_sizes = (64, 64)
    grand_max, grand_min = 0, 255
    counter = 0
    white_image = Image.new('L', (128, 128))
    white_background = [255 for x in range(128 * 128)]  # for white background
    white_image.putdata(white_background)
    
    #initialize return labels
    labels_freq = dict()
    labels_list = list()

    #initialize image data matrix
    total_images = np.sum(files_dict[i] for i in files_dict)
    ret = np.ndarray((total_images,64,64), dtype=np.int32)
    print(ret.shape, ret.size)
    
    for filename in files_dict:
        if verbose:
            print(filename)
        Min, Max = 255, 0
        local_count = 0
        for num in range(files_dict[filename]):
            data, img, jis_code, serial = fetch_ETL8(filename, num, white_background=True)
            white_image.paste(img, (0, 1))
            
            ret_image = white_image.resize(target_sizes, Image.ANTIALIAS)
            ret[counter] = ret_image
            min, max = np.min(data), np.max(data)
        
            label = str(jis_code)
            labels_list.append(label)
            if counter % (total_images>>3) == 0 and verbose:
                plt.imshow(ret[counter],cmap='gray')
                plt.show()
                print('jis code={}'.format(jis_code))
            counter += 1
            local_count += 1
            if label in labels_freq:
                labels_freq[label] += 1
            else:
                labels_freq[label] = 1
                #print('{} was added.'.format(label), end=' ')
            if min < Min:
                Min = min
            if max > Max:
                Max = max
        if verbose:
            print('filename={:s}, '.format(filename), end='')
            print('record numbers={:d}, '.format(files_dict[filename]), end='')
            print('local_count={:d}'.format(local_count))

        if grand_max < Max:
            grand_max = Max
        if grand_min > Min:
            grand_min = Min
        if verbose:
            print('grand_min={}, grand_max={}'.format(grand_min, grand_max))
            print('counter={}'.format(counter))
    return ret, labels_list


#------------------------------------------------------------------------------


def make_ETL1(verbose=True):
    ETL1_files = {'ETL1/ETL1C_01':11560, 
                  'ETL1/ETL1C_02':11560,
                  'ETL1/ETL1C_03':11560,
                  'ETL1/ETL1C_04':11560,
                  'ETL1/ETL1C_05':11560,
                  'ETL1/ETL1C_06':11560,
                  'ETL1/ETL1C_07':11288,
                  'ETL1/ETL1C_08':11288,
                  'ETL1/ETL1C_09':11287,
                  'ETL1/ETL1C_10':11288,
                  'ETL1/ETL1C_11':11288,
                  'ETL1/ETL1C_12':11287,
                  'ETL1/ETL1C_13':4233}
    ETL1, ETL1_labels, ETL1_labels_freq, is_ok = make_data_ETL_Mtype(ETL1_files,verbose=verbose)
    return ETL1, ETL1_labels

    
def make_ETL6(verbose=True):
    ETL6_files = {'ETL6/ETL6C_01':13800, 
                  'ETL6/ETL6C_02':13800,
                  'ETL6/ETL6C_03':13800,
                  'ETL6/ETL6C_04':13800,
                  'ETL6/ETL6C_05':13800,
                  'ETL6/ETL6C_06':13800,
                  'ETL6/ETL6C_07':13800,
                  'ETL6/ETL6C_08':13800,
                  'ETL6/ETL6C_09':13800,
                  'ETL6/ETL6C_10':13800,
                  'ETL6/ETL6C_11':13800,
                  'ETL6/ETL6C_12':6915}
    #ETL6_total_images = np.sum([ETL6_files[i] for i in ETL6_files])
    ETL6, ETL6_labels, ETL6_labels_freq, is_ok = make_data_ETL_Mtype(ETL6_files,verbose=verbose)
    return ETL6, ETL6_labels


def make_ETL7(verbose=True):
    ETL7_files = {'ETL7/ETL7LC_1':9600, 
                  'ETL7/ETL7LC_2':7200, 
                  'ETL7/ETL7SC_1':9600, 
                  'ETL7/ETL7SC_2':7200}
    #ETL7_total_images = np.sum([ETL7_files[i] for i in ETL7_files])
    ETL7, ETL7_labels, ETL7_labels_freq, is_ok = make_data_ETL_Mtype(ETL7_files, verbose=verbose)
    return ETL7, ETL7_labels

def make_ETL3(verbose=True):
    ETL3_files = {'ETL3/ETL3C_1':4792, 
                  'ETL3/ETL3C_2':4792}
    ETL3, ETL3_labels, ETL3_labels_freq, is_ok = make_data_ETL_Ctype(ETL3_files)
    #data, img, jis_code, serial_number = fetch_ETL_Ctype(filename, 4792, white_background=True)
    return ETL3, ETL3_labels


def make_ETL4(verbose=True):
    ETL4_files = {'ETL4/ETL4C':6112}
    ETL4, ETL4_labels, ETL4_labels_freq, is_ok = make_data_ETL_Ctype(ETL4_files)
    return ETL4, ETL4_labels


def make_ETL5(verbose=True):
    ETL5_files = {'ETL5/ETL5C':6120}
    ETL5, ETL5_labels, ETL5_labels_freq, is_ok = make_data_ETL_Ctype(ETL5_files)
    return ETL5, ETL5_labels

def make_ETL8G(verbose=True):
    ETL8G_filenames = ['ETL8G/ETL8G_{:02d}'.format(i+1) for i in range(32)]
    ETL8G_files = {f:4780 for f in ETL8G_filenames}
    ETL8G_files['ETL8G/ETL8G_33'] = 956
    ETL8G, ETL8G_labels = make_data_ETL8(ETL8G_files,verbose=verbose)
    return ETL8G, ETL8G_labels


def make_ETL9G(verbose=True):
    ETL9G_filenames = ['ETL9G/ETL9G_{:02d}'.format(i+1) for i in range(50)]
    ETL9G_files = {f:12144 for f in ETL9G_filenames}
    ETL9G, ETL9G_labels = make_data_ETL8(ETL9G_files,verbose=verbose)
    return ETL9G, ETL9G_labels


def for_sklearn(data_filename, label_filename, dtype=np.float32):
    #datafilename = 'ETL3_images.hdf5'
    #labelfilename = 'ETL3_labels.pk'

    if not os.path.exists(data_filename):
        print('File {0} does not exist.'.format(data_filename))
        sys.exit()
    if not os.path.exists(label_filename):
        print('File {0} does not exist.'.format(label_filename))
        sys.exit()

    with h5py.File(data_filename,'r') as f:
        data = np.copy(f['Images'])
    #f.close()

    with codecs.open(label_filename,'rb') as f:
        labels = pickle.load(f)
    
    if len(data) != len(labels):
        print('len({0}) is not the same as len({1})'.format(data_filename,label_filename))
        sys.exit()

    if data.ndim != 3:
        print('Image data file was not 3-dim')
        sys.exit()

    image_sizes = (data.shape[1], data.shape[2])
    reshapes = image_sizes[0] * image_sizes[1]
    modified_data = np.ndarray((len(data), reshapes), dtype=dtype)
    for i in range(len(data)):
        modified_data[i] = data[i].reshape(reshapes,)
        
    modified_data /= 255
    
    labels_set = sorted(set(labels))
    lbl2ind = {label:i for i, label in enumerate(labels_set)}
    labels_matrix = np.zeros((len(labels), len(labels_set)))
    for i, label in enumerate(labels):
        labels_matrix[i, lbl2ind[label]] = 1
        
    return modified_data, labels_matrix, lbl2ind


#------------------------------------------------------------------------------


class jis2utf(object):
    """Convert str or int to utf code or chr.

    to_utf(n):
        argument:
            n : str or digit
        return:
            utf code: hex

    to_utfchar(n)
    """
    def __init__(self):
        self.shiftjis = []
        self.jisx0208 = []
        self.unicode = []
        with open("JIS0208.TXT", "r") as f:
            for line in f:
                if line[0] == "#":
                    pass
                else:
                    sjis, jisx, unic, _ = line.strip().split("\t")
                    self.shiftjis.append(int(sjis, base=16))
                    self.jisx0208.append( int(jisx, base=16))
                    self.unicode.append(  int(unic, base=16))

    def to_utf(self, n):
        if isinstance(n, str):
            h = int(n, base=16)
            return self.unicode[self.jisx0208.index(h)]
        else:
            return self.unicode[self.jisx0208.index(n)]

    def to_utfchar(self, n):
        x = self.to_utf(n)
        return chr(x)

#------------------------------------------------------------------------------

def make_all_again():
    ETL1, ETL1_labels = make_ETL1(verbose=False)
    ETL3, ETL3_labels = make_ETL3(verbose=False)
    ETL4, ETL4_labels = make_ETL4(verbose=False)
    ETL5, ETL5_labels = make_ETL5(verbose=False)
    ETL6, ETL6_labels = make_ETL6(verbose=False)
    ETL7, ETL7_labels = make_ETL7(verbose=False)
    ETL8G, ETL8G_labels = make_ETL8G(verbose=False)
    ETL9G, ETL9G_labels = make_ETL9G(verbose=False)

    for data,label in ((ETL1, ETL1_labels),\
                       (ETL3, ETL3_labels),\
                       (ETL4, ETL4_labels),\
                       (ETL5, ETL5_labels),\
                       (ETL6, ETL6_labels),\
                       (ETL7, ETL7_labels),\
                       (ETL8G, ETL8G_labels),\
                       (ETL9G, ETL9G_labels)):
        print(len(data), len(label), type(data), type(label))


#from https://stackoverflow.com/questions/10908877/extracting-a-zipfile-to-memory
#import zipfile
#if sys.version_info[0] == 2:
#    import StringIO
#else:
#    import io
#https://stackoverflow.com/questions/32075135/python-3-in-memory-zipfile-error-string-argument-expected-got-bytes

class InMemoryZip(object):

    def __init__(self):
        # Create the in-memory file-like object for working w/imz
        #self.in_memory_zip = io.StringIO()
        self.in_memory_zip = io.BytesIO()

    # Just zip it, zip it
    def append(self, filename_in_zip, file_contents):
        # Appends a file with name filename_in_zip and contents of
        # file_contents to the in-memory zip.
        # Get a handle to the in-memory zip in append mode
        zf = zipfile.ZipFile(self.in_memory_zip, "a", zipfile.ZIP_DEFLATED, False)
        self.in_memory_zip.debug = 3
        
        # Write the file to the in-memory zip
        zf.writestr(filename_in_zip, file_contents)
        
        # Mark the files as having been created on Windows so that
        # Unix permissions are not inferred as 0000
        for zfile in zf.filelist:
            zfile.create_system = 0
        return self

    def read(self):
        # Returns a string with the contents of the in-memory zip.
        self.in_memory_zip.seek(0)
        return self.in_memory_zip.read()

    # Zip it, zip it, zip it
    def writetofile(self, filename):
        zf = zipfile.ZipFile(self.in_memory_zip, 'w', zipfile.ZIP_DEFLATED, False)
        zf.writestr(filename, self.read())
        #f = codecs.open(filename,'wb')
        #f.write(self.read())
        #f.close()
        #zipfile.ZipFile.writestr(filelan)
        #self.in_memory_zip.writestr(filename)
        # Writes the in-memory zip to a file.
        #f = file.open(filename, 'wb')
        #f.write(self.read())
        #f.close()
        #with codecs.open(filename,'wb') as f:
        #f = file(filename, "wb")
        #    f.write(self.read())




