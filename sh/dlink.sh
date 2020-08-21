#!/bin/bash
# Maintainer: Faris Chugthai

#for i in /data/data/com.termux/files/usr/lib/byobu/**; do
for i in "$1"; do
  ln -s "$i"
done
