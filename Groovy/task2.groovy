Integer target_num = 44535
summ = 0

do {
summ = summ + target_num % 10
target_num = target_num / 10
} while (target_num >=10)

println(summ + target_num)