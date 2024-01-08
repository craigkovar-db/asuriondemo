# Databricks notebook source
# MAGIC %pip install --upgrade databricks-sdk

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from databricks.sdk import WorkspaceClient
w = WorkspaceClient()

w.repos.update(1502861152868509, branch="main")

# COMMAND ----------

import os

path = '/Workspace/Users/craig.kovar@databricks.com'
dir = 'dir1'

full_path = os.path.join(path,dir)
    
with open(f'{full_path}/new_file.txt', "r") as f:
    name_string = f.readline()

print(f"Hello {name_string}, this is initial message!")
