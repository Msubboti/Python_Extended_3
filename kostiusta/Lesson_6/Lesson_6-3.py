Russia={'xxs':42,'xs':44,'s':46,'m':48,'l':50,'xl':52,'xxl':54,'xxxl':56}
German={'xxs':36,'xs':38,'s':40,'m':42,'l':44,'xl':46,'xxl':48,'xxxl':50}
USA={'xxs':8,'xs':10,'s':12,'m':14,'l':16,'xl':18,'xxl':20,'xxxl':22}
France={'xxs':38,'xs':40,'s':42,'m':44,'l':46,'xl':48,'xxl':50,'xxxl':52}
GB={'xxs':24,'xs':26,'s':28,'m':30,'l':32,'xl':34,'xxl':36,'xxxl':38}

def size_convert (Russia,German,USA,France,GB):
    k=input('Enter european size from XXS to XXXL:').lower()
    return Russia.get(k),German.get(k),USA.get(k),France.get(k),GB.get(k)

r=(size_convert(Russia,German,USA,France,GB))
c=('Russia','German','USA','France','GB')
res=list(zip(r,c))
print(res)