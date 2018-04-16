# UpdateIP
A python script for detecting external IP changes

# usage
First create a `mail-setting.conf` configuration file by copying the template

```
cp mail-setting.conf.template mail-setting.conf
```

Edit the fields in `mail-setting.conf` file

Run the script
```
python updateip.py
```

To run the script in background, add `&` to the end of the command
```
python updateip.py &
```
If you want to run `updateip.py` directly as a script, eg.
```
./updateip.py
```
you need to change the first line in `updateip.py` to point to your python interpreter
