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
* In the end of file you can initialize facts to true (by default all facts = false) after `=` operator. For example: `= fact1, fact2, fact3, fact4...` or simple form `=ABCDEF...` (if facts named only by one letter) -> fact A = true, fact B = true, fact C = true...
* After that you can ask a condition of the fact (true or false) by `?` operator. For example `? fact1, fact2, fact3...` or in simple form `?ABD` -> fact A - ?, fact B - ?...

### Logical operators

* `+` - logical operator `AND`
* `|` - logical operator `OR`
* `^` - logical operator `XOR`
* `!` - logical operator `NOT`
* `(` and `)` - standart mathematical brackets

### File example
File `examples/AND_OR1.ex`
```
S | E | V => V
V + !V => C

=S # initialize S to true
?VC # Results V - true, C - false
```

File `examples/XOR1.ex`
```
A ^ (X | Y) => V
N + (B ^ V) ^ !V => S

=XBN # initialize X, B and N to true
?SV # Results: S - false, V - true
```

## Other

After file is read and results is displayed, you can in console mode add rules and facts, initialize facts (by operator `=`) and display results (by operator `?`)

Besides that, in `console mode` you can:
* Reset all rules by next command
```
>> remove base
```
* Reset all facts initialized to true
```
>> remove facts
```
* Read other file (reading base and display results)
```
>> open path/to/file
```
