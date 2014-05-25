#Application Kernels in the RADICAL software stack

##Introduction

Application Kernels are DCI-specific descriptions of applications.
Using this abstraction it allows users to specify that they want to run a
certain application and don't need to care about the specific module that needs
to be loaded or a certain path that a binary is available.

##Structure of description

Currently there is a JSON file per application.

The application can be described for every resource with two parameters:
* "executable" - The command to execute the application.
* "pre\_exec" - Configuration commands needed to run prior to the start of the
application (e.g. "module load").

There is also a "DEFAULT" section for convenience.

All together a kernel\_app.json should look like:
```json
{
    "DEFAULT": {
        "executable": "default.bin"
    },
    "resource1": {
        "executable": "non-default.bin"
        "pre_exec": "module load X"
    },
    "resource2": {
        "pre_exec": ["module load X", "module load Y"]
    },
    "resource3": {
    }
}
```

## Available Application Kernels

Currently these are available:

* [NAMD](namd.json)

Feel free to submit your own so that we can capture and reuse as much of this
information as possible.
