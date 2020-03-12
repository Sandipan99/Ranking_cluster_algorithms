import os
def convert(arg_1, arg2):
  fs = open(arg_1)  # the cluster file (input)
  temp = []
  mid = []
  for line in fs:
    mid.append(int(line.strip()))
  fs.close()
  comm_size = max(mid)
  #print comm_size
  comm = [[] for i in range(comm_size+1)]
  count = 1
  for li in mid:
    comm[int(li)].append(count)
    count += 1
  ft = open(arg2,"w")   # the line-wise file (output)
  for i in range(1,comm_size+1):
    if len(comm[i])>0:
      for li in comm[i]:
        ft.write(str(li)+"\t")
      ft.write("\n")
  ft.close()

path = 'Data-GT/Whitewine/'
convert('Data-GT/Whitewine/wwin_ground_truth','Data-GT/Whitewine/gt_linewise')