{
	"make_global_settings": [
    		["CXX", "/usr/bin/g++-4.9"]
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
