import random

# set random seed
random.seed(0)

# slice the data into euqally num parts
def generate_mushroom(data, num):
  
  # randomly shuffle the data
  random.shuffle(data)
  
  # Calculate the size of each part
  size = len(data) // num
  
  # return the 1/size, 2/size, ..., num/size parts
  for i in range(num):
    data_i =  data[0:(i+1)*size]
    
    # save the data to a new file
    with open('mushroom/data_{}_{}.dat'.format(i+1, num), 'w') as file:
      file.writelines(data_i)
  

    
if __name__ == '__main__':
  print('Generating mushroom ...')
  with open('mushroom.dat', 'r') as file:
    data = file.readlines()
  generate_mushroom(data, 10)
  print('Done.')