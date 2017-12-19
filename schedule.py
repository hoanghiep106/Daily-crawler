from crontab import CronTab

my_cron = CronTab(user='hoanghiepnguyen')

file = open('last_tweet_id.txt', 'r')
last_tweet_id = file.readline()
file.close()

cd_to_directory = 'cd Project/tweetf0rm/'

job = my_cron.new(command=cd_to_directory + ' && sh client.sh -c config.json -cmd SEARCH -q="Gold Coast" -si=' + last_tweet_id
                          + ' && sh client.sh -c config.json -cmd BATCH_CRAWL_FRIENDS -d 1 -dt "ids" -j user_ids.json'
                          + ' && sh client.sh -c config.json -cmd BATCH_CRAWL_USER_TIMELINE -j user_ids.json')
job.minute.every(24)
my_cron.write()

# for job in my_cron:
#     print(job)

# my_cron.remove_all()
