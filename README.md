# bageledio
Guessing game of athletes

**To Do**:
* Build frontend
* Pass filename as arg to main script
* Streamline creation of original file

**Frontend To Do**
| Given       | When | Then|
| ----------- | ----------- | ----------- |
| I navigate to the page | The page loads |The first gif is available and I see a dropdown to select a player and a button to submit |
| I am on the page and the flag is set to male | I click on the dropdown |I see a list of the top 100 players in the ATP|
| I am on the page and the flag is set to female | I click on the dropdown |I see a list of the top 100 players in the WTA|
| Given I am in the dropdown | I begin typing | the dropdown filters for players whose name contains that substring|
| A player is selected | I click the submit button | A call is made with the player's name to https://ci39xriub5.execute-api.us-east-2.amazonaws.com/bagelio_check?player_name={player_name} |
| A successful API call | The response is false | show the next gif |
| I am on on the last gif | The response is false | Show pop-up indicating that I lost |
| A successful API call | The response is true | Show pop-up indicating that I won |
| I have reached the end of the game | The pop-up comes up | Show the number of guesses I took |
| I have reached the end of the game | The pop-up comes up | Show an option to share |
| I have reached the end of the game | The pop-up comes up | Show an option to donate |
| The pop-up is open | I click  the share button | My clipboard is filled with "bageld {todays_date}: \n" black squares for each wrong guess and a tennis ball for the correct guess \n link to page |
