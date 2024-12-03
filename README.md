# weather-cli
Weather information on the command line
# Usage 

This will get current weather information for London (by default) location is an optional parameter. This will work provided 
the ``init`` command has already been run, as this relies on existing configuration that is stored in ``$HOME/.config/weather-cli``. 

You can also provide the flag ``--json`` (disabled by default) to receive the current weather info as JSON, this is incase you want to pass 
the data to a different tool (my personal motive for writing this). 

```bash
 weather-cli get 
 ☁ Currently it feels like 1 °C in London.
  * It is actually 4 °C.
  * It's partly cloudy.
```

Providing a path to the init is optional as mentioned above, although you may want to put the configuration elsewhere. 

```bash
 weather-cli init <key> <path-optional>
```

# Installation and prerequisites 

In order to install the tool, you need to have at least ``python@3.12`` and ``pip3``. 

This tool also then expects that you correctly set the path variables for your ``pip3`` and ``python``
installations, for example the ones that I currently have set in my zsh profile are: 

```bash
 export PATH="$HOME/.local/bin:$PATH"
 export PATH="$HOME/Library/Python/3.12/bin:$PATH"
```

Once requirements are satisfied, you can either build the project yourself by running: 

```bash
 poetry build -o release && 
 pip3 install $CURRENT_DIRECTORY/release/weathercli-1.x.xx-py3-none-any.whl
```

You can also download the latest wheel from [here](https://github.com/ch55secake/weather-cli/releases). However, that still requires that 
you run: 
```bash
 pip3 install $CURRENT_DIRECTORY/weathercli-1.x.xx-py3-none-any.whl
```


