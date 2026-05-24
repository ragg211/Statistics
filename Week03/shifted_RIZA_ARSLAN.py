def shifted(data):
    n = len(data)
    if n == 0:
        return 0.0
        
    ortalama = sum(data) / n
    sirali = sorted(data)
    medyan = (sirali[n // 2] + sirali[(n - 1) // 2]) / 2
    
    if ortalama == 0:
        return 0.0
        
    yuzdelik_fark = (abs(ortalama - medyan) / abs(ortalama)) * 100
    return yuzdelik_fark