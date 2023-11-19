sample = "Hello world"


# n: là VỊ TRÍ kí tự bạn muốn xóa
n = int(input("vi tri ban muon xoa: "))

#Cách 1:
print(sample[0:n] + sample[n+1: len(sample)])

#Cách 2: viết tắt từ cách 1: 
# để trống bên trái dấu ":" nghĩa là số 0, 
# để trống bên phải dấu ":" là kí tự cuối mảng
print(sample[:n] + sample[n+1 :])
