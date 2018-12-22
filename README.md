<h1>NBA Twitter Analysis</h1>
<p>
The project given to us was to demonstrate an Extract-Transform-Load process using Python.  The initial considerations were two-fold.  Firstly, we had to find a some appropriate datasets.  We decided on three related datasets from different sources:
<p>
<ol>
<li>The “Social Power NBA” dataset from Kaggle</li></li>
<li>A game data API endpoint from stats.nba.com</li></li>
<li>The Twitter API</li>
</ol>
<p>
  Secondly, and relatedly, we had to decide what types of questions we wanted analysts be able to inquire of the dataset we were compiling.  Ultimately, the main question we wanted to be able to ask of our gestalt dataset were along the lines of what types relationships existed between a player’s activity on the court and their activity on twitter.  We were interested in being able to see how frequently a particular player’s twitter account was mentioned and what sorts of correlations that had with their on-court performance and personal twitter activity.
<p>
  Rather than extract all the data, transform all the data, and load it all at once, we structured our code to run a single extraction/transformation to produce a bridge table.  This bridge table was then used to run additional extractions ad-hoc based on user specified inputs such as date ranges.  Initial data transforms were then performed on the API call results before being loaded into a mysql environment, as we would be using relational databases throughout the process.
<p>
  The Social Power NBA dataset from Kaggle was our starting point.  This dataset came as a *.csv file containing a sample of 100 NBA players, and had some personal stats from the 2016-2017 season along with their NBA player ID and twitter handle (if they had one).  This dataset was going to be the linchpin for our ETL process, as it would allow us to bridge the NBA data with the Twitter data.  The data required some cleaning & preparation to ease its use in the python environment, as not all columns would be necessary, we eliminated players who didn’t have a twitter handle, and we wanted to promote column name continuity across all datasets. 
<p>
  We then proceeded to use this database as a list for performing API calls on the other two datasets. This allowed us to minimize calling unnecessary data through APIs that otherwise would have been filtered out and discarded while performing joins on databases in memory.
<p>
  The <b>PLAYER_ID</b> column was iterated against the NBA stats API to pull game data from a specified date range. Various statistics regarding the players performance within games in the specified date range  were pulled through the API into a local dataframe, reorganized, and then sent to the local mySQL environment.
<p>
  Likewise a series of API calls using the <b>TWITTER_HANDLE</b> column were run against the Twitter API to pull tweet data regarding the given list of players.  The Twitter API calls each returned a significant quantity of data that required extensive examination and filtering to narrow down the data to just the fields that would be relevant to the analyses we would expect to be run on the final database.
<p>
  Because of the ad-hoc nature of the API calls, this final database would allow examination of Twitter activity regarding a player (not just tweets from the player themselves) that could be contrasted against a number of criteria.  Examples are listed below:
<ul>
  <li>Number of tweets about a player during/after a particular game</li>
  <li>Trends over time (such as a season, or year) regarding player performance vs public mindshare</li> 
</ul>
