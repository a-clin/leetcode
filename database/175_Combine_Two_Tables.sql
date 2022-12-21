SELECT firstName, lastName, city, state
FROM Person LEFT OUTER JOIN Address using (personId)