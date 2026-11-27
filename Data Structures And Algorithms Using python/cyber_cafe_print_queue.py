# 1.Write 'cyber_cafe_print_queue.py' in a folder named 'cyber_cafe_print_queue' that uses 
# `collections.deque` to hold print jobs as (customer, pages) tuples, with functions `add_job`
#  (`append`), `serve_next` (`popleft`) and `show_queue`. Add 6 jobs, serve 3 and print the waiting
#  list after each step; print 'No jobs waiting' when the queue is empty.
#  Constraint: Do not use `list.pop(0)`.


'''from collections import deque

q = deque()

def add_job(customer,page):
    q.append((customer,page))
    print("Job added:",customer,page)

def serve_next():
    print("Served:",q.popleft())

def show_queue():
    print("Waiting jobs:",q)

add_job("abc",6)
add_job("adc",4)
add_job("sxd",5)
add_job("qwe",3)
show_queue()
serve_next()
show_queue()'''


# 2.Add `waiting_times(queue)` that, assuming each page takes 2 seconds, prints how many seconds
#  each waiting customer must wait before their job starts, without removing any job from the queue.
#  Test with jobs of 4, 10, 3 and 6 pages (waits of 0, 8, 28 and 34 seconds).



'''from collections import deque

q = deque()

def add_job(customer,page):
    q.append((customer,page))
    print("Job added:",customer,page)

def serve_next():
    print("Served:",q.popleft())

def show_queue():
    print("Waiting jobs:",q)

def waiting_times(queue):
    total = 0
    for i,j in queue:
        print(f"{i} must wait {total} seconds ")
        total += j*2
    
    

add_job("abc",6)
add_job("adc",4)
add_job("sxd",5)
add_job("qwe",3)
show_queue()
serve_next()
show_queue()
waiting_times(q)'''

# 3.Add `round_robin(queue)` where a job with more than 10 pages prints only 10 pages and
#  then goes to the back of the queue with its remaining pages. Print the order of service. 
# Test with Asha 4, Bhavin 25, Chirag 12 and Dhara 8 pages. Hint: `popleft()` the job, 
# then `append()` the remaining part.


from collections import deque

q = deque()

def add_job(customer,page):
    q.append((customer,page))
    print("Job added:",customer,page)

def serve_next():
    print("Served:",q.popleft())

def show_queue():
    print("Waiting jobs:",q)

add_job("Asha",4)
add_job("Bhavin",25)
add_job("Chirag",12)
add_job("Dhara",8)
show_queue()

