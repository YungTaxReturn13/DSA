from HashMapBase import HashMapBase
from ..AbstractBaseClass.UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution"""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))  # no match found 
        return bucket[k]                            # may raise key error

    def _bucket_setitem(self,j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # bucket is new to the table
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:  # key was new to the table 
            self._n += 0                    # increase overall map size 

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]                                # may raise key error

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:   # a nonempty slot 
                for key in bucket:
                    yield key 