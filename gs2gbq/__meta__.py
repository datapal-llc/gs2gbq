# `name` is the name of the package as used for `pip install package`
name = "gsgbq"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.dev0"
author = "Giang Bui"
author_email = ""
description = ""  # One-liner
url = ""  # your project homepage
license = "Unlicense"  # See https://choosealicense.com
