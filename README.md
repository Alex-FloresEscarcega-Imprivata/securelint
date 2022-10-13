# Setup
`docker -t securelint:latest build .`

# Usage
* Add your java linting rule in rules/java-rules.txt
    * Make sure to add comment above query rule with leading semicolon e.g. `; Catch Intellij NotNull or Nullable annotations` 
* mount inputs files in a inputs directory

Note: if adding new query rule, you have to rebuild container.

`docker run -v `pwd`/inputs:/usr/src/securelint/inputs/ securelint:latest`


## Debugging query example
`docker run -it --entrypoint=/bin/bash securelint:latest`
`tree-sitter query 'rules/java-rules.txt' 'inputs/StorageConfigurationServiceTest.java'`

# Crafting a parser
Very quick tips to get you started

This is the interactive playground to get you going fast testing a query. Make sure to "ticket" query mode.
https://tree-sitter.github.io/tree-sitter/playground


Queries are like code-aware greps! But, it's not regex!

`((marker_annotation)@capture1 (#match? @capture1 "Nullable|NotNull"))`

marker_annotation is a token you would use to create a capture. You can write rules, like match regex string, on tokens you capture.
![Capturing tokens](static/capturing_tokens.png)


To learn more, visit https://tree-sitter.github.io/tree-sitter/creating-parsers