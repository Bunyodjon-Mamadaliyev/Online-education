# Online Ta'lim Platformasi !


### Django asosida qurilgan kurslar, darslar, ro'yxatdan o'tish va foydalanuvchilar progressini boshqarish uchun onlayn ta'lim platformasi.

## Xususiyatlar

- [Foydalanuvchi autentifikatsiyasi va avtorizatsiyasi](#Foydalanuvchi autentifikatsiyasi va avtorizatsiyasi)
- [Kurslarni boshqarish tizimi](#Kurslarni boshqarish tizimi)
- [Dars modullari va kontenti](#Dars modullari va kontenti)
- [Ro'yxatdan o'tishni kuzatish](#Ro'yxatdan o'tishni kuzatish)
- [Progressni monitoring qilish](#Progressni monitoring qilish)
- [Sharh va baholash tizimi](#Sharh va baholash tizimi)
- [Media kontentni qo'llab-quvvatlash](#Media kontentni qo'llab-quvvatlash)

## Loyiha tuzilishi


```Online-education//                      # Loyiha asosiy papkasi
├── categories/           Kurs kategoriyalari
├── common/               Umumiy yordamchi dasturlar
├── config/               Loyiha konfiguratsiyasi
├── courses/              Kurslarni boshqarish
├── enrollments/          Talabalarni ro'yxatga olish tizimi
├── lessons/              Dars kontenti
├── media/                Yuklangan media fayllar
├── modules/              Kurs modullari
├── progresses/           Talaba progressini kuzatish
├── reviews/              Kurs sharhlari va baholari
├── users/                Foydalanuvchi hisoblari va autentifikatsiya
├── .gitignore            Git ignore qoidalari
├── db.sqlite3            Ma'lumotlar bazasi fayli (ishlab chiqish uchun)
├── manage.py             Django boshqaruv skripti
├── requirements.txt      Python bog'liqliklari
└── README.md             Loyiha hujjatlari
```

## O'rnatish
#### 1.Repozitoriyani klonlang:
```
git clone https://github.com/Bunyodjon-Mamadaliyev/Online-education.git
cd Online-education
```
#### 2.Virtual muhit yarating va faollashtiring:
```
python -m venv venv
# Linux: source venv/bin/activate
# Windowsda: venv\Scripts\activate
```
#### 3.Bog'liqliklarni o'rnating:
```
pip install -r requirements.txt
```
#### 4.Migratsiyalar yarating:
```
 python manage.py makemigrations
```
#### 5.Migratsiyalarni qo‘llang:
```
 python manage.py migrate  
```
#### 6.Ishga tushirish serverini ishga tushiring:
```
python manage.py runserver
```
## Foydalanuvchi rollari

- Admin: Barcha ma'lumotlarni boshqarish huquqiga ega.

- O'qituvchi: Kurs yaratish va talabalarga dars berish imkoniyati.

- Talaba: Kurslarga yozilish va darslarni o'rganish imkoniyati.

## API endpoints

- /api/courses/ – Kurslar ro'yxati

- /api/enrollments/ – Ro'yxatdan o'tish

- /api/progress/ – Talaba progressi

- /api/reviews/ – Sharh va baholar

## Qo‘shimcha sozlamalar

### Agar loyiha .env fayliga muhtoj bo‘lsa, quyidagilarni qo‘shing:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```