def time_conversion(s):
    # Write your code here
    s_split = s.split(':')
    hh, am_pm = int(s_split[0]), s_split[2][-2:]
    if am_pm.lower() == 'am':
        hh = 0 if hh == 12 else hh
    elif am_pm.lower() == 'pm':
        hh = hh if hh == 12 else hh + 12

    hh = '{:02d}'.format(hh)
    military_time = f'{hh}:{s_split[1]}:{s_split[2][:2]}'
    return military_time


if __name__ == '__main__':
    times = [f'{x}:00:00{am_pm}' for am_pm in ['AM', 'PM'] for x in ['{:02d}'.format(h) for h in range(1, 13)]] + ['12:45:54PM']
    [print(time_conversion(x), x) for x in times]
