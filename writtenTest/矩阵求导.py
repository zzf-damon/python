#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Matrix:
    def __init__(self, shape, data: list):
        self.shape = shape
        self.data = data
        self.length = self.shape[0] * self.shape[1]

    def _verify(self, location):
        assert location[0] < self.shape[0] and location[1] < self.shape[1]

    def __getitem__(self, location):
        self._verify(location)
        return self.data[location[0] * self.shape[1] + location[1]]

    def __setitem__(self, location, value: int):
        self._verify(location)
        self.data[location[0] * self.shape[1] + location[1]] = value

    def transpose(self):
        transposed_data = [self.data[i * self.shape[1] + j] for j in range(self.shape[1]) for i in range(self.shape[0])]
        return Matrix((self.shape[1], self.shape[0]), transposed_data)

    def reshape(self, shape):
        self.shape = shape

    @staticmethod
    def matmul(ma, mb):
        assert ma.shape[1] == mb.shape[0]
        mc = Matrix.zeros((ma.shape[0], mb.shape[1]))
        for i in range(mc.shape[0]):
            for j in range(mc.shape[1]):
                mc[i, j] = sum([ma[i, k] * mb[k, j] for k in range(ma.shape[1])])
        return mc

    def __add__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value + other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] + other.data[i] for i in range(self.length)])

    def __sub__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value - other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] - other.data[i] for i in range(self.length)])

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value * other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] * other.data[i] for i in range(self.length)])

    @staticmethod
    def zeros(shape):
        return Matrix(shape, [0 for _ in range(shape[0] * shape[1])])

    @staticmethod
    def ones(shape):
        return Matrix(shape, [1 for _ in range(shape[0] * shape[1])])

    def print(self):
        print(",".join([str(i) for i in self.data]))

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value * other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] * other.data[i] for i in range(self.length)])

    @staticmethod
    def zeros(shape):
        return Matrix(shape, [0 for _ in range(shape[0] * shape[1])])

    @staticmethod
    def ones(shape):
        return Matrix(shape, [1 for _ in range(shape[0] * shape[1])])

    def print(self):
        print(",".join([str(i) for i in self.data]))


class Matrix3D:
    def __init__(self, shape, data: list):
        self.shape = shape
        self.data = data
        self.length = self.shape[0] * self.shape[1] * self.shape[2]

    def _verify(self, location):
        assert location[0] < self.shape[0] and location[1] < self.shape[1] and location[2] < self.shape[2]

    def __getitem__(self, location):
        self._verify(location)
        return self.data[location[0] * (self.shape[1] * self.shape[2]) + location[1] * self.shape[2] + location[2]]

    def __setitem__(self, location, value: int):
        self._verify(location)
        self.data[location[0] * (self.shape[1] * self.shape[2]) + location[1] * self.shape[2] + location[2]] = value

    def get_2D_slice(self, index):
        offset = self.shape[1] * self.shape[2]
        loc = index * offset
        return Matrix((self.shape[1], self.shape[2]), self.data[loc:loc + offset])

    def reshape(self, shape):
        self.shape = shape

    @staticmethod
    def zeros(shape):
        return Matrix3D(shape, [0 for _ in range(shape[0] * shape[1] * shape[2])])

    @staticmethod
    def ones(shape):
        return Matrix3D(shape, [1 for _ in range(shape[0] * shape[1] * shape[2])])

    def print(self):
        print(",".join([str(i) for i in self.data]))
