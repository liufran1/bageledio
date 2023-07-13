# bageledio
Guessing game of athletes

**To Do**:
* Build frontend
* Save gifs instead of mp4
* Streamline creation of original file
  * Pass filename as arg to main script
  * Upload files to [cloud location](https://stackoverflow.com/questions/16799956/javascript-to-download-a-file-from-amazon-s3-bucket) - probably don't need to persist 
  * Have page read from cloud location
  * Update dictionary the lambda is reading from

**Frontend To Do**

Automatically pull from backend
| Given       | When | Then| Status |
| ----------- | ----------- | ----------- | ----------- |
| I am on the page | the page loads | A call is made to get the hashed answer and the updated files| |

Typeahead dropdown
| Given       | When | Then| Status |
| ----------- | ----------- | ----------- | ----------- |
| Given I am in the dropdown | I begin typing | the dropdown filters for players whose name contains that substring| |
| No player is selected | I try to click the guess button | the button is disabled, and the css is updated accordingly| |
| A player is selected | I try to click the guess button | the button is enabled. Use an event listener to update this| |

Scores are saved

| Given       | When | Then| Status |
| ----------- | ----------- | ----------- | ----------- |
| I have reached the end of the game | The pop-up comes up | Show an option to donate | |
| I have reached the end of the game | ... | Record score in browser cookie | |
| I have reached the end of the game | I refresh the page | I see the end-state pop-up | |
| I have reached the end of the game previously | I reach the end of the game today | I see my score history | |
