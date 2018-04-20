# UpdateIP
A python script for detecting external IP changes

## Usage
1. First create a `mail-setting.conf` configuration file by copying the template

    ```
    cp mail-setting.conf.template mail-setting.conf
    ```

2. Edit the fields in `mail-setting.conf` file
```
  1 [mail-setting]
  2 smtp_server = smtp.aliyun.com ### smtp server address used to send mail ###
  3 port = 465                    ### smtp port used to send mail ###  
  4 username = abcd@aliyun.com    ### username used to connect to smtp server ###
  5 password = 12345678!          ### password used to connect to smtp server ###  
  6 recipient = 1234@aliyun.com   ### mail address to receive notification ###  
```
3. Run the script
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
