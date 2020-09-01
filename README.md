My version of [hypermodern-python](https://github.com/cjolowicz/hypermodern-python) for playing around. There is [an excellent companion blog](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) by Claudio Jolowicz.

## Tips
Before using poetry commands you need to source it:

source ~/.poetry/env

When setting up the package in src layout, do not do this manually, but simply type

poetry new --src <package-name>

Replace <package-name> with the name of your package/repository.

This is probably a new poetry feature described here: https://python-poetry.org/docs/cli/#new
