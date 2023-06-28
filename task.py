Tasks=[]

          
def input_task():

     f=input('enter  name of task for storage:')
     Tasks.append(f)
     print('Task added to Memory')
          
def view_task():
     if len(Tasks) == 0:
           print('No tasks')
     else:
          print('Tasks are:')
          for i,f in enumerate(Tasks,start=1):
               print(f'{i}.{f}')

def delete_task():
     view_task()
     index=int(input('Enter the index of task to be removed:'))-1
     if index <= 0 and index < len(Tasks):
          removed=Tasks.pop(index)
          print(f'the task {removed} has been  sucessfully removed')

def clear_task():
     while True:
          h=input('do you want to clear all the task now? (y/n):')
          if h == 'y':
               Tasks.clear()
          elif h == 'n':
              
               print('clear operation has been jinxed')
          break

def reverse_tasks(word):

     index=input('the task you want to reverse:')-1
     for index,word in enumerate(word,start=1):
          reverse=''
          reverse+=word[-1:]
          print(f'the reverse of task no{index} is :')
          return reverse
               
def show_tasks():
     print('Todo Manager')
     print('1.Input Tasks')
     print('2.View Tasks')
     print('3.Delete Tasks')
     print('4.Clear Tasks')
     print('5.Goodbye.')
             
def main():            
     while True:
          show_tasks()
          choice=input('enter the task operation to be performed [1-5]:')
          if choice == '1':
               input_task()
               
          elif choice == '2':
               view_task()
               
          elif choice == '3':
             delete_task()
          elif choice == '4':
               clear_task()
          elif choice == '5':
               print('Nicee using my software.')
               break
          else:
               print('Invalid choice')


if __name__=="__main__":
     main()
               
          

     
        


