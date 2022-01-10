from datetime import datetime


def timestamp_to_datenum(timestamp_string):

    parsed_date = datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%SZ')

    fraction_days = (parsed_date.second + parsed_date.minute * 60 + parsed_date.hour * 60 * 60) / (24 * 60 * 60)

    datenum = parsed_date.date().toordinal() + 366 + fraction_days

    return datenum


print(timestamp_to_datenum('2022-12-23T23:47:23Z'))
# 738878.991238426
