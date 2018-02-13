# 0 CMTE_ID: identifies the flier, which for our purposes is the recipient of this contribution
# 7 NAME: Name of the contributor
# 10 ZIP_CODE: zip code of the contributor (we only want the first five digits/characters)
# 13 TRANSACTION_DT: date of the transaction
# 14 TRANSACTION_AMT: amount of the transaction
# 15 OTHER_ID: a field that denotes whether contribution came from a person or an entity

from datetime import datetime
import sys
import math

# print str(datetime.now()) 

file1 = open (sys.argv[1], "r")
file2 = open (sys.argv[2], "r")
file3 = open (sys.argv[3], "w")

factor = 0
for line in file2:
  factor = float(int(line)/100.0)
  break

hm_zip = {}
hm_receipent = {}
for line in file1:
  data = line.split("|")
  if len(data)>11:
    data[10] = data[10][:5]
  if len(data)>20 and len(data[15])<1 and len(data[10])>4 and len(data[0])>0 and len(data[7])>0 and len(data[13])==8 and data[13].isdigit() and len(data[14])>0 and int(data[14])>0: #Input checks
    if data[10] in hm_zip:
      if data[7] in hm_zip[data[10]]:
        curr_date = datetime.strptime(data[13], "%m%d%Y").date()
        if curr_date>=hm_zip[data[10]][data[7]]:
          key = data[0] +"-"+ data[10] +"-"+ data[13][4:]
          if key in hm_receipent:
            hm_receipent[key]["sum"] = hm_receipent[key]["sum"] + int(data[14])
          
            flag = False
            for i in range(0, len(hm_receipent[key]["amts"])):
              if int(data[14])<=hm_receipent[key]["amts"][i]:
                hm_receipent[key]["amts"].insert(i, int(data[14]))
                flag = True
                break
            if not flag:
              hm_receipent[key]["amts"].append(int(data[14]))
              
            percentile = int(math.ceil(factor*len(hm_receipent[key]["amts"]))) - 1

            file3.write(data[0] + "|" + data[10] + "|" + data[13][4:] + "|" + str(hm_receipent[key]["amts"][percentile]) + "|" + str(hm_receipent[key]["sum"]) + "|" + str(len(hm_receipent[key]["amts"])) +"\n")
            # file3.write(data[0] + "|" + data[10] + "|" + data[13][4:] + "|" + str(hm_receipent[key]["amts"][percentile]) + "|" + str(hm_receipent[key]["sum"]) + "|" + str(len(hm_receipent[key]["amts"])) +"     Donated by: "+data[7]+ " List: "+ str(hm_receipent[key]["amts"])+"\n")
          else:
            hm_receipent[key] = {}         
            hm_receipent[key]["sum"] = int(data[14])
            hm_receipent[key]["amts"] = []
            hm_receipent[key]["amts"].append(int(data[14]))
            file3.write(data[0] + "|" + data[10] + "|" + data[13][4:] + "|" + str(int(data[14])) + "|" + str(hm_receipent[key]["sum"]) + "|" + str(len(hm_receipent[key]["amts"]))+"\n") 
            # file3.write(data[0] + "|" + data[10] + "|" + data[13][4:] + "|" + str(int(data[14])) + "|" + str(hm_receipent[key]["sum"]) + "|" + str(len(hm_receipent[key]["amts"])) +"     Donated by: "+data[7]+ " List: "+ str(hm_receipent[key]["amts"])+"\n")
        else:
          pass
          # file3.write("Current date " + str(curr_date) + " was less than original date " + str(hm_zip[data[10]][data[7]])+"     Donated by: "+data[7]+"\n")
      else:
        hm_zip[data[10]][data[7]] = datetime.strptime(data[13], "%m%d%Y").date()
    else:
      hm_zip[data[10]] = {}
      hm_zip[data[10]][data[7]] = datetime.strptime(data[13], "%m%d%Y").date()

file1.close()       
file2.close()
file3.close()