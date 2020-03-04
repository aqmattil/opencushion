{
	"make_global_settings": [
    		["CXX", "/usr/bin/g++"]
  	],
	"link_settings": {
		"libraries": [
  			"-lwiringPi"
		],
	}, 
 	"targets": [
    		{
      			"target_name": "hx711",
      			"sources": [ "binding.cpp", "hx711.cpp" ],
    			"ldflags": [ "-lwiringPi" ]
		}
  	]
}
