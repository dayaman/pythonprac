import random

def onigiri():
    
    try:
        with open('ongrct.txt', 'r') as fp: 
            on = int(fp.read())
            #fp.close()
    except:
        on = 0
        
    on += 1
    if on % 10 == 0:
        print('''　　　　　　　　　おにぎりワッショイ！！
　　　　　＼＼　 おにぎりワッショイ！！　／／
　+　　　+　＼＼　おにぎりワッショイ！！／+
　　　　　　　　　　　　　　　　　　　　　　　　　　　　+
.　　　+　　 ／■＼　 　／■＼　   ／■＼　　+
　　　　　　（　´∀｀∩（´∀｀∩） ( ´ー｀）
　+　　  （(（つ　ノ （つ　丿 （つ　　つ　)）　　+
      　　　 ヽ（ ノ （ ヽノ　  ） ） ）
　　　　   　（＿)し'  し(＿）（＿）＿）''')
    else:
        print(on,'回目のおにぎりです。')
    with open('ongrct.txt', 'w') as fw:
        fw.write(str(on))
        #fw.close()

def main():

    num = random.randint(1, 5)

    if num  == 5:
        print('おにぎり')
        onigiri()
    else :
        print('はずれ')

if __name__ == '__main__':
    main()
