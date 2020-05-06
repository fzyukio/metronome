# Metronome

Create a pulse train and store in a WAV file.
 The pulse is 440Hz

## Install python
- Recommend python 3.7. DO NOT USE python 3.8!!! 
- If on Windows, don't forget to check the option "Add python to the PATH environment variable"
- On Linux/Mac, you know what to do
- After installation, check that it can be called by opening a terminal and type `python --version`.
If you see `Python 3.x.x` you're good to go


## Setup the script:
- Using git `git checkout https://github.com/fzyukio/metronome.git` or download ZIP file at `https://github.com/fzyukio/metronome/archive/master.zip`
- If you download the ZIP file, extract it. Let's say you extract it to `C:\Koe\metronome\`
- Open a terminal and `cd "C:\Koe\metronome" `
- Run `pip install -r requirements.txt`


## Run the script
- Open a terminal and `cd "C:\Koe\metronome" `
- To generate a 1-second long test.wav file with pulses every 100 ms: 
```bash
python main.py --file-name=test.wav --gap-length=100 --duration=1000
```
