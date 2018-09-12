# Expert_system

General-purpose Expert system for various conclusions
Present Expert system is based on `backward chaining` algorithm

## Run

```
> ./expert.py you_knowledge_base_file
```
OR
```
> python3 expert.py you_knowledge_base_file
```

## Format of file

* At first, your file should have rules separated by new line
* Every rule should have conlusion by `=>` - implication operator or `<=>` - logical equality operator. For example: `A => B # A implies B`
* Comment starting by `#` symbol
