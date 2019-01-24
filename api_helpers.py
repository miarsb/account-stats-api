import datetime as DT
import os

def pull_account_traffic(account_name):
    """Pulls the traffic score for a particular acocunt for each
            day the generate_dates() method generated

            Args:
                The account name to return the scores for x in xrange(1,10):
                    pass
            Returns:
                A list of scores, containing the score for each day"""
    traffic_report = ''
    dates = generate_dates()
    check = "failed"
    for log_file in dates:
        log_to_check = 'scores/account_score_{}'.format(log_file)
        check_for_log(log_to_check)
        with open(log_to_check, "r") as log:
                for line in log:
                    line = line.strip()
                    split_line = line.split(',')
                    if split_line[0] == account_name:
                        traffic_report += split_line[5]+','
                        check = "passed"
                        break
                    else:
                        check = "failed"
                if check == "failed":
                    return "Account Not Found"
    return str(traffic_report)[:-1]

def check_for_log(log):
    if not os.path.isfile(log):
        pull_log(log)

def pull_log(log):
    created_log = open(log, "w+")
    created_log.write('account_name,requests,rps,avg_response_time,errors_504,score\n')
    created_log.write('test,19745,32.908333333333331,3.8591649025069659,1,5\n')
    created_log.write('branden,17335,28.891666666666666,2.9916038650129804,386,10\n')
    created_log.close()

def generate_dates():
    """Generates the dates for the last 30 days

            Returns:
                A list of dates within the last 30 days, 
                starting from yesterday"""
    last_week = []
    today = DT.date.today()

    for day in range(1,31):
        new_day = today - DT.timedelta(days=day)
        date_to_add = str(new_day.year)+format_date(str(new_day.month))+format_date(str(new_day.day))
        last_week.append(date_to_add)
    return last_week

def format_date(date):
    """Converts dates to the proper format to match logs

            Args:
                Takes in a date from datetime

            Returns:
                A date in the proper format to match the logs"""
    if len(date) == 1:
        return "0{}".format(date)
    else:
        return date

