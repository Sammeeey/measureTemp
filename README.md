# measureTemp
- execute Python script as cronjob on Ubuntu

**every 30th minute: go to directory, execute `temp.py`& log output of `temp.py` in `temp.log`**:

`*/30 * * * * cd /home/pi/Dokumente/temp && python3 temp.py >> /home/pi/Dokumente/temp/temp.log 2>&1`

## Resources
- [script template](https://stackoverflow.com/a/57274737)
    - removed log part from script because cronjob logs automatically
- [setup cronjobs](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804)
- [setup cron for python script](https://stackoverflow.com/a/8727991)
- [write crontab command for python script](https://stackoverflow.com/a/34735675)

## Crontab Commands
`crontab -e` (edit)
`crontab -l` (list)
