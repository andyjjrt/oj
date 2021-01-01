#oj
###This cli is an upgrade version of [oj-cli](https://github.com/josix/oj-cli "oj-cli")
#####Python2.7 &rarr; Python3 up
#####FUll support for Git-Bash, Powershell, and Windows cmd
###Installation
1. Install required module **requests**
`pip3 install requests2`
2. Download source code by **git**
`git clone gh repo clone andyjjrt/oj ~`
3. Add following command in your `.bashrc` or `.profile`
   - Git bash
   `alias oj="winpty python3 ~/oj/oj.py"`
   - Linux (Unix)
   `alias oj="python3 ~/oj/oj.py`

Note : This cli tool can also run in **Powershell** and **Windows cmd**
###Usage
**oj login** : Login to your oj account.
**oj update** : Update your assignmapping.
**oj get [assign_no]** : Get your hw sample file.
**oj submit [assign_no] [code_file]** : Submit your hw code and get response.

###In the furture
1. Color prompt (Removed now because of unknown reason.)
2. rank
3. stat
4. dl
5. problem features