# UpdateIP
A python script for detecting external IP changes

# usage
First create a `mail-setting.conf` configuration file by copying the template

```
cp mail-setting.conf.template mail-setting.conf
```

edit the fields in `mail-setting.conf` file

run the script
```
python updateip.py
```

to run the script in background, add `&` to the end of the command
```
python updateip.py &
```
