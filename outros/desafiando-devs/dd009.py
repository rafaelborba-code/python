def hor_sec(time: str):
    div = {'hora': time[0:2],
        'minuto': time[3:5],
        'segundo': time[6:]}
    secs = int(div['segundo'])
    h_s = (div['hora'] * 60 + div['minuto']) * 60
    secs += h_s
    return secs


print(hor_sec())