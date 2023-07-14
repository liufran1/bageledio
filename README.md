# bageld
Guessing game of athletes

**Backend To Do**:
* Streamline creation of original file
* Cron job runs at certain time
* Have folder of files ready to go, script iterates over the files
* Expand to other sports
    * Basketball - requires more sophisticated object detection

**Frontend To Do**

Automatically pull from backend
| Given       | When | Then| Status |
| ----------- | ----------- | ----------- | ----------- |
| I am on the page | the page loads | A call is made to get the hashed answer and the updated files - need way to persist value of the answer - could try saving it into the dom lmao| |

[Typeahead dropdown](https://jsuites.net/v4/dropdown-and-autocomplete)
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
