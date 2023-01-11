def get_time_str(total_secends: int) -> str:
    '''依照秒數 回傳時間'''
    msg = ''
    seconds = total_secends % 60
    minutes = (total_secends // 60) % 60
    hours = ((total_secends // 60) // 60) % 24
    days = ((total_secends // 60) // 60) // 24
    if days != 0:
        msg += f"{str(days).center(3)}天"
    if hours != 0:
        msg += f"{str(hours).center(2)}時"
    if minutes != 0:
        msg += f"{str(minutes).center(2)}分"
    if seconds != 0:
        msg += f"{str(seconds).center(2)}秒"
    return msg
