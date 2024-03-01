# E-commerce Price Comparison Platform

## Project Overview

The E-commerce Price Comparison Platform is a Django-based web application that enables users to compare product prices, delivery speeds, and quality across multiple e-commerce platforms. The system intelligently analyzes various platforms, providing users with a graphical representation of results to aid in making informed purchase decisions.

### Key Features

- **Dynamic Price Comparison:**
  - Searches multiple e-commerce platforms for product prices and delivery details.
  - Presents results in a graphical manner for user-friendly interpretation.

- **Quality Assessment:**
  - Evaluates product quality based on historical data and user reviews.

- **Historical Data Storage:**
  - Utilizes SQL for storing historical data, enabling users to track price changes over time.

## Project Differentiators

1. **Comprehensive Comparison:**
   - Stands out by considering not only prices but also delivery speed and product quality.

2. **Visual Representation:**
   - Offers a graphical representation of comparison results for enhanced user understanding.

3. **Historical Tracking:**
   - Stores historical data in SQL, allowing users to monitor price trends.

## Tech Stacks

- **Django:** Web framework for building the application.
- **HTML and Bootstrap:** Front-end development for a visually appealing interface.
- **Pandas:** Used for efficient data processing.
- **Matplotlib:** Enables graphical representation of comparison results.
- **SQL:** Database management for storing historical data.

## Getting Started

1. Clone the repository: `https://github.com/vengateshk18/django-price-comparison`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `settings.py`.
4. Run migrations: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`

Feel free to explore and contribute to the project!
