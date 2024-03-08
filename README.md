# E-commerce Price Comparison Platform

## Project Overview

The E-commerce Price Comparison Platform is a Django-based web application that empowers users to make informed purchasing decisions by comparing product prices, delivery speeds, and quality across multiple e-commerce platforms. Leveraging intelligent analysis, the system provides users with a graphical representation of results, enhancing the overall shopping experience.

### Key Features

- **Dynamic Price Comparison:**
  - The platform systematically searches multiple e-commerce platforms, extracting information on product prices and delivery details.
  - Utilizes an intuitive graphical representation for users to interpret and compare data effectively.

- **Quality Assessment:**
  - Evaluates product quality based on historical data and user reviews, contributing to a holistic product assessment.

- **Historical Data Storage:**
  - Implements SQL for efficient storage and retrieval of historical data, allowing users to track price changes over time.

## Project Differentiators

1. **Comprehensive Comparison:**
   - Stands out by considering not only prices but also the critical factors of delivery speed and product quality.

2. **Visual Representation:**
   - Offers a graphical representation of comparison results for enhanced user understanding and decision-making.

3. **Historical Tracking:**
   - Stores historical data in SQL, enabling users to monitor and analyze price trends, fostering a data-driven shopping experience.

## Tech Stacks

- **Django:** A robust web framework for building the application.
- **HTML and Bootstrap:** Front-end development for a visually appealing and user-friendly interface.
- **Pandas:** Efficient data processing for effective analysis.
- **Matplotlib:** Enables the creation of graphical representations of comparison results.
- **SQL:** A reliable database management system for storing and retrieving historical data.
- **BeautifulSoup:** Utilized for web scraping, extracting data from e-commerce platforms to facilitate dynamic price comparison.

## Getting Started

1. Clone the repository: `https://github.com/vengateshk18/django-price-comparison`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `settings.py`.
4. Run migrations: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`

Feel free to explore and contribute to the project!

