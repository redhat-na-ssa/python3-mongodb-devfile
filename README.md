# OpenShift Dev Spaces (Eclipse Che project) Sample for Python + MongoDB development

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
   
   db.books.insertMany(
      [ 
        {
          _id: '001',
          title: 'Openshift 101',
          author: 'Red Hat',
          synopsis: 'Learning Openshift'
        },
        {
          _id: '002',
          title: 'Python in Action',
          author: 'Python',
          synopsis: 'Learning python'
        },
        {
          _id: '003',
          title: 'Java in Action',
          author: 'Sun',
          synopsis: 'The Java programming language'
        }
      ]
   )

   db.books.find()
   ```

## Port-forwarding mongodb to your local machine

If you need to connect a local client tool (eg. Mongo Compass) to the mongodb instance running inside your DevWorkspace Pod on Openshift, you can do that by

> Note: you need to have the Openshift CLI tool `oc` in your system path.
get an API toke by requesting https://oauth-openshift.apps.your-cluster-domain/oauth/token/request

```bash
oc login https://api.apps.your-cluster-domain:6443 --token='YOUR TOKEN HERE'
oc get svc
NAME                                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                                     AGE
workspaced2ed88cfa73a4091-service   ClusterIP   172.30.233.191   <none>        3030/TCP,27017/TCP,13131/TCP,13132/TCP,13133/TCP,8000/TCP   17m

oc port-forward service/workspaced2ed88cfa73a4091-service 27017:27017
Forwarding from 127.0.0.1:27017 -> 27017
Forwarding from [::1]:27017 -> 27017
```

Now you can connect using the URL `mongodb://localhost:27017/`