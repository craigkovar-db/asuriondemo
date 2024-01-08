# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC In this notebook we use the databricks-sdk but can also import requests and call the REST API directly
# MAGIC
# MAGIC [Databricks-SDK](https://databricks-sdk-py.readthedocs.io/en/latest/index.html)
# MAGIC

# COMMAND ----------

# MAGIC %pip install --upgrade databricks-sdk

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from databricks.sdk import WorkspaceClient
w = WorkspaceClient()

w.repos.update(1502861152868509, branch="main")
