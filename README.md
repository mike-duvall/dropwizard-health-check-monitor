#dropwizard-health-check-monitor


This is a very rudimentary tool for calling the healthchecks on a series of dropwizard instances and reporting an error if any of the healthchecks reports an error.

##Usage:

python healthcheck.py example-config.txt


where

example-config.txt is a file containing the URL's of the healthcheck page for each dropwizard service instance.


I currently use this by having  my CI tool run this healthcheck every 5 minutes.  If it fails, my build radiator turns red and I get an email.


This is the initial version.  I'll be enhanching this over time.


## Next steps

* Update to check for non-200 return code rather than looking for the word "ERROR" in the response
* Add better error reporting
* Run checks for all servers instead of stopping if one fails
