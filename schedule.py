from crontab import CronTab

my_cron = CronTab(user='hoanghiepnguyen')

file = open('last_tweet_id.txt', 'r')
last_tweet_id = file.readline()
file.close()

cd_to_directory = 'cd Project/tweetf0rm/'
# crawl_proxies = 'python crawl_proxies.py'
run_script = 'sh client.sh -c config.json -cmd SEARCH -q="Gold Coast" -si=' + last_tweet_id
command = [cd_to_directory, run_script]

job = my_cron.new(command=' && '.join(command))
job.hour.every(24)
my_cron.write()

# for job in my_cron:
#     print(job)

# my_cron.remove_all()
