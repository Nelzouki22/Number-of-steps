# قراءة عدد العناصر في المصفوفتين
n = int(input())

# قراءة المصفوفة a
a = list(map(int, input().split()))

# قراءة المصفوفة b
b = list(map(int, input().split()))

# البحث عن أصغر قيمة في a
min_a = min(a)

# حساب عدد الخطوات المطلوبة
steps = 0
possible = True

for i in range(n):
    # تحقق من إمكانية تحويل a[i] إلى min_a
    if (a[i] - min_a) % b[i] == 0:
        steps += (a[i] - min_a) // b[i]
    else:
        possible = False
        break

# إذا كان من الممكن تحويل جميع العناصر، اطبع عدد الخطوات، وإلا اطبع -1
if possible:
    print(steps)
else:
    print(-1)

