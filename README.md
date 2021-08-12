# steamy-jungle
Convert list of steam URL links to steamid64

# setup - windows

1. Go to https://github.com/smiley/steamapi and install as instructed in the **"How do I use this?"** section.
1. Go to https://steamcommunity.com/dev/apikey and make a Steam dev API key.
2. Create a file called ".env" in this folder .
3. On the first line of that folder put `export STEAM_DEV_API_KEY=[YOUR API KEY HERE]` and save it.
3. Optionally set a time between steam calls (do not go below 1 second) by adding a line with `export SLEEP_BETWEEN_STEAM_CALLS=1.5` (or whatever time you want) in that file.
3. Make sure the `.env` file has a new line at the end of it.
3. Open command prompt (or however you use pip) and do a `pip install python-dotenv`.
4. Run the program with `python .\main.py` in a powershell in this folder.
