#!/usr/bin/env python3
"""
Simple script to generate sitemap.xml for academic website
"""

import os
from datetime import datetime

def generate_sitemap():
    # Your website base URL
    base_url = "https://fawnliu.github.io"
    
    # Get current date for lastmod
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Define your pages
    pages = [
        {"url": "/", "priority": "1.0", "changefreq": "monthly"},
        {"url": "/index.html", "priority": "1.0", "changefreq": "monthly"},
    ]
    
    # Generate sitemap XML
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for page in pages:
        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{base_url}{page["url"]}</loc>\n'
        sitemap_content += f'    <lastmod>{current_date}</lastmod>\n'
        sitemap_content += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        sitemap_content += f'    <priority>{page["priority"]}</priority>\n'
        sitemap_content += '  </url>\n'
    
    sitemap_content += '</urlset>'
    
    # Write to file
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print(f"Sitemap generated successfully! Last updated: {current_date}")

if __name__ == "__main__":
    generate_sitemap() 