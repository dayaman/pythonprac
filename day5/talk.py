import os

def main():
    while True:
        try:
            say = input('Say:')
        except:
            print("Good Bye!")
            break
        
        os.system('say -v Otoya "{}"'.format(say))

if __name__=='__main__':
    main()
