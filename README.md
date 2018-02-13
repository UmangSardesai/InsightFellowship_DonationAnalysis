# InsightFellowship_DonationAnalysis

## Code Explanation
1. To find unique Donors, I used a HashMap of HashMaps. The key for the first order Hashmap would be the 5 digit Zipcode and the key for the second order HashMap would be the name. The second order HashMap will have value as the "Transaction Date". 
2. Once we have the unique donor and also his start date, I use another HashMap to calculate repeating donors. A unique key made up of Zipcode + Year + Receiptient ID. Using this key I could calculate the numbers of times a donor has contributed and the total amouint collected for the combo mentioned

## Test Cases:
1. The sample one.
2. Check that if the dates are unordered, only the repeating donor with latter dates should be considered.
3. Check that if two peple have the same name, they should not be considered as unique, unless they also have the same ZIP
4. Malformed input data like
   - Negative amount
   - Transaction_Date with alphabets
   - Zipcode with less than 5 characters
5. Large input. Code should be efficient enough tp take a long time to process. 
