# -*- coding: utf-8 -*-
'''Utility functions for managing ETL hand writting dataset.

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
for file in ETL1.zip ETL3.zip ETL4.zip ETL5.zip ETL6.zip ETL7.zip ETL8G.zip ETL9G.zip; do  wget "http://etlcdb.db.aist.go.jp/etlcdb/data/${file}"
```

You would be able to get the files blow.

```
-rw-r--r-- 1 asakawa  579975229 Mar 31 09:45 ETL1.npz
-rw-r--r-- 1 asakawa   39334155 Mar 31 09:45 ETL3.npz
-rw-r--r-- 1 asakawa   25109563 Mar 31 09:45 ETL4.npz
-rw-r--r-- 1 asakawa   25142211 Mar 31 09:45 ETL5.npz
-rw-r--r-- 1 asakawa  651368618 Mar 31 09:45 ETL6.npz
-rw-r--r-- 1 asakawa  137895867 Mar 31 09:45 ETL7.npz
-rw-r--r-- 1 asakawa  633534613 Mar 31 09:45 ETL8G.npz
-rw-r--r-- 1 asakawa 2499287067 Mar 31 09:45 ETL9G.npz
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

'''

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

TARGETSIZE = (32, 32)
(TARGET_HEIGHT, TARGET_WIDTH) = TARGETSIZE

def get_data(filename, forceDownload=False):
    """Downloading data from Tokyo Women's Christian univ.

    Example:
        dataset.get_data('ETL8G.npz')
    """

    url = 'https://www.cis.twcu.ac.jp/~asakawa/ETL'
    size_dict = {
        'ETL1.npz': 579975229,
        'ETL3.npz': 39334155,
        'ETL4.npz': 25109563,
        'ETL5.npz': 25142211,
        'ETL6.npz': 651368618,
        'ETL7.npz': 137895867,
        'ETL8G.npz': 633534613,
        'ETL9G.npz': 2499287067
    }
 
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


#----------------------------------------------------------------------------

def download_all():
    filenames = ['ETL1.npz', 'ETL3.npz', 'ETL4.npz', 'ETL5.npz', 'ETL6.npz',
                 'ETL7.npz', 'ETL8G.npz', 'ETL9G.npz']

    for filename in filenames:
        get_data(filename, forceDownload=False)


#----------------------------------------------------------------------------
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
    ETL1, ETL1_labels, ETL1_freq, is_ok = make_data_ETL_Mtype(ETL1_files,verbose=verbose)
    return ETL1, ETL1_labels, ETL1_freq


def make_ETL3(verbose=True):
    ETL3_files = {'ETL3/ETL3C_1':4792, 
                  'ETL3/ETL3C_2':4792}
    ETL3, ETL3_labels, ETL3_freq, is_ok = make_data_ETL_Ctype(ETL3_files)
    #data, img, jis_code, serial_number = fetch_ETL_Ctype(filename, 4792, white_background=True)
    return ETL3, ETL3_labels, ETL3_freq


def make_ETL4(verbose=True):
    ETL4_files = {'ETL4/ETL4C':6112}
    ETL4, ETL4_labels, ETL4_freq, is_ok = make_data_ETL_Ctype(ETL4_files)
    return ETL4, ETL4_labels, ETL4_freq


def make_ETL5(verbose=True):
    ETL5_files = {'ETL5/ETL5C':6120}
    ETL5, ETL5_labels, ETL5_freq, is_ok = make_data_ETL_Ctype(ETL5_files)
    return ETL5, ETL5_labels, ETL5_freq

    
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
    ETL6, ETL6_labels, ETL6_freq, is_ok = make_data_ETL_Mtype(ETL6_files,verbose=verbose)
    return ETL6, ETL6_labels, ETL6_freq


def make_ETL7(verbose=True):
    ETL7_files = {'ETL7/ETL7LC_1':9600, 
                  'ETL7/ETL7LC_2':7200, 
                  'ETL7/ETL7SC_1':9600, 
                  'ETL7/ETL7SC_2':7200}
    #ETL7_total_images = np.sum([ETL7_files[i] for i in ETL7_files])
    ETL7, ETL7_labels, ETL7_freq, is_ok = make_data_ETL_Mtype(ETL7_files, verbose=verbose)
    return ETL7, ETL7_labels, ETL7_freq

def make_ETL8G(verbose=True):
    ETL8G_filenames = ['ETL8G/ETL8G_{:02d}'.format(i+1) for i in range(32)]
    ETL8G_files = {f:4780 for f in ETL8G_filenames}
    ETL8G_files['ETL8G/ETL8G_33'] = 956
    ETL8G, ETL8G_labels, ETL8G_freq, is_ok = make_data_ETL_Gtype(ETL8G_files,verbose=verbose)
    return ETL8G, ETL8G_labels, ETL8G_freq


def make_ETL9G(verbose=True):
    ETL9G_filenames = ['ETL9G/ETL9G_{:02d}'.format(i+1) for i in range(50)]
    ETL9G_files = {f:12144 for f in ETL9G_filenames}
    ETL9G, ETL9G_labels, ETL9G_freq, is_of = make_data_ETL_Gtype(ETL9G_files,verbose=verbose)
    return ETL9G, ETL9G_labels, ETL9G_freq


#----------------------------------------------------------------------------
# Ctype
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

def make_data_ETL_Ctype(files_dict, target_size=TARGETSIZE, verbose=True):
    """Read ETL C-type data and return numpy matrix such ask ETL3, ETL4, and ETL5.
    
    Also, this function resize images to (TARGET_HEIGHT, TARGET_WIDTH)
    
    Augments:
        files_dict: information of data files and number of records
        
    Returns:
        ret: numpy matrix of images (total_images, TARGET_HEIGTH, TARGET_WIDTH)
        labels_list: list of labels
        labels_freq: frequncy tables of labels
    """
    grand_max, grand_min = 0, 255
    counter = 0
    white_image = Image.new('L', (76, 76))
    white_background = [255 for x in range(76 * 76)]  # for white background
    white_image.putdata(white_background)    
    #initialize return labels
    freqs, labels_list = dict(), list()
    
    #initialize image data matrix
    total_images = np.sum(files_dict[i] for i in files_dict)
    ret = np.ndarray((total_images, target_size[0], target_size[1]), dtype=np.int32)
    if verbose:
        print(ret.shape, ret.size)
    
    for filename in files_dict:
        if verbose:
            print('filename: {}'.format(filename))
        Min, Max, local_count = 255, 0, 0
        for num in range(files_dict[filename]):
            data, img, jis_code, serial_number = fetch_ETL_Ctype(filename, 
                                                                 num, 
                                                                 white_background=True)
            min, max = np.min(data), np.max(data)
            white_image.paste(img, (0, 0))
            ret_image = white_image.resize(target_size, Image.ANTIALIAS)
            ret[counter] = ret_image
            label = str(jis_code)
            labels_list.append(label)
            if counter % (total_images>>3) == 0 and verbose:
                plt.imshow(ret[counter],cmap='gray')
                plt.show()
                print('jis code={}'.format(jis_code))
            counter += 1
            local_count += 1
            if label in freqs:
                freqs[label] += 1
            else:
                freqs[label] = 1

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
    return ret, labels_list, freqs, counter == total_images


#------------------------------------------------------------------------------
# Mtype
def fetch_ETL_Mtype(num,
                    filename='ETL7/ETL7LC_1', 
                    rec_size=2052,            #ETL_Mtype_rec_size,
                    img_sizes=(64, 63),       #ETL_Mtye_image_sizes,
                    WhiteBackGround=True,
                    dtype=np.int32):
    """Get an image of ETL M-type. such as ETL1, ETL6, and ETL7."""
        
    #ETL_Mtype_rec_size = 2052
    ETL_Mtype_rec_size = rec_size
    ETL_Mtype_img_sizes = (64, 63)            #size = (width, hight), for ETL1, 6, and 7
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
        img = Image.eval(iL, lambda x: 255-x*16)  # Background: white, and foreground: black
    else:
        img = Image.eval(iL, lambda x: x*16)  # background: black, and foreground: white
    return np.asarray(img, dtype=dtype), img, jis_code


def make_data_ETL_Mtype(files_dict, target_size=TARGETSIZE, verbose=True):
    """Read ETL Mtype data and return numpy matrix and so on.
    
    Augments:
        files_dict: information of data files and number of records

    Returns:
        ret: numpy matrix of images (total_images, TARGET_HEIGHT, TARGET_WIDTH)
        labels_list: list of labels
        labels_freq: frequncy tables of labels
    """
    grand_max, grand_min, counter = 0, 255, 0
    white_image = Image.new('L', (64, 63))
    white_background = [255 for x in range(64, 63)]  # for white background
    white_image.putdata(white_background)
    
    #initialize return labels
    freqs, labels_list = dict(), list()

    #initialize image data matrix
    total_images = np.sum(files_dict[i] for i in files_dict)
    ret = np.ndarray((total_images, target_size[0], target_size[1]), dtype=np.int32)
    #print(ret.shape, ret.size)
    
    for filename in files_dict:
        if verbose:
            print(filename)
        Min, Max, local_count = 255, 0, 0

        for num in range(files_dict[filename]):
            data, img, jis_code = fetch_ETL_Mtype(num, filename, WhiteBackGround=True)
            min, max = np.min(data), np.max(data)
            #white_image.paste(img, (0, 1))
            white_image.paste(img, (0, 0))
            ret_image = white_image.resize(target_size, Image.ANTIALIAS)
            #ret[counter] = white_image
            ret[counter] = ret_image
            label = str(jis_code)
            labels_list.append(label)

            if counter % (total_images>>3) == 0 and verbose:
                plt.imshow(ret[counter], cmap='gray')
                plt.show()
                print('jis code={}'.format(jis_code))
            counter += 1
            local_count += 1
            if label in freqs:
                freqs[label] += 1
            else:
                freqs[label] = 1
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
    return ret, labels_list, freqs, counter == total_images


#------------------------------------------------------------------------------
# Gtype 
def read_record_ETL_Gtype(fd, rec_size=8199, verbose=False):
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


def fetch_ETL_Gtype(filename, id_record, white_background=True, verbose=False):
    rec_size = 8199
    with open(filename, 'rb') as f:
        f.seek(id_record * rec_size)
        r = read_record_ETL_Gtype(f)
    serial, jis_code = r[0], r[1]
    if white_background:
        iE = Image.eval(r[-1], lambda x: 255-x*16)  # Background: white, and foreground: black
    else:
        iE = Image.eval(r[-1], lambda x: x*16)  # background: black, and foreground: white
    return np.asarray(iE), iE, jis_code, serial

    
def make_data_ETL_Gtype(files_dict, target_size=TARGETSIZE, verbose=True):
    """Read ETL Mtype data and return numpy matrix and so on.
    
    Arguments:
        files_dict: information of data files and number of records
        
    Returns:
        ret: numpy matrix of images (total_images, TARGET_HEIGHT, TARGET_WIDTH)
        labels_list: list of labels
        labels_freq: frequncy tables of labels
    """

    grand_max, grand_min = 0, 255
    counter = 0
    white_image = Image.new('L', (128, 127))
    white_background = [255 for x in range(128 * 127)]  # for white background
    white_image.putdata(white_background)
    
    #initialize return labels
    freqs, labels_list = dict(), list()

    #initialize image data matrix
    total_images = np.sum(files_dict[i] for i in files_dict)
    ret = np.ndarray((total_images, target_size[0], target_size[1]), dtype=np.int32)
    print(ret.shape, ret.size)
    
    for filename in files_dict:
        if verbose:
            print(filename)
        Min, Max = 255, 0
        local_count = 0
        for num in range(files_dict[filename]):
            data, img, jis_code, serial = fetch_ETL_Gtype(filename, num, white_background=True)
            white_image.paste(img, (0, 1))
            
            ret_image = white_image.resize(target_size, Image.ANTIALIAS)
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
            if label in freqs:
                freqs[label] += 1
            else:
                freqs[label] = 1
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
    return ret, labels_list, freqs, counter == total_images

#-----------------------------------------------------------------------------


def make_all():
    main()
    
def main():
    ETL1, ETL1_label, ETL1_freq = make_ETL1(verbose=False)
    ETL3, ETL3_label, ETL3_freq = make_ETL3(verbose=False)
    ETL4, ETL4_label, ETL4_freq = make_ETL4(verbose=False)
    ETL5, ETL5_label, ETL5_freq = make_ETL5(verbose=False)
    ETL6, ETL6_label, ETL6_freq = make_ETL6(verbose=False)
    ETL7, ETL7_label, ETL7_freq = make_ETL7(verbose=False)
    ETL8G, ETL8G_label, ETL8G_freq = make_ETL8G(verbose=False)
    ETL9G, ETL9G_label, ETL9G_freq = make_ETL9G(verbose=False)

    ETLs = {'ETL1': (ETL1, ETL1_label, ETL1_freq),
            'ETL3': (ETL3, ETL3_label, ETL3_freq),
            'ETL4': (ETL4, ETL4_label, ETL4_freq),
            'ETL5': (ETL5, ETL5_label, ETL5_freq),
            'ETL6': (ETL6, ETL6_label, ETL6_freq),
            'ETL7': (ETL7, ETL7_label, ETL7_freq),
            'ETL8G': (ETL8G, ETL8G_label, ETL8G_freq),
            'ETL9G':(ETL9G, ETL9G_label, ETL9G_freq),
    }
    import os

    for key, values in ETLs.items():
        (data,label,freq) = ETLs[key]
        print('len(data):{0}, len(label):{1}, len(freq):{2}'.format(len(data),
                                                                    len(label),
                                                                    len(freq)))
        filename_tobesaved = key + '.npz'
        if os.path.isfile(filename_tobesaved):
            print('Overwriting {0}...'.format(key + '.npz'))
            np.savez(filename_tobesaved, data, label, freq)


if __name__ == "__main__":
    # execute only if run as a script
    main()

