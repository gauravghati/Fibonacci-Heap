import requirements
import random as rand

# Instructions
# Some test cases for the FibHeap class can be found below.
#
# Note that the test cases here are just to give an idea of how we will test your submissions, so passing these tests does not mean that your code is correct.
# It is a good idea to try and create different test cases with different table sizes to fully test your implementation.

def is_delete_min_correct(roots):
	seen = set()
	for root in roots:
		if len(root.children) in seen:
			return False
		seen.add(len(root.children))
	return True

def fib_heap_tests():
	# fib = requirements.FibHeap()
	# uncomment the following line to test FibHeapLazy. The outputs should stay the same.
	fib = requirements.FibHeapLazy() 
	fib.insert(5)
	fib.insert(7)
	fib.insert(12)
	node = fib.insert(14)
	fib.insert(2)
	fib.print_fib()
	
	if [x.val for x in fib.get_roots()] != [5, 7, 12, 14, 2]:
		print("fib heap contents incorrect")
		return
	
	fib.find_min_lazy()
	fib.print_fib()

	fib.decrease_priority(node, 1)
	fib.print_fib()

	fib.delete_min_lazy()
	fib.print_fib()

	fib.find_min_lazy()
	fib.print_fib()

	node1 = fib.insert(34)
	fib.insert(14)
	fib.insert(94)
	node2 = fib.insert(55)
	fib.print_fib()
	fib.delete_min_lazy()
	fib.print_fib()
	fib.decrease_priority(node1, 9)
	fib.print_fib()
	fib.decrease_priority(node2, 10)
	fib.print_fib()
	print("MIN VALUE: ", fib.find_min_lazy().val)
	fib.print_fib()

	fib.delete_min_lazy()
	fib.print_fib()
	print("MIN VALUE: ", fib.find_min_lazy().val)
	fib.print_fib()

	print("all tests passed")

if __name__ == '__main__':
	fib_heap_tests()
