import datetime as DT

def pull_account_traffic(account_name):
    """Pulls the traffic score for a particular acocunt for each
            day the generate_dates() method generated

            Args:
                The account name to return the scores for x in xrange(1,10):
                    pass
            Returns:
                A list of scores, containing the score for each day"""
    traffic_report = []
    dates = generate_dates()
    check = "failed"
    for log_file in dates:
        with open('scores/account_score_{}'.format(log_file), "r") as log:
                for line in log:
                    line = line.strip()
                    split_line = line.split(',')
                    if split_line[0] == account_name:
                        traffic_report.append(split_line[5])
                        check = "passed"
                        break
                    else:
                        check = "failed"
                if check == "failed":
                    return "Account Not Found"
    return str(traffic_report)

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

