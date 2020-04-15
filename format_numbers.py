def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def formatação(m):
    while True:
        try:
            v = ppv(str(input(m)))
            return v
        except ValueError:
            print('\nVocê digitou um ou mais caracteres inválidos. '
                  'Digite apenas números, separando as casas decimais com ponto ou vírgula!\n')
            continue


def msv(k):
    mf = '{:.2f}'.format(k)
    dec = mf[-2:]
    intf = '{:,}'.format(int(k))
    antes = str(intf).replace(',', '.')
    fn = '{}{}{}'.format(antes, ',', dec)
    return fn
