# -*- coding: utf-8 -*-
import random
def make(x):
    k=[]
    box=list(range(10))
    for i in range(x):
        k.append(box.pop(random.randint(0,9-i)))
    return k

def main():
    aite=[]
    flag_input=0
    flag_exit=0
    eat=0
    a=1
    b=1
    print("地方によって名前の違う数当てゲーム、数字の重複は無し")
    print("今回は数字だけ合ってたらbite、桁も合ってたらeat")
    print("0を入力すると強制終了")
    while flag_input==0:
        a=int(input("ゲームの桁数を入力してください。"))
        if a==0:
            print("GAME OVER")
            flag_input=1
            flag_exit=2
            break
        elif a > 10:
            print("１～１０までを入力してください。")
        else:
            aite=make(a)
            flag_input=1
            #print(aite)
    while flag_exit==0:
        while eat != a:
            jibun=[]
            c=0
            b=input(str(a)+"桁の自分の手")
            flag_exit=0
            if int(b)==0:
                print("GAME OVER")
                flag_exit=2
                break
            else:
                for x in str(b):
                    c += 1
                    if c > a:
                        print("MISS")
                        flag_exit=2
                        break
                    else:
                        jibun.append(int(x))
                if flag_exit==2 or len(jibun)<a:
                    continue
                atari=[]
                eat=0
                for i in range(a):
                    if jibun[i]==aite[i]:
                        eat += 1
                        atari.append(jibun[i])
                if eat==a:
                    flag_exit=1
                    break
                bite=0
                if atari != 0:
                    for r in atari:
                        jibun.remove(r)
                for k in range(len(jibun)):
                    if jibun[k] in aite:
                        bite += 1
                print(str(eat)+"eat\n"+str(bite)+"bite")
    if flag_exit==1:
        print(str(a)+"eat!!!PERFECT!!!")

if __name__=="__main__":
    main()