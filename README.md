# bageld
Guessing game of athletes

**Backend To Do**:
* Streamline creation of original file
 * staged_videos/ now contains videos with dates assigned
 * raw_videos/ now contains videos that still need to have dates assigned
 * don't need to update code because it currently just searches for the date in the filename, and the prefix doesn't impact the parsing
* Cron job runs at certain time - AWS lambda
* Have folder of files ready to go, script iterates over the files
* have database of videos
* automatically assign dates to video, given atp/wta, top view vs bottom view, when the player was last featured. submit info to the script, and it renames the file automatically - don't include date in video name, instead have top/bottom
  * could do reoptimizations every day - rename older files based on new files
* Expand to other sports
    * Basketball - requires more sophisticated object detection

**Frontend To Do**

* Update css
* Scores are saved
* Update dropdown items to be less hardcoded - combo of top ranked players and players in the database of games


| Given       | When | Then| Status |
| ----------- | ----------- | ----------- | ----------- |
| I have reached the end of the game | The pop-up comes up | Show an option to donate | |
| I have reached the end of the game | ... | Record score in browser cookie | |
| I have reached the end of the game | I refresh the page | I see the end-state pop-up | |
| I have reached the end of the game previously | I reach the end of the game today | I see my score history | |


