import random
import sys
def make(x):
    #入力の数だけランダムに数字を取得する関数
    k=[]
    box=list(range(10))#ここから抽出
    for i in range(x):
        k.append(box.pop(random.randint(0,9-i)))
    return k

def make_aite():
    #相手の手を作る関数
    flag_input=0
    while flag_input==0:
        a=input("ゲームの桁数を入力してください。")
        if a=="":
            sys.exit("GAME OVER")
        elif int(a) <= 0:
            print("１～１０までを入力してください。")
        elif int(a) > 10:
            print("１～１０までを入力してください。")
        else:
            aite=make(int(a))
            flag_input=1
            #print(aite)
    return aite

def main():
    aite=[]
    flag_exit=0
    eat=0
    b=1
    print("地方によって名前の違う数当てゲーム、数字の重複は無し")
    print("今回は数字だけ合ってたらbite、桁も合ってたらeat")
    print("Enterを入力すると強制終了\n"+ " ")
    aite=make_aite()
    a=len(aite)
    while flag_exit==0:
        while eat != a:
            jibun=[]
            c=0
            b=input(str(a)+"桁の自分の手/空白で終了")
            flag_exit=0 #フラグのリセット
            if b=="":
                print(aite) #答えの表示
                print("GAME OVER")
                flag_exit=2
                break
            else:
                #正常入力か判定
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
                #以下正解判定及び表示
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
        print(str(a)+"eat!!!PERFECT!!!\n"+str(aite))

if __name__=="__main__":
    main()
