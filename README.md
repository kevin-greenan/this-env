# this-env
A quick and dirty python module to load local environment variables from the current directory automatically.

## Usage
Simply import and run `merge_envrc()`; update the `ENVRC_FMT` global variable as necessary, if you do not use the more-traditional `.envrc` filename.  Once the environment has been merged, you can use any of the environment variables like you usually would.

```python
import this_env
this_env.merge_envrc()

```
