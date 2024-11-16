
# AltiusHub Assignment

Follow these steps to run this project on your gcp service account.

* Install dependencies from requirements.txt
* python manage.py runserver


## APIs & Permissions

To run this project in GCP, a set of APIs has to be enabled so that the different services can connect to each other:

* Secret Manager API
* Cloud Build API
* Cloud SQL Admin API
* Compute Engine API
* Cloud Logging API
* App Engine API
* Identity and Access Management (IAM) API
* App Engine Admin API


## Considerations and optimizations possible if time given

* Add db indexing for faster queries performance
* Finish frontend
* Adding some quirky apis before first frontend call goes and store csrf token in session probably use interceptors here ( Like i've used for refreshing access tokens but couldn't make any api calls to test it due to lack of time )
* Make controllers in django pure functions so they're easy to test
* I've followed standards like pagination and versioning but more restful standards could be added
* Use asynchronous server


## Errors that took my time 

* I thought it's a good idea to document my apis although for some reason my models and views won't show up in swagger documentation. This wasted good minutes and I couldn't resolve it in time.
* So i've tested the things on django admin and they work fine there but yeah having it on swagger would've made it much better.
* Configuring gcp bucket settings on the django side. So i configured gcp bucket and public permissions quickly but it was first time in django so that took good time and still I'm unsure of few settings.
[ for now it's ofc the basic setting so it uploads it on the server side itself]


