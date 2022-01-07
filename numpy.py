import numpy as np #numpy'ı import ettik

# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*15 vector

print(array.shape) # kaça kaçlık vektör olduğunu belirtir

a = array.reshape(3,5) # 3'e 5'lik bir matris yap

print("shape: ",a.shape)
print("dimension: ", a.ndim) # kaç boyutludur
print("data type: ",a.dtype.name) # değişken tipini gösterir
print("size: ",a.size) # arrayın boyutu nedir
print("type: ",type(a)) # tipi nedir

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]]) # 3'e 4'lük bir matrisi kendimiz oluşturduk

zeros = np.zeros((3,4)) # 3'e 4'lük bir 0 matrisi oluştur.
zeros[0,0] = 5 # 0'a 0'lık elemanı 5 olsun 
print(zeros)

np.ones((3,4)) # 3'e 4'lük 1'lik matris oluştur.
np.empty((2,3)) # 2'e 3'lük boş matris oluştur.

a = np.arange(10,50,5)
print(a) # 10 ile 50 arasında 5'er 5'er sayıları yazdır

a = np.linspace(10,50,20)
print(a) # 10 ile 50 arasında rastgele 20 sayı yazdır



# %% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b) # toplama
print(a-b) # çıkarma
print(a**2) # a'nın karesi
print(np.sin(a)) # a'nın sinüsünü al

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print(a*b) # her satırı diğer aynı satırla çarp

a.dot(b.T) # b'nin transpozu yani tersini aldır
print(np.exp(a))

a = np.random.random((5,5)) # 5'e 5'lik random matris oluştur
print(a.sum()) # toplamları
print(a.max()) # maksimum değer
print(a.min()) # minimum değer
print(a.sum(axis=0)) # satırları topla
print(a.sum(axis=1)) # sütunları topla
print(np.sqrt(a)) # a'nın kökünü al
print(np.square(a)) # a**2


# %% indexing and slicing
array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

print(array[0]) # 0. indexi yazdır
print(array[0:4]) # 0. indixden 4. ye kadar yazdır

reverse_array = array[::-1]
print(reverse_array) # arrayi ters çevirip -1. değeri al

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1]) # 1. satırın 1. sütununa erişmek isteniyor
print(array1[:,1]) # tüm 0 ve 1. sütunlara erişmek isteniyor
print(array1[1,1:4]) # 1. satırın 1 ve 3. satırlarını yazdır
print(array1[-1,:]) # en son satırı aldır
print(array1[:,-1]) # en son sütunu aldır

# %% shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = array.ravel() # matrisleri tek bir satırda birleştirir

array2 = a.reshape(3,3) # tekrar 3'e 3'lük matris oluşturur
arrayT = array2.T # Satırları sütun a sütunları satıra çevirir
print(arrayT.shape) # Kaça kaçlık matris olduğunu yazar

# %% stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
array3 = np.vstack((array1,array2)) # dikey birleştirme
array4 = np.hstack((array1,array2)) # yatay birleştirme

# %% Dönüşüm

liste = [1,2,3,4]   # list
array = np.array(liste) # listeyi arraya çevirdi
liste2 = list(array) # arrayi listeye çevir



