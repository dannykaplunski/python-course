avengers_file = open('file.txt', 'r')
print(avengers_file.read())
print(avengers_file.read())

avengers_file.seek(5)
print(avengers_file.read())

avengers_file.seek(0)
new_avengers = open('new_avengers.txt', 'w')
new_avengers.write(avengers_file.read())
new_avengers.close()
new_avengers = open(new_avengers.name, 'r+')
print(new_avengers.read())

new_avengers.seek(0)
new_avengers.write("Hulk")
new_avengers.seek(0)
print(new_avengers.read())
new_avengers.close()

new_avengers = open(new_avengers.name, 'a+')
new_avengers.write("\nBlack Widow")
new_avengers.seek(0)
print(new_avengers.read())
new_avengers.close()
