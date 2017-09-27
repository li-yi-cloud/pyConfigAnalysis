## Help :
#####   A python project about to analysis the type of "key = value" configuration file.
## Usage :
#### analysis.conf
    # about ...
	key1 = value1
	key2 = value2
	
------------
    from py-ConfigAnalysis import ConfigAnalysis
    config = ConfigAnalysis()
	config.read("analysis.conf")
#### Get all of the key:
    config.keys()
	->["key1","key2"]
#### Get the value from a key:
    config.get("key1")
	->"value1"
