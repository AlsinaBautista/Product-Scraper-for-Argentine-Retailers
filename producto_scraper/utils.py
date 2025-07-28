from urllib.parse import quote

def formatear_codigo(codigo):
    return str(codigo).strip().zfill(13)

def armar_url(base, codigo):
    return base.format(quote(codigo))
