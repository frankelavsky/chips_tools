import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"


#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file

dataTest = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)

#print the resulting data
print(dataTest)
print(dataTest.__str__())
# print(type(dataTest))
# print(dataTest.levels[0])
print(type(dataTest.levels[0]))
file2write=open("data/pfgd_test.txt",'w')
file2write.write(dataTest.__str__())
file2write.close()