import open_transform

def main():
    crawl = open_transform.folder_crawler() #crawl through folder
    open_transform.open_transform_message(crawl) #use function to crawl and transform to df
    open_transform.df.to_excel("output"+open_transform.TODAY+".xlsx") #save df to excel
    print(open_transform.df) #print df

if __name__ == '__main__':
    main()