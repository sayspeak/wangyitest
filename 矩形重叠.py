#! /usr/bin/env python
#coding:utf-8
a = int(input())
b = int(input())
aliquot = [ x for x in range(a,b) if x%3==0 ]
print(len(aliquot))