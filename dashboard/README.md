# Performance Dashboard

This is a App Engine web app for displaying and monitoring performance
test results.

See
[online documentation](http://www.chromium.org/developers/speed-infra/performance-dashboard).

## Prerequisites

Running the tests, running the local server and
deploying all depends on having the [the App Engine
SDK](https://cloud.google.com/appengine/downloads).

After downloading and unpacking, you should add the path to the SDK to
both `PATH` and `PYTHONPATH`.

## Running the tests

To run all of the unit tests, you can run `bin/run_tests`. You can also
pass the import path to the test module to run a particular test, for
example `bin/run_tests dashboard.utils_test`.

## To run locally

Run `bin/dev_server`; this sets up a temporary directory, adds links to
required libraries, and calls `dev_appserver.py` on that directory.  By
default, this starts a server on [localhost:8080](http://localhost:8080/).

To load sample graph or alert data from production, navigate to
[/load_from_prod](http://localhost:8080/load_from_prod).

## Deploying to production

To deploy, you can run `bin/deploy`, which prepares the
code to be deployed and runs `appcfg.py`. Note that this
doesn't set the new version as the default version; to do
this, you can use the versions page on the [Google Developers
Console](https://console.developers.google.com/) if you have edit or
owner permissions for the App Engine project; otherwise if you want to
request to set a new default version for chromeperf.appspot.com you can
contact chrome-perf-dashboard-team@google.com.

WARNING: Some changes to production may not be easily reversible; for
example `appcfg.py ... vacuum_indexes` will remove datastore indexes that
are not in your local index.yaml file, which may take more than 24 hours,
and will disable any queries that depend on those indexes.

## Debugging in production

See [cloud-debugger.md](/dashboard/cloud-debugger.md).
