import getopt
import sys

#getopt.getopt()函数使用方法

#输入参数含义：
# args指的是当前脚本接收的参数，它是一个列表，可以通过sys.argv获得
# shortopts  短参数　　 什么是短参数？　　比如：python test.py -h # 输出帮助信息
# longopts   长参数　　 什么是长参数？　　比如：python test.py --help # 输出帮助信息

#返回结果含义：
# opts 为分析出的格式信息。args 为不属于格式信息的剩余的命令行参数。

def main(argv):
    nodes = []
    vip = ''
    #other = ''
    opts, args = getopt.getopt(argv, "", ["nodes=","vip="])
    # print(args)
    for opt, arg in opts:
        if opt == "--nodes":
            nodes.append(arg)
        elif opt == "--vip":
            vip = arg
    if not len(vip):
        print("vip is empty")

    print(nodes)
    print(vip)


if __name__ == '__main__':
  main(sys.argv[1:])