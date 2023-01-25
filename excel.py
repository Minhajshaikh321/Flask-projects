import xlsxwriter

data = [
    {
        'name': 'Suraiya',
        'phone': '883832',
        'email':'suraiya12@gmail.com'
    },
    {
        'name': 'Minhaj',
        'phone': '2874237',
        'email':'minhaj12@gmail.com'

    },
    {
        'name': 'Zikra',
        'phone': '2322525',
        'email':'zikra12@gmail.com'

    },
    {
        'name': 'Iram',
        'phone': '1234567',
        'email':'iram12@gmail.com'

    }            
]

#instance of workobook file
workbook = xlsxwriter.Workbook("AllAboutPythonExcel.xlsx")
worksheet = workbook.add_worksheet("firstsheet")

worksheet.write(0,0,'#')
worksheet.write(0,1,'Name')
worksheet.write(0,2,'Phone')
worksheet.write(0,3,'Email')


for index, entry in enumerate(data):
    worksheet.write(index+1,0,str(index))
    worksheet.write(index+1,1,entry["name"])
    worksheet.write(index+1,2,entry["phone"])
    worksheet.write(index+1,3,entry["email"])
   
workbook.close()   