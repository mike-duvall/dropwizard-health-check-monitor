#dropwizard-health-check-monitor


This is a very rudimentary tool for calling the healthchecks on a series of dropwizard instances and reporting an error if any of the healthchecks reports an error.

##Usage:

python healthcheck.py example-config.txt


where

example-config.txt is a file containing the URL's of the healthcheck page for each dropwizard service instance.



This is the first version.  I'll be enhanching this over time.

The way I currently use this is I have my CI tool run this healthcheck every 5 minutes.  If it fails, my build radiator turns red and I get an email.

## Next steps

* Add better error reporting
* Run checks for all servers instead of stopping if one fails
