# Databricks notebook source
import os

path = '/Workspace/Users/craig.kovar@databricks.com'
dir = 'dir1'

full_path = os.path.join(path,dir)
    
with open(f'{full_path}/new_file.txt', "r") as f:
    name_string = f.readline()

print(f"Hello {name_string}, this is an updated message!")
