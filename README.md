# RKBD

Remote keyboard in python

## Usage

Clone the repository on to both machines and install the requirements.

```bash
pip install -r requirements.txt
```

Then run `server.py` on the target machine and `client.py` from the source machine.

```bash
python server.py
```

You will need to provide the ip address and port of the target machine which is `5054` and the keystroke file.
```bash
python client.py --ip=<target_ip> --port=<target_port>  --file=<file_name>
```

## Keystroke file

The keystroke file should look like this:

```bash
win+r
notepad
enter
```

The above example will open notepad on a Windows machine using the run window.

## Licence

This project is licenced under the GNU General Public Licence v3.0 - see the [LICENCE](LICENCE) file for details.
