# School District Analysis 

## 1) Overview of Election Audit
The purpose of the challenge was to analyze election audit results. Additional data needed to be extracted to complete the election audit. This included the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout. These final results were then transferred to a text file for quick accessibility. 

## 2) Election Audit Results 
- How many votes were cast in this congressional election? 
 	
	Total Votes = 369,711
- Breakdown of the number of votes and the percentage of total votes for each country in the precinct. 

	Jefferson: 10.5% (38,855)

	Denver: 82.8% (306,055)

	Arapahoe: 6.7% (24,801)

	![thisisanimage](https://github.com/cmmoreno9/Election_Analysis/blob/506c506f025ebcd0357b022556575f6c34095a56/code_screenshots/Screen%20Shot%202022-04-08%20at%208.34.02%20AM.png)
	
These results were attained by utilizing the above code. It is important to note, before the execution of this section I had to write a statment that checks if the county is in the county list. If it is not included, I had to append the item into the county list. The following step was setting the county_votes = 0, and then adding the votes to that specific county's vote count. 

- County with the largest amount of votes?

	Denver
	
- Number of votes and the percentage of the total votes each candidate recieved. 

	Charles Casper Stockman: 23.0% (85,213)
	
	Diana DeGette: 73.8% (272,892)
	
	Raymon Anthony Doane: 3.1% (11,606)
	
	![thisisapicture](https://github.com/cmmoreno9/Election_Analysis/blob/506c506f025ebcd0357b022556575f6c34095a56/code_screenshots/Screen%20Shot%202022-04-08%20at%208.35.17%20AM.png)
		
These results were attained by utilizing the above code. It is important to note that before the execution of this section, I had to write a statement that checks if the candidate's name is on the candidate list. If it is not included, I had to append the item into candidate options. The following step was setting the candidate_votes = 0 and then adding the votes to that specific candidate's vote count. 

- Winning candidate, including vote count, and percentage of total votes

	Winner: Diana DeGette
	
	Winner Vote Count: 272,892
	
	Winner Percentage: 73.8%
	
	![thisisanimage](https://github.com/cmmoreno9/Election_Analysis/blob/be3086049283284925f047e231f764d3818425ef/code_screenshots/Screen%20Shot%202022-04-08%20at%208.56.04%20AM.png)
	
- Text file results 

	![thisisaimage](https://github.com/cmmoreno9/Election_Analysis/blob/021b253553bf9a8cde598cab1c2afa9a3e07f9b0/code_screenshots/Screen%20Shot%202022-04-08%20at%208.59.30%20AM.png)
	
## 3) Election-Audit Results 

1. One possible modification for the future is to view the candidate percentage of votes within a county level. This will bring insight into which regions favour a particular candidate. This preference can shed light on which candidates' proposals may not be favoured within that county. Total_votes would need to be broken into three counties' subsets to only look at that specific county. Slight modifications for loops and statements would also be necessary. Another pathway is implementing an if-statement to the code to attain these results. Although this will create a slightly longer code, it can bring valuable information about the political state of each county.

2. A second way to modify the code is to expand the results not by county but by the state for a federal election. Thus, one would need to change the county into states. 
