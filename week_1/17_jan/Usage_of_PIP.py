# what is pip: pip is package manager for python packages

# command to check pip Install or not: // pip --version

# How to download packages: pip install package_name

# remove package : pip unistall package_name

# check the list of package : pip list


# Here i downloaded the camelcase package using pip , let's use it

import camelcase

c = camelcase.CamelCase()

txt = "helloworld"

print(c.hump(txt))
