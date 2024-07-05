course = ['apple', 'cherry', 'bananaa', 'orange']

course_str = ' - '.join(course)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)

# for index, item in enumerate(course, start=1):
#     print(index, item)

# num = [1, 5, 6, 2, 4, 10]

# sorted_course = sorted(course)

# # course.sort(reverse=True)
# # num.sort(reverse=True)

# print(sum(num))
# # print(num)