## Help :
#####   A python project that parses the configuration file for "key = value" type.
## Usage :
#### analysis.conf
    # remark ...
	key1 = value1
	key2 = value2
	
------------
#### Create a ConfigAnalysis object:
    from py-ConfigAnalysis import ConfigAnalysis
    config = ConfigAnalysis()
	config.read("analysis.conf")
#### Get all of the key:
    config.keys()
	->["key1","key2"]
#### Get the value from a key:
    config.get("key1")
	->"value1"
