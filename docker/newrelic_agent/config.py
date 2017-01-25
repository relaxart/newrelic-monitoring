import os
import sys
import string
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="/usr/local/bin/agent/")
templateEnv = jinja2.Environment(loader=templateLoader)
newrelicKey = os.environ['NEWRELIC_KEY']

def read_env_to_list(prefix):
	"This function read env variables like PSQL_HOST_TMS"
	"to list of dictionaries first level will be list"
	"with dictionaries inside like host,port and others"

	previx_len = len(prefix)

	result = {}

	for key, value in os.environ.iteritems():
		if prefix == key[:previx_len]:
			env = key[previx_len:].split("_")
			if len(env) == 2:
				d = result.setdefault(env[1], {})
				d[env[0]] = value
				
			else:
			 	print "ENV configuration is wrong"
			 	sys.exit(2)

	return result

configuration = {}
configuration['postgres'] = read_env_to_list("NPOSTGRES_")
configuration['redis'] = read_env_to_list("NREDIS_")

template = templateEnv.get_template("config.template.yaml")
templateVars = { 
	"NEWRELIC_KEY" : newrelicKey,
    "configuration" : configuration 
}

print template.render( templateVars )