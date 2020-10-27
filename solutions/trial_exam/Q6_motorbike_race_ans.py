'''
a program to sort the results of a motorbike race
'''

motorbike_make=['Ducati Monster', 'Kawasaki Z900', 'Honda Goldwing', \
               'Yamaha XSZ900', 'Suzuki Hayabusa', 'Yamaha MT09 Tracer', \
               'Kawasaki Ninja', 'Ducati Streetfighter', 'Suzuki GSX 1000', \
               'Moto Guzzi', 'Honda Gladiator', 'Ducati Diabolo']

m_top_speed=[286, 270, 175, 280, 205, 189, 245, 297, 252, 195, 199, 330]


m_rider=['John Sattler', 'Ziqi ZHANG', ' Shaosen ZHUANG', \
         'Salim Zadah', 'Chang Yuan', ' Zongjie Meng', \
         ' Jinyu Chen', ' Yue Fan', ' Meng HOANG', \
         ' Yijun Cai', ' Wentao Yeung', 'Clive Churchill']


# sort the list
for i in range(len(motorbike_make)-1):
    for j in range(i+1,len(motorbike_make)):
        if m_top_speed[j]>m_top_speed[i]:
            temp=motorbike_make[i]
            motorbike_make[i]=motorbike_make[j]
            motorbike_make[j]=temp
            temp=m_top_speed[i]
            m_top_speed[i]=m_top_speed[j]
            m_top_speed[j]=temp
            temp=m_rider[i]
            m_rider[i]=m_rider[j]
            m_rider[j]=temp
    

# print the list
print('Motorbike Make        Top Speed    Rider')
for i in range(len(motorbike_make)):
    string=motorbike_make[i]
    while len(string)<25: string+=' '
    string+=str(m_top_speed[i])+'       '
    string+=m_rider[i]
    print(string) 
