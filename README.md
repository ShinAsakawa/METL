# METL

METL is a (M)odified ETL Japanese handwriting characters dataset.

- Please refer to [ETL](http://www.is.aist.go.jp/etlcdb/)

- Yu Qiao's [page](https://www.gavo.t.u-tokyo.ac.jp/~qiao/database.html)


All the images were convereted to 64 X 64 pixels gray scale

first, you must download all the database:

```python
import METL
METL.download_all()
```

When you want to use `ETL8G` database, you would type like:
```
ETL8G = METL.load_images_hdf5('ETL8G_images.hdf5')
ETL8G_labels = METL.load_labels_pickle('ETL8G_labels.pk')
```

```python
ETL8G.shape
len(ETL8G_labels)
```

you would like to get belows:

```
(153916, 64, 64)
153916
```

- When you want to convert the data to try `sklearn`, then you can try `.for_sklera()`:

```python
data, label = ETL.for_sklern('ETL8G_images.hdf5', 'ETL8G_labes.pk')
```

Enjoy!
