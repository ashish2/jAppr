#import itertools 

class MyMod:
	
	li = [8, 1, 3,  5, 2, 7, 4]
	li = [8, 1, 3,  5, 7, 2, 4]
	
	def __init__(self):
		pass
	
	def sum_to_10_bubble(self):
		""" Using Bubble sort to loop """
		li = self.li
		li_len = len(li)
		for i in range(0, li_len):
			num = i + 1
			for k in range(num, li_len):
				if li[i] + li[k] == 10:
					return i, k
		return None
	
	def sum_to_10_single(self):
		""" Using single loop & an extra dict to keep track of the elements """
		li = self.li
		di = dict()
		ret = None
		for i in li:
			num = 10 - i
			if di.get(num):
				ret = li.index(num), li.index(i)
				break
			else:
				di[i] = i
		return ret
		
	def sum_to_10_jump(self):
		""" Using dictionary & Jumping indexes """
		li = self.li
		di = dict()
		ret = None
		counter = 0
		i = 0
		li_len = len(li)
		while i < li_len:
			i_1 = i+1
			if i_1 < li_len:
				num = li[i] + li[i+1]
				sub_i = 10 - li[i]
				sub_i_1 = 10 - li[i+1]
			else:
				num = li[i]
				sub_i = 10 - li[i]
			
			if num == 10:
				ret = i, i+1
				break
			elif di.get(sub_i):
				# does number summing to 10 of i exists in di, then get li.index(num) & return both indexes
				ret = li.index(sub_i), i
				break
			elif di.get(sub_i_1):
				# does number summing to 10 of i+1 exists in di, then get li.index(num) & return both indexes
				ret = li.index(sub_i_1), i
				break
			else:
				# add both to dict
				di[li[i]] = li[i]
				di[li[i+1]] = li[i+1]
				# Jumping indexes here
				i = i + 2
		return ret

