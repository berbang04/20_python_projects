import requests,schedule,time


def send_message():
    reesp=requests.post("https://textbelt.com/text",{
        'phone':'+905445983963',
        'message':'good morning babe',
        'key':'textbelt',
    })
    print(reesp.json())
# schedule.every().day.at("08:30").do(send_message)
schedule.every(10).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
