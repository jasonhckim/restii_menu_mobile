# Restii Menu Mobile

## Description
**Restii Menu Mobile** is a mobile-friendly, responsive restaurant menu viewer designed for seamless navigation and enhanced user experience. It dynamically loads menu categories and items from a JSON file and features image enlargement, sticky navigation, and smooth scrolling, all styled with Tailwind CSS.

## Features
- Sticky top category navigation bar with horizontal scrolling
- Dynamic loading of categories and menu items from `menu.json`
- Click-to-enlarge images with modal view
- Smooth scroll-to-top button
- Fully responsive and mobile-optimized layout
- Styled using TailwindCSS CDN

## Files Included

| File/Folder       | Description                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------|
| `index.html`     | Main HTML file that dynamically fetches and displays menu categories and items with interactive features.|
| `menu.json`      | Core data source containing restaurant name, categories, items, prices, ingredients, and image URLs.    |
| `images/`        | Folder containing all menu item images used for display and modal enlargement.                          |

## Usage

### Setup Steps
1. Place `index.html`, `menu.json`, and the `images/` folder in the same directory.
2. Open `index.html` in any mobile or desktop browser.
3. The menu will load automatically from `menu.json`, displaying all categories and items with their images and pricing.

## Example JSON Structure
```json
{
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
}
```

## Repository
[GitHub Repository](https://github.com/jasonhckim/restii_menu_mobile)

## Author
Jason Kim

## License
This project is licensed under the [MIT License](LICENSE).

