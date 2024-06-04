# Openshift DevSpaces (EclipseChe project) Sample for Python + MongoDB development

[![Contribute](https://www.eclipse.org/che/contribute.svg)](https://{openshift_dev_spaces_url}/#https://{your_git_repository_url})

This repo contains two pieces to show case Python coding
 * A simple program that displays “Hello, World!”. It's often used to illustrate the syntax of the language.
 * A full CRUD Rest API service using [FastAPI](https://fastapi.tiangolo.com/) and [PyMongo](https://pypi.org/project/pymongo/). This service is based on the original [Mongo's pymongo tutorial](https://github.com/mongodb-developer/pymongo-fastapi-crud/tree/main) 

## Devfile tasks definitions

 * `Run Tasks -> devfile`
   * `Run the Hello World Program` 
   * `Start pymongo-fastapi-crud app`
   * `Start mongosh-cli`

   ```shell
   show dbs
   use pymongo_tutorial
   show tables
   books.movies.find()
   ```
