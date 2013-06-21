dropwizard-health-check-monitor
===============================

This is a very rudimentary tool for calling the healthchecks on a series of dropwizard instances and reporting an error if any of the healthchecks reports an error.

Usage:

python healthcheck.py example-config.txt


where

example-config.txt is a file containing the URL's of the healthcheck page for each dropwizard service instance.



This is the first version.  I'll be enhanching this over time.
