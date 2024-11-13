import asyncio
from playwright.async_api import async_playwright
import logging
import pandas as pd
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urlencode, urljoin

urls = [
    # "https://www.f-takken.com/",
    "https://www.f-takken.com/freins/buy/land/area/items?currentTabIndex=0&listtype=land&lang=ja&location=area&locate%5B%5D=40131&locate%5B%5D=40132&locate%5B%5D=40133&locate%5B%5D=40134&locate%5B%5D=40135&locate%5B%5D=40136&locate%5B%5D=40137&locate%5B%5D=40217&locate%5B%5D=40218&locate%5B%5D=40219&locate%5B%5D=40220&locate%5B%5D=40221&locate%5B%5D=40223&locate%5B%5D=40224&locate%5B%5D=40230&locate%5B%5D=40231&locate%5B%5D=40343&locate%5B%5D=40349&locate%5B%5D=40348&locate%5B%5D=40345&locate%5B%5D=40341&locate%5B%5D=40344&locate%5B%5D=40342&locate%5B%5D=40101&locate%5B%5D=40103&locate%5B%5D=40105&locate%5B%5D=40106&locate%5B%5D=40107&locate%5B%5D=40108&locate%5B%5D=40109&locate%5B%5D=40213&locate%5B%5D=40214&locate%5B%5D=40215&locate%5B%5D=40383&locate%5B%5D=40382&locate%5B%5D=40381&locate%5B%5D=40384&locate%5B%5D=40621&locate%5B%5D=40625&locate%5B%5D=40647&locate%5B%5D=40642&locate%5B%5D=40646&locate%5B%5D=40205&locate%5B%5D=40206&locate%5B%5D=40204&locate%5B%5D=40227&locate%5B%5D=40226&locate%5B%5D=40421&locate%5B%5D=40401&locate%5B%5D=40402&locate%5B%5D=40601&locate%5B%5D=40610&locate%5B%5D=40602&locate%5B%5D=40604&locate%5B%5D=40608&locate%5B%5D=40605&locate%5B%5D=40609&locate%5B%5D=40202&locate%5B%5D=40203&locate%5B%5D=40207&locate%5B%5D=40210&locate%5B%5D=40211&locate%5B%5D=40212&locate%5B%5D=40216&locate%5B%5D=40225&locate%5B%5D=40229&locate%5B%5D=40503&locate%5B%5D=40522&locate%5B%5D=40544&locate%5B%5D=40228&locate%5B%5D=40447&locate%5B%5D=40448&locate%5B%5D=35&locate%5B%5D=41&locate%5B%5D=42&locate%5B%5D=43&locate%5B%5D=44&locate%5B%5D=45&locate%5B%5D=46&locate%5B%5D=47&locate%5B%5D=01&locate%5B%5D=02&locate%5B%5D=03&locate%5B%5D=04&locate%5B%5D=05&locate%5B%5D=06&locate%5B%5D=07&locate%5B%5D=08&locate%5B%5D=09&locate%5B%5D=10&locate%5B%5D=19&locate%5B%5D=15&locate%5B%5D=20&locate%5B%5D=16&locate%5B%5D=17&locate%5B%5D=18&locate%5B%5D=11&locate%5B%5D=12&locate%5B%5D=13&locate%5B%5D=14&locate%5B%5D=25&locate%5B%5D=26&locate%5B%5D=27&locate%5B%5D=28&locate%5B%5D=29&locate%5B%5D=30&locate%5B%5D=31&locate%5B%5D=32&locate%5B%5D=33&locate%5B%5D=34&locate%5B%5D=36&locate%5B%5D=37&locate%5B%5D=38&locate%5B%5D=39&order1=pl&order2=&limit=100&data_21=0&data_22=1500&data_23=500&data_24=1500&data_486=&data_486_code=&data_487=&data_487_code=",
    # "https://www.f-takken.com/freins/buy/land/area/items?listtype=land&lang=ja&location=area&locate%5B0%5D=40131&locate%5B1%5D=40132&locate%5B2%5D=40133&locate%5B3%5D=40134&locate%5B4%5D=40135&locate%5B5%5D=40136&locate%5B6%5D=40137&locate%5B7%5D=40217&locate%5B8%5D=40218&locate%5B9%5D=40219&locate%5B10%5D=40220&locate%5B11%5D=40221&locate%5B12%5D=40223&locate%5B13%5D=40224&locate%5B14%5D=40230&locate%5B15%5D=40231&locate%5B16%5D=40343&locate%5B17%5D=40349&locate%5B18%5D=40348&locate%5B19%5D=40345&locate%5B20%5D=40341&locate%5B21%5D=40344&locate%5B22%5D=40342&locate%5B23%5D=40101&locate%5B24%5D=40103&locate%5B25%5D=40105&locate%5B26%5D=40106&locate%5B27%5D=40107&locate%5B28%5D=40108&locate%5B29%5D=40109&locate%5B30%5D=40213&locate%5B31%5D=40214&locate%5B32%5D=40215&locate%5B33%5D=40383&locate%5B34%5D=40382&locate%5B35%5D=40381&locate%5B36%5D=40384&locate%5B37%5D=40621&locate%5B38%5D=40625&locate%5B39%5D=40647&locate%5B40%5D=40642&locate%5B41%5D=40646&locate%5B42%5D=40205&locate%5B43%5D=40206&locate%5B44%5D=40204&locate%5B45%5D=40227&locate%5B46%5D=40226&locate%5B47%5D=40421&locate%5B48%5D=40401&locate%5B49%5D=40402&locate%5B50%5D=40601&locate%5B51%5D=40610&locate%5B52%5D=40602&locate%5B53%5D=40604&locate%5B54%5D=40608&locate%5B55%5D=40605&locate%5B56%5D=40609&locate%5B57%5D=40202&locate%5B58%5D=40203&locate%5B59%5D=40207&locate%5B60%5D=40210&locate%5B61%5D=40211&locate%5B62%5D=40212&locate%5B63%5D=40216&locate%5B64%5D=40225&locate%5B65%5D=40229&locate%5B66%5D=40503&locate%5B67%5D=40522&locate%5B68%5D=40544&locate%5B69%5D=40228&locate%5B70%5D=40447&locate%5B71%5D=40448&locate%5B72%5D=35&locate%5B73%5D=41&locate%5B74%5D=42&locate%5B75%5D=43&locate%5B76%5D=44&locate%5B77%5D=45&locate%5B78%5D=46&locate%5B79%5D=47&locate%5B80%5D=01&locate%5B81%5D=02&locate%5B82%5D=03&locate%5B83%5D=04&locate%5B84%5D=05&locate%5B85%5D=06&locate%5B86%5D=07&locate%5B87%5D=08&locate%5B88%5D=09&locate%5B89%5D=10&locate%5B90%5D=19&locate%5B91%5D=15&locate%5B92%5D=20&locate%5B93%5D=16&locate%5B94%5D=17&locate%5B95%5D=18&locate%5B96%5D=11&locate%5B97%5D=12&locate%5B98%5D=13&locate%5B99%5D=14&locate%5B100%5D=25&locate%5B101%5D=26&locate%5B102%5D=27&locate%5B103%5D=28&locate%5B104%5D=29&locate%5B105%5D=30&locate%5B106%5D=31&locate%5B107%5D=32&locate%5B108%5D=33&locate%5B109%5D=34&locate%5B110%5D=36&locate%5B111%5D=37&locate%5B112%5D=38&locate%5B113%5D=39&order1=pl&order2=&limit=100&data_21=0&data_22=1500&data_23=500&data_24=1500&data_486=&data_486_code=&data_487=&data_487_code=&page=2&currentTabIndex=0",
]


link_in_page = "<a class='detail-submit' data-id='98846684'"
detail_url = "https://www.f-takken.com/freins/items/98846684?1731491730059"
square_meters = "土地面積"
land_title = "地目"
address = "所在地"
table_in_details_page = "<table class='detail-list'"


# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def generate_page_url(base_url, page_num):
    """Generate URL for specific page number"""
    parsed = urlparse(base_url)
    qs = parse_qs(parsed.query)
    qs["page"] = [str(page_num)]
    return urljoin(base_url, f"{parsed.path}?{urlencode(qs, doseq=True)}")


async def get_total_pages(page):
    """Detect total number of pages from pagination element"""
    await page.goto(urls[0])
    await page.wait_for_selector(".uk-pagination")

    try:
        # Get all page numbers from pagination
        page_numbers = await page.eval_on_selector(
            ".uk-pagination",
            """(element) => {
                const links = element.querySelectorAll('a[href^="#page-"]');
                const numbers = Array.from(links).map(link => {
                    const match = link.getAttribute('href').match(/#page-(\\d+)/);
                    return match ? parseInt(match[1]) : null;
                }).filter(num => num !== null);
                return Math.max(...numbers);
            }""",
        )

        logger.info(f"Detected {page_numbers} total pages")
        return page_numbers

    except Exception as e:
        logger.error(f"Error detecting total pages: {e}")
        logger.warning("Defaulting to 1 page")
        return 1


async def get_all_data_ids(page):
    all_data_ids = set()

    # Get total pages
    total_pages = await get_total_pages(page)

    # Generate URLs for all pages
    page_urls = [urls[0]] + [
        generate_page_url(urls[0], i) for i in range(2, total_pages + 1)
    ]

    for i, url in enumerate(page_urls, 1):
        logger.info(f"Scanning page {i} of {len(page_urls)} for data-ids")
        try:
            await page.goto(url)
            await page.wait_for_selector(".detail-submit")

            data_ids = await page.eval_on_selector_all(
                ".detail-submit",
                'elements => elements.map(el => el.getAttribute("data-id"))',
            )

            new_ids = set(id for id in data_ids if id)
            previous_count = len(all_data_ids)
            all_data_ids.update(new_ids)

            logger.info(
                f"Found {len(new_ids)} ids on page {i} "
                f"({len(all_data_ids) - previous_count} new), "
                f"total unique ids so far: {len(all_data_ids)}"
            )

            # If we don't find any new IDs, we might have reached the end
            if len(all_data_ids) == previous_count:
                logger.info("No new IDs found on this page, might be last page")
                break

        except Exception as e:
            logger.error(f"Error processing page {i}: {e}")
            break

    return list(all_data_ids)


async def scrape_listings():
    async with async_playwright() as p:
        logger.info("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        results = []

        # Get deduplicated list of data_ids first
        unique_data_ids = await get_all_data_ids(page)
        logger.info(f"Total unique properties to process: {len(unique_data_ids)}")

        # Process each unique data_id
        for index, data_id in enumerate(unique_data_ids, 1):
            if index > 5:
                break
            detail_url = f"https://www.f-takken.com/freins/items/{data_id}"
            logger.info(
                f"Processing listing {index}/{len(unique_data_ids)}: {detail_url}"
            )

            try:
                await page.goto(detail_url)
                await page.wait_for_selector(".detail-list")

                square_meters_value = None
                land_title_value = None
                address_value = None

                property_details = await page.eval_on_selector_all(
                    "table.detail-list tr",
                    """rows => {
                    const details = {};
                    rows.forEach(row => {
                        const cells = row.querySelectorAll('td');
                        if (cells.length >= 2) {
                            const label = cells[0].textContent.trim();
                            switch(label) {
                                case '土地面積':
                                    details.square_meters = cells[1].textContent.trim();
                                    break;
                                case '地目':
                                    details.land_title = cells[1].textContent.trim();
                                    break;
                                case '所在地':
                                    const addressCell = cells[1];
                                    const addressSpan = addressCell.querySelector('span');
                                    const mapLink = addressCell.querySelector('a');
                                    details.address = addressSpan ? addressSpan.textContent.trim() : '';
                                    details.map_link = mapLink ? mapLink.href : '';
                                    break;
                            }
                        }
                    });
                    return details;
                }""",
                )

                image_url = await page.eval_on_selector(
                    "ul.thumbs img",
                    """img => {
                        const src = img.getAttribute('src');
                        return src.startsWith('//') ? 'https:' + src : src;
                    }""",
                )

                result = {
                    "url": detail_url,
                    "id": data_id,
                    "square_meters": property_details.get("square_meters"),
                    "land_title": property_details.get("land_title"),
                    "address": property_details.get("address"),
                    "map_link": property_details.get("map_link"),
                    "image_url": image_url,
                }

                results.append(result)
                logger.info(f"Successfully scraped data: {result}")

            except Exception as e:
                logger.error(f"Error processing {detail_url}: {str(e)}")
                continue

        logger.info("Closing browser...")
        await browser.close()
        return results


async def main():
    logger.info("Starting scraping process...")
    results = await scrape_listings()
    logger.info(f"Scraping completed. Total items scraped: {len(results)}")

    # Create DataFrame and save to CSV
    df = pd.DataFrame(results)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"property_listings_{timestamp}.csv"

    # Save to CSV
    logger.info(f"Saving results to {filename}")
    df.to_csv(
        filename, index=False, encoding="utf-8-sig"
    )  # utf-8-sig for proper Japanese character encoding
    logger.info("Data saved successfully")

    return results


if __name__ == "__main__":
    results = asyncio.run(main())
