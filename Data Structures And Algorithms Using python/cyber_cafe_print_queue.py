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


'''from collections import deque

q = deque()

def add_job(customer,page):
    q.append((customer,page))
    print("Job added:",customer,page)

def serve_next():
    print("Served:",q.popleft())

def show_queue():
    print("Waiting jobs:",q)

def round_robin(q):
    print("Service Orders:")
    while q:
        i , j = q.popleft()

        if j <= 10:
            print(f"{i} -> {j} pages")
            
        elif j > 10:
            print(f"{i} -> 10 pages")
            q.append((i,j-10))
        
add_job("Asha",4)
add_job("Bhavin",25)
add_job("Chirag",12)
add_job("Dhara",8)
show_queue()
round_robin(q)'''


# 4.Finish 'cyber_cafe_print_queue.py' with a menu (add job, serve next, show queue, show waiting times,
#  run round robin, exit) that allows at most 5 waiting jobs and prints 'Queue full' for a sixth.
#  Test by adding 6 jobs, serving 2 and adding 1 more. Paste the output as a comment at the end
#  and push the folder to 'dsa_python_portfolio'.

from collections import deque



q = deque()


def add_job():
    customer = input("Enter customer name:")
    page = int(input("Enter a page number:"))
    q.append((customer,page))
    print("Job added:",customer,page)


def serve_next():
    if q:
        print("Served:",q.popleft())
    else:
        print("No jobs waiting")

def show_queue():
    print("Waiting jobs:",q)

def waiting_times(queue):
    total = 0
    for i,j in queue:
        print(f"{i} must wait {total} seconds ")
        total += j*2

def round_robin(q):
    print("Service Orders:")
    while q:
        i , j = q.popleft()

        if j <= 10:
            print(f"{i} -> {j} pages")
        
        elif j > 10:
            print(f"{i} -> 10 pages")
            q.append((i,j-10))

stop = False

while stop == False:
    print("----------The Menu----------")
    print("1. Add Job")
    print("2. Serve next")
    print("3. Show queue")
    print("4. Show waiting times")
    print("5. Run round robin")
    print("6. exit")
    method = int(input("Choose method (1/2/3/4/5/6): "))

    if method == 1:
        if len(q) >= 5:
            print("Queue full")
        else:
            add_job()

    elif method == 2:
        serve_next()
    elif method == 3:
        show_queue()
    elif method == 4:
        waiting_times(q)
    elif method == 5:
        round_robin(q)
    elif method == 6:
        print("----Exited---")
        stop = True
        
    else:
        print("---Incorrect Method-----")


    

        

