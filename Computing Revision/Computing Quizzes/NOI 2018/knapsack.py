


weight_types = raw_input().split()

weight = int(weight_types[0])
types = int(weight_types[1])

vwn = []
for i in range(types):
      vwn.append(raw_input().split())
current = 0

while current > weight:
      if (weight//int(vwn[0][1])) >= int(vwn[0][2]):
            total_v = (weight//int(vwn[0][1]))*int(vwn[0][0])
      else:
            total_v = int(vwn[0][2])*int(vwn[0][0])
      total_w = (weight//int(vwn[0][1]))*int(vwn[0][1])
      print str(total_v)
