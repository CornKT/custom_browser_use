# import json
# import random

# json_data = [
#     {"url": "wordpress.stormbird.vn/"},
#     {"url": "wordpress.stormbird.vn/wp-includes/blocks/navigation/style.min.css"},
#     {"url": "wordpress.stormbird.vn/wp-includes/blocks/image/style.min.css"},
#     {"url": "wordpress.stormbird.vn/wp-includes/js/dist/script-modules/block-library/navigation/view.min.js"},
#     {"url": "wordpress.stormbird.vn/wp-includes/js/dist/script-modules/interactivity/index.min.js"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/images/building-exterior.webp"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/fonts/inter/Inter-VariableFont_slnt,wght.woff2"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/fonts/cardo/cardo_normal_400.woff2"},
#     {"url": "wordpress.stormbird.vn/favicon.ico"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/fonts/cardo/cardo_italic_400.woff2"},
#     {"url": "wordpress.stormbird.vn/"},
#     {"url": "wordpress.stormbird.vn/wp-includes/blocks/navigation/style.min.css"},
#     {"url": "wordpress.stormbird.vn/wp-includes/js/dist/script-modules/block-library/navigation/view.min.js"},
#     {"url": "wordpress.stormbird.vn/wp-includes/blocks/image/style.min.css"},
#     {"url": "wordpress.stormbird.vn/wp-includes/js/dist/script-modules/interactivity/index.min.js"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/fonts/inter/Inter-VariableFont_slnt,wght.woff2"},
#     {"url": "wordpress.stormbird.vn/favicon.ico"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/fonts/cardo/cardo_italic_400.woff2"},
#     {"url": "wordpress.stormbird.vn/wp-content/themes/twentytwentyfour/assets/fonts/cardo/cardo_normal_400.woff2"},
#     {"url": "wordpress.stormbird.vn/"},
#     {"url": "wordpress.stormbird.vn/"},
#     {"url": "wordpress.stormbird.vn/wp-content/plugins/wpforms-lite/assets/css/frontend/modern/wpforms-full.min.css"},
#     {"url": "wordpress.stormbird.vn/wp-includes/blocks/cover/style.min.css"},
#     {"url": "wordpress.stormbird.vn/wp-includes/js/jquery/jquery.min.js"},
#     {"url": "wordpress.stormbird.vn/wp-includes/js/jquery/jquery-migrate.min.js"},
#     {"url": "wordpress.stormbird.vn/"},
#     {"url": "wordpress.stormbird.vn/"},
#     {"url": "wordpress.stormbird.vn/"}
# ]

# # Chuyển JSON thành List[Tuple[str, int]]
# request_logs = []
# count_404 = 0
# max_404 = 5

# for entry in json_data:
#     url = entry["url"]
#     if count_404 < max_404 and random.random() < 0.2:  # Xác suất 404 khoảng 20%
#         status = 404
#         count_404 += 1
#     else:
#         status = 200
#     request_logs.append((url, status))

# # In kết quả
# for log in request_logs:
#     print(log)
from playwright.sync_api import sync_playwright

def save_webpage_as_pdf(url, output_path="output.pdf"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="load")
        page.pdf(path=output_path, format="A4", print_background=True, full_page=True)
        browser.close()
        print(f"Đã lưu PDF tại {output_path}")

# Gọi hàm với URL cần xuất PDF
save_webpage_as_pdf("https://vietjack.me/top-20-cau-trac-nghiem-quy-tac-cong-va-quy-tac-nhan-toan-10-chan-troi-89037.html", "output.pdf")
