{
"project": "Restii Menu Mobile",
"description": "A mobile-friendly restaurant menu viewer with category navigation and image enlargement functionality. The menu data is loaded from a JSON file and displayed using a responsive design with Tailwind CSS.",
"files_included": [
{
"file": "index.html",
"description": "Main HTML file that dynamically fetches and displays menu categories and items from menu.json, with sticky navigation and click-to-enlarge image feature."
},
{
"file": "menu.json",
"description": "The core data source containing restaurant name, categories, and items with details like name, price, ingredients, and image URLs."
},
{
"file": "images/",
"description": "Folder containing item images used in the menu display."
}
],
"features": [
"Sticky top category navigation bar with horizontal scroll",
"Dynamic loading of categories and menu items from JSON",
"Click on item image to view enlarged modal version",
"Smooth scroll-to-top button",
"Fully responsive and mobile-optimized layout",
"TailwindCSS CDN for styling"
],
"usage": {
"steps": [
"Place index.html, menu.json, and images folder in the same directory.",
"Open index.html in a mobile or desktop browser.",
"The menu will load automatically from menu.json and display all categories and items with images and pricing."
]
},
"json_structure_example": {
"restaurant": "Restaurant Name",
"categories": [
{
"name": "Category Name",
"items": [
{
"name": "Item Name",
"price": "0.00",
"ingredients": ["ingredient1", "ingredient2"],
"image": "images/item-image.jpg"
}
]
}
],
"disclaimer": "Optional disclaimer text"
},
"repository": "https://github.com/jasonhckim/restii_menu_mobile",
"author": "Jason Kim",
"license": "MIT"
}

