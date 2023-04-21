import bs4
import pandas
import beautifulsoup4 


Scraped_Data=[]

Stars_Data=[]

 


def scrape():

    bright_star_table=  beautifulsoup4.find("table",attrs={"class","wikitable"})

    table_body=bright_star_table.find('tbody')

    table_rows=table_body.find_all('tr')

    for row in table_rows():
        table_cols=row.find_all('td')
        print(table_cols)

        temp_list=[]

        
        for col_data in table_rows():
        
            data= col_data.text.strip()
            print(data)

            temp_list.append(data)

            Scraped_Data.append(temp_list)

        for i in range():
            Star_names=Scraped_Data[i][1]
            Distance=Scraped_Data[i][3]
            Mass=Scraped_Data[i][5]
            Radius=Scraped_Data[i][6]
            Lum=Scraped_Data[i][7]

            required_data=[Star_names,Distance,Mass,Radius,Lum]
            Stars_Data.append(required_data)

headers=["Star_names","Distance","Mass","Radius","Lum"]

star_df_1=pandas.dataframe(Stars_Data,columns=headers)

star_df_1.to_csv('scrapped_data.csv',index=True,index_label="id")