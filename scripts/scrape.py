import mechanicalsoup

urls = [
    # "https://www.f-takken.com/",
    "https://www.f-takken.com/freins/buy/land/area/items?currentTabIndex=0&listtype=land&lang=ja&location=area&locate%5B%5D=40131&locate%5B%5D=40132&locate%5B%5D=40133&locate%5B%5D=40134&locate%5B%5D=40135&locate%5B%5D=40136&locate%5B%5D=40137&locate%5B%5D=40217&locate%5B%5D=40218&locate%5B%5D=40219&locate%5B%5D=40220&locate%5B%5D=40221&locate%5B%5D=40223&locate%5B%5D=40224&locate%5B%5D=40230&locate%5B%5D=40231&locate%5B%5D=40343&locate%5B%5D=40349&locate%5B%5D=40348&locate%5B%5D=40345&locate%5B%5D=40341&locate%5B%5D=40344&locate%5B%5D=40342&locate%5B%5D=40101&locate%5B%5D=40103&locate%5B%5D=40105&locate%5B%5D=40106&locate%5B%5D=40107&locate%5B%5D=40108&locate%5B%5D=40109&locate%5B%5D=40213&locate%5B%5D=40214&locate%5B%5D=40215&locate%5B%5D=40383&locate%5B%5D=40382&locate%5B%5D=40381&locate%5B%5D=40384&locate%5B%5D=40621&locate%5B%5D=40625&locate%5B%5D=40647&locate%5B%5D=40642&locate%5B%5D=40646&locate%5B%5D=40205&locate%5B%5D=40206&locate%5B%5D=40204&locate%5B%5D=40227&locate%5B%5D=40226&locate%5B%5D=40421&locate%5B%5D=40401&locate%5B%5D=40402&locate%5B%5D=40601&locate%5B%5D=40610&locate%5B%5D=40602&locate%5B%5D=40604&locate%5B%5D=40608&locate%5B%5D=40605&locate%5B%5D=40609&locate%5B%5D=40202&locate%5B%5D=40203&locate%5B%5D=40207&locate%5B%5D=40210&locate%5B%5D=40211&locate%5B%5D=40212&locate%5B%5D=40216&locate%5B%5D=40225&locate%5B%5D=40229&locate%5B%5D=40503&locate%5B%5D=40522&locate%5B%5D=40544&locate%5B%5D=40228&locate%5B%5D=40447&locate%5B%5D=40448&locate%5B%5D=35&locate%5B%5D=41&locate%5B%5D=42&locate%5B%5D=43&locate%5B%5D=44&locate%5B%5D=45&locate%5B%5D=46&locate%5B%5D=47&locate%5B%5D=01&locate%5B%5D=02&locate%5B%5D=03&locate%5B%5D=04&locate%5B%5D=05&locate%5B%5D=06&locate%5B%5D=07&locate%5B%5D=08&locate%5B%5D=09&locate%5B%5D=10&locate%5B%5D=19&locate%5B%5D=15&locate%5B%5D=20&locate%5B%5D=16&locate%5B%5D=17&locate%5B%5D=18&locate%5B%5D=11&locate%5B%5D=12&locate%5B%5D=13&locate%5B%5D=14&locate%5B%5D=25&locate%5B%5D=26&locate%5B%5D=27&locate%5B%5D=28&locate%5B%5D=29&locate%5B%5D=30&locate%5B%5D=31&locate%5B%5D=32&locate%5B%5D=33&locate%5B%5D=34&locate%5B%5D=36&locate%5B%5D=37&locate%5B%5D=38&locate%5B%5D=39&order1=pl&order2=&limit=100&data_21=0&data_22=1500&data_23=500&data_24=1500&data_486=&data_486_code=&data_487=&data_487_code=",
    # "https://www.f-takken.com/freins/buy/land/area/items?listtype=land&lang=ja&location=area&locate%5B0%5D=40131&locate%5B1%5D=40132&locate%5B2%5D=40133&locate%5B3%5D=40134&locate%5B4%5D=40135&locate%5B5%5D=40136&locate%5B6%5D=40137&locate%5B7%5D=40217&locate%5B8%5D=40218&locate%5B9%5D=40219&locate%5B10%5D=40220&locate%5B11%5D=40221&locate%5B12%5D=40223&locate%5B13%5D=40224&locate%5B14%5D=40230&locate%5B15%5D=40231&locate%5B16%5D=40343&locate%5B17%5D=40349&locate%5B18%5D=40348&locate%5B19%5D=40345&locate%5B20%5D=40341&locate%5B21%5D=40344&locate%5B22%5D=40342&locate%5B23%5D=40101&locate%5B24%5D=40103&locate%5B25%5D=40105&locate%5B26%5D=40106&locate%5B27%5D=40107&locate%5B28%5D=40108&locate%5B29%5D=40109&locate%5B30%5D=40213&locate%5B31%5D=40214&locate%5B32%5D=40215&locate%5B33%5D=40383&locate%5B34%5D=40382&locate%5B35%5D=40381&locate%5B36%5D=40384&locate%5B37%5D=40621&locate%5B38%5D=40625&locate%5B39%5D=40647&locate%5B40%5D=40642&locate%5B41%5D=40646&locate%5B42%5D=40205&locate%5B43%5D=40206&locate%5B44%5D=40204&locate%5B45%5D=40227&locate%5B46%5D=40226&locate%5B47%5D=40421&locate%5B48%5D=40401&locate%5B49%5D=40402&locate%5B50%5D=40601&locate%5B51%5D=40610&locate%5B52%5D=40602&locate%5B53%5D=40604&locate%5B54%5D=40608&locate%5B55%5D=40605&locate%5B56%5D=40609&locate%5B57%5D=40202&locate%5B58%5D=40203&locate%5B59%5D=40207&locate%5B60%5D=40210&locate%5B61%5D=40211&locate%5B62%5D=40212&locate%5B63%5D=40216&locate%5B64%5D=40225&locate%5B65%5D=40229&locate%5B66%5D=40503&locate%5B67%5D=40522&locate%5B68%5D=40544&locate%5B69%5D=40228&locate%5B70%5D=40447&locate%5B71%5D=40448&locate%5B72%5D=35&locate%5B73%5D=41&locate%5B74%5D=42&locate%5B75%5D=43&locate%5B76%5D=44&locate%5B77%5D=45&locate%5B78%5D=46&locate%5B79%5D=47&locate%5B80%5D=01&locate%5B81%5D=02&locate%5B82%5D=03&locate%5B83%5D=04&locate%5B84%5D=05&locate%5B85%5D=06&locate%5B86%5D=07&locate%5B87%5D=08&locate%5B88%5D=09&locate%5B89%5D=10&locate%5B90%5D=19&locate%5B91%5D=15&locate%5B92%5D=20&locate%5B93%5D=16&locate%5B94%5D=17&locate%5B95%5D=18&locate%5B96%5D=11&locate%5B97%5D=12&locate%5B98%5D=13&locate%5B99%5D=14&locate%5B100%5D=25&locate%5B101%5D=26&locate%5B102%5D=27&locate%5B103%5D=28&locate%5B104%5D=29&locate%5B105%5D=30&locate%5B106%5D=31&locate%5B107%5D=32&locate%5B108%5D=33&locate%5B109%5D=34&locate%5B110%5D=36&locate%5B111%5D=37&locate%5B112%5D=38&locate%5B113%5D=39&order1=pl&order2=&limit=100&data_21=0&data_22=1500&data_23=500&data_24=1500&data_486=&data_486_code=&data_487=&data_487_code=&page=2&currentTabIndex=0",
]



link_in_page = "<a class='detail-submit' data-id='98846684'"
detail_url = "https://www.f-takken.com/freins/items/98846684?1731491730059"
square_meters = "土地面積"
land_title = "地目"
table_in_details_page = "<table class='detail-list'"


import mechanicalsoup
import re

def extract_id_from_url(url):
    match = re.search(r'/items/(\d+)', url)
    return match.group(1) if match else None

def scrape_details(browser, url):
    page = browser.get(url)
    tables = page.soup.find_all('table', class_='detail-list')
    
    square_meters_value = None
    land_title_value = None
    
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                label = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                
                if label == square_meters:
                    square_meters_value = value
                elif label == land_title:
                    land_title_value = value
    
    return square_meters_value, land_title_value

def scrape_listings():
    browser = mechanicalsoup.Browser()
    results = []
    
    for url in urls:
        print(url)
        page = browser.get(url)
        detail_links = page.soup.find_all('a')
        # print(page)
        # print(detail_links)
        print("Status code:", page.status_code)
        print("\nFull HTML:")
        print(page.soup.prettify())
        
        for link in detail_links:
            data_id = link.get('data-id')
            if data_id:
                detail_url = f"https://www.f-takken.com/freins/items/{data_id}"
                square_meters_value, land_title_value = scrape_details(browser, detail_url)
                
                result = {
                    "url": detail_url,
                    "square_meters": square_meters_value,
                    "id": data_id,
                    "land_title": land_title_value
                }
                results.append(result)
    
    return results

if __name__ == "__main__":
    results = scrape_listings()
    print(f"Scraped {len(results)} listings:")
    for result in results:
        print(result)