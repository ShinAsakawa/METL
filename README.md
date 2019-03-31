# METL

METL is a (M)odified ETL Japanese handwriting characters dataset.

- Please refer to [ETL](http://www.is.aist.go.jp/etlcdb/)

- Yu Qiao's [page](https://www.gavo.t.u-tokyo.ac.jp/~qiao/database.html)


All the images were convereted to 32 x 32 pixels gray scale

first, you must download all the database:

```python
import numpy as np
import METL as metl
metl.get_data('ETL3.npz')
a = np.load('ETL3.npz')
X, y, _ = a['arr_0'].reshape(-1,32*32), a['arr_1']
from sklearn.neuralnetwork import MLPClassifier as mlp
model = mlp
model.fit(X,y)
```

When you want to use `ETL8G` database, you would type like:
```python
metl.get_data('ETL8G.npz')
ETL8G = np.load('ETL8g.npz')

for x in ETL8G:
  prit(x, len(x))
```

Enjoy!
