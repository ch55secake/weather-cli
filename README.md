# weather-cli
Weather information on the command line
# Usage 

This will get current weather information for London (by default) location is an optional parameter. This will work provided 
the ``init`` command has already been run, as this relies on existing configuration that is stored in ``$HOME/.config/weather-cli``. 

You can also provide the flag ``--json`` (disabled by default) to receive the current weather info as JSON, this is incase you want to pass 
the data to a different tool (my personal motive for writing this). 

```bash
weather-cli get 
```

Providing a path to the init is optional as mentioned above, although you may want to put the configuration elsewhere. 

```bash
weather-cli init <key> <path-optional>
```

# Installation 

Under construction or something idek 