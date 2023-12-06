#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("youssef_append.txt", "Youssef is so cool!\n")
print(nb_characters_added)
