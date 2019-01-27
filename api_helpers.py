import datetime as DT
import os
from os.path import isfile, join


def pull_account_traffic(account_name):
    """Pulls the traffic score for a particular acocunt for each
            day the generate_dates() method generated

            Args:
                The account name to return the scores for x in xrange(1,10):
                    pass
            Returns:
                A list of scores, containing the score for each day"""
    log_names = setup()
    traffic_report = ''    
    check = "failed"
    for log_file in log_names:
        log_to_check = 'scores/{}'.format(log_file)
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

def setup():
    """Runs through some initial setup steps: 
        Generates dates for current 30 days
        Formates dates into log file names
        Cleans up any files outside the 30 days

        Returns:
            log files to check in correct format"""
    dates = generate_dates()
    log_names = format_log_file(format_date(dates))
    cleanup_old_logs(log_names)
    return log_names

def check_for_log(log):
    """Ensure provided log file exists locally"""
    if not os.path.isfile(log):
        pull_log(log)

def pull_log(log):
    """Place holder method for now. Ensures we have the logs for the correct dates for the API to have available
        Should be replaced with a method to pull from the Google bucket if service account is created"""
    created_log = open(log, "w+")
    created_log.write('account_name,requests,rps,avg_response_time,errors_504,score\n')
    created_log.write('test,19745,32.908333333333331,3.8591649025069659,1,5\n')
    created_log.write('branden,17335,28.891666666666666,2.9916038650129804,386,10\n')
    created_log.close()

def cleanup_old_logs(dates):
    """Takes a date range and removes any logs that fall outside the range

        Args:
            dates: list of dates to check against"""

    current_log_files = [f for f in os.listdir('./scores') if isfile(join('./scores', f))]
    for log in current_log_files:
        if log not in dates:
            os.remove('./scores/{}'.format(log))

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

def format_log_file(date_list):
    """Use dates to create a list of names that match the account stat files format

        Args:
            date_list: list of dates to be converted to file names"""
    log_formatted_names = []
    for date in date_list:
        log_formatted_names.append('account_score_{}'.format(date))
    return log_formatted_names

