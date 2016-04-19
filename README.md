# RHPCOpattern -  Exploit Pattern Tool

## Banner
```
______ _   _ ______  _____ _____
| ___ \ | | || ___ \/  __ \  _  |
| |_/ / |_| || |_/ /| /  \/ | | |
|    /|  _  ||  __/ | |   | | | |
| |\ \| | | || |    | \__/\ \_/ /
\_| \_\_| |_/\_|     \____/\___/ pattern
            Exploit Pattern Tool
            Pattern generator and searcher like
            metasploit-framework/tools/pattern_create.rb

positional arguments:
  {generate,search}
  generate           generate pattern length
  search             search pattern position

optional arguments:
  -h, --help         show this help message and exit
```

## Example
### Pattern generation
```
rhpco@darkmoon:~/CODE/RHPCOpattern$ python RHPCOpattern.py generate 100
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
```
### Pattern position
```
rhpco@darkmoon:~/CODE/RHPCOpattern$ python RHPCOpattern.py search 0x41346141
Pattern 0x41346141 first occurrence at position 12 in pattern.
```
