import numpy as np
import torch


class DataLoader(object):
    def __init__(self, dataset,
                 batch_size=1):
        self.dataset1 = dataset[0]
        self.dataset2 = dataset[1]
        self.batch_size = batch_size

        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= 1:
            raise StopIteration()

        x = torch.LongTensor(self.dataset1)
        t = torch.LongTensor(self.dataset2)

        self._idx += self.batch_size

        return x, t
