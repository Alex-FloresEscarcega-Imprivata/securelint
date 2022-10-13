# Setup
docker -t securelint:latest build .

# Usage
* Add your java linting rule in rules/java-rules.txt
    * Make sure to add comment above query rule with leading semicolon e.g. `; Catch Intellij NotNull or Nullable annotations` 
* mount inputs files in a inputs directory

Note: if adding new query rule, you have to rebuild container.

docker run -v `pwd`/inputs:/usr/src/securelint/inputs/ securelint:latest


## Debugging query example
docker run -it --entrypoint=/bin/bash securelint:latest
tree-sitter query 'rules/java-rules.txt' 'inputs/StorageConfigurationServiceTest.java'