# explorer-agent

This program calculates the total score of and agent exploring a map (maze) with monsters, obstacles and treasures

## Getting Started



These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites



What things you need to install the software and how to install them.


* Python.
  https://www.python.org/downloads/	

* Git.
  https://git-scm.com/downloads



### Installing



Clone this repository



```bash
git clone https://github.com/Vixan/explorer-agent
```



Open any CLI like CMD, Bash or Powershell and navigate to the folder of the program



```bash
cd explorer-agent/maze-solver

```


Next, just run the program using the Python interpretor

```py
py app.py
```

### Usage

The default maze is defined in /maze-solver/defs.py
 

### Example

```bash
~/explorer-agent/maze-solver/
$ py app.py
_ _ _ _ _ _ _ _ _ _ _ _
_ # _ _ # _ _ M _ _ T _
_ # T _ # _ _ _ _ # _ _
_ # _ _ # _ # # _ # _ _
_ # # # # _ _ _ _ # _ _
_ # _ _ _ _ _ _ _ # _ M
_ # _ _ _ _ _ _ _ # _ _
_ # _ _ _ _ _ _ _ _ _ _
_ # _ _ _ _ _ # # # # _
_ # _ _ _ _ _ _ _ _ _ _
_ _ _ # # # # _ T _ _ _
_ _ _ _ _ M _ _ _ _ _ _



_ * * * * * * * * * _ _
_ # * * # * * * * * * _
_ # * * # * * * * # * *
_ # _ * # * # # * # * *
_ # # # # * * * * # * *
_ # * * * * * * * # * *
* # * * * * * * * # * *
* # * * * * * * * * * *
* # * * * * * # # # # *
* # * * * * * * * * * *
* * * # # # # * * * * *
* * * * * * * * * * * *

Final score -800
```

## Authors

* **Duca Vitalie-Alexandru** - *Development* - [Vixan](https://github.com/Vixan)