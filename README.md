## Help :
#####   This is a python project that parses the configuration file for the "key = value" type.
## Usage :
#### analysis.conf
    # remark ...
	key1 = value1
	key2 = value2
	
------------
#### Create a ConfigAnalysis object:
    from pyConfigAnalysis import ConfigAnalysis
    config = ConfigAnalysis()
	config.read("analysis.conf")
#### Get all of the key:
    config.keys()
	->["key1","key2"]
#### Get the value from a key:
    config.get("key1")
	->"value1"
#### Update a configuration
    config.update("key2","newvalue2")
	#check
	config.get("key2")
	->"newvalue2"
	#save to configuration file
	config.save()
#### Add a configuration
    config.add("key3","value3")
	#check
    config.get("key3")
	->"value3"
	#save to configuration file
    config.save()