"""
Build environment.yml from requirements.txt
"""
requirements = []
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

preamble = """# Do not manually modify this file.
# It is automatically generated by
# `./build_tools/requirements_to_environment.py`
name: testenv
dependencies:
"""
with open("environment.yml", "w") as f:
    f.write(preamble)
    pip = False
    for req in requirements:
        if req.startswith("# For conda"):
            f.write("- pip:\n")
            pip = True
        elif not req.startswith("#"):
            if not pip:
                f.write("- {req}".format(req=req.replace("==", "=")))
            else:
                f.write("  - {req}".format(req=req))
