# zrh-waiting-time

Scraping and presenting tool for Zürich airport security check waiting times

## Scraping

The scraped endpoint is:

```shell
curl https://dxp-fds.flughafen-zuerich.ch/WaitingTimes
```

Response example:

```json
{
  "maxWaitingTime": "1-3"
}
```

Certainly! Here's a step-by-step suggestion for implementing the program you described:

1. **Identify the target endpoint**: Determine the specific endpoint you want to scrape data from. This could be a website or an API.

2. **Choose a programming language**: Select a programming language you are comfortable with or interested in using. Popular choices for web scraping and data manipulation include Python, Node.js, and Ruby.

3. **Web scraping library**: Choose a web scraping library in your selected programming language. For Python, you could consider libraries like BeautifulSoup or Scrapy. If you prefer Node.js, you could use libraries such as Cheerio or Puppeteer.

4. **Set up a database**: Choose a database management system (DBMS) for storing the scraped data. Common options include PostgreSQL, MySQL, or MongoDB. Set up the database and create a table or collection to store the scraped data.

5. **Database connection**: Install a database driver or ORM (Object-Relational Mapping) library for your selected programming language to establish a connection between your program and the database. For Python, you could use libraries like SQLAlchemy or Psycopg2. In Node.js, libraries like Sequelize or Mongoose can be helpful.

6. **Scrape data from the endpoint**: Write code to scrape the data from the target endpoint using the web scraping library you chose. Extract the relevant information from the HTML or API response and store it in variables or data structures.

7. **Connect to the database**: Use the database connection library you selected to establish a connection with your database. This will allow you to interact with the database, such as inserting, updating, or querying data.

8. **Save the scraped data to the database**: Write code to save the scraped data to the database. Use the appropriate methods provided by the database library to insert the data into the created table or collection.

9. **Data visualization library**: Choose a data visualization library for presenting the results as a graph. Popular choices include Matplotlib (Python), D3.js (JavaScript), or Chart.js (JavaScript).

10. **Generate the graph**: Write code to generate the graph based on the data retrieved from the database. Use the data visualization library you selected to create the desired graph representation.

11. **Run and schedule the program**: Write a script or application that ties all the components together. You can set up a scheduler to run the program at specified intervals to scrape and update the data in the database. Tools like cron (Unix-like systems) or Windows Task Scheduler (Windows) can be used for scheduling.

Remember to consider legal and ethical aspects when scraping data, respecting the website's terms of service, and being mindful of any API rate limits or guidelines.

This step-by-step guide should provide a general outline for your program. Implementation details will vary based on the programming language, libraries, and database management system you choose to work with.