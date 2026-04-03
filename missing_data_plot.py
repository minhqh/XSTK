import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Đọc và ghi data 
data = pd.read_csv('Intel_CPUs.csv')

#Đếm số giá trị bị null ở từng cột
missing_count = data.isnull().sum()

#Chỉ lấy cột lớn hơn 0 và sắp xếp giảm dần 
missing_count = missing_count[missing_count > 0].sort_values(ascending=False)

#Vẽ đồ thị
plt.figure(figsize=(12, 8))
sns.barplot(x=missing_count.values, y=missing_count.index, palette="viridis")

# Thêm tiêu đề và nhãn
plt.title("Số lượng giá trị thiếu (Missing Values) theo từng đặc trưng", fontsize=15)
plt.xlabel("Số lượng giá trị thiếu", fontsize=12)
plt.ylabel("Tên đặc trưng (Feature)", fontsize=12)

# Hiển thị số liệu cụ thể ở đầu mỗi thanh biểu đồ
for i, v in enumerate(missing_count.values):
    plt.text(v + 3, i + .25, str(v), color='black', fontweight='bold')


plt.tight_layout()
plt.show()