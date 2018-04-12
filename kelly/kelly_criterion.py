# -*- coding: utf-8 -*-
import time
import random
import sys
import getopt

INPUT_ERROR = 0
INVALID_ARGS = 1

'''
f=p/rl - ((1-p)/rw)
f为最优比例，p为赢的概率。rw为赢时的净收益率，rl是输时的净损失率
'''
def kelly_calc(p, rl, rw):
	f = (p/rl)-((1-p)/rw)
	return f

def input_calc(total, f):
	return total*f

def profit_calc(input, rl, rw, result):
	profit = 0
	if result == -1:
		profit = input*rl*result
	elif result == 1:
		profit = input*rw*result
	else:
		print("error:result must be 1 or -1")
	return profit

# def random_pick(seq,prob):
# 	'''按概率产生整数，seq为整数列表，prob为对应的概率列表'''
# 	x = random.uniform(0, 1)#首先随机生成一个0，1之间的随机数
# 	cumulative_prob = 0.0
# 	for item, item_prob in zip(seq, prob):#seq代表待输入的字符串，prob代表各自字符串对应的概率
# 		cumulative_prob += item_prob#只有当累加的概率比刚才随机生成的随机数大时候，才跳出，并输出此时对应的字符串
# 		if x < cumulative_prob:
# 			break
# 	return item


def usage():
	print("use:python kelly_criterion.py -t total -p p -l rl -w rw")


def main():
	if(("-t" not in sys.argv) | ("-p" not in sys.argv) | ("-l" not in sys.argv) | ("-w" not in sys.argv)):
		usage()
		sys.exit(INPUT_ERROR)
	opts,args = getopt.getopt(sys.argv[1:], "t:p:l:w:", ["total=","probability=","lost=","win="])
	for op,value in opts:
		if op in ("-t", "--total"):
			total = int(value)
		elif op in ("-p", "--probability"):
			p = float(value)
		elif op in ("-l", "--lost"):
			rl = float(value)
		elif op in ("-w", "--win"):
			rw = float(value)
		else:
			print "invalid arguments"
			sys.exit(INVALID_ARGS)
	# p = 0.5
	# rl = 1#lost rate
	# rw = 2#win rate
	# int_list = [1, -1]
	# prob_list = [p, 1-p]
	total = 100
	f = kelly_calc(p, rl, rw)
	if not 0.0 <= f <= 1.0:
		print(f)
		print("f is not reasonable")
	put = input_calc(total, f)
	# num = random_pick(int_list,prob_list)
	# profit = profit_calc(put, rl, rw, num)
	# total = total + profit
	print(put)
	# print(profit)
	# print(total)

if __name__ == '__main__':
	main()
