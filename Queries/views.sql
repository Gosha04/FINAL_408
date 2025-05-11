--
-- View of dealerships with full addresses
--
CREATE VIEW vDealershipAddresses AS
SELECT dealershipID, address.streetAddress, city.cityName, county.countyName, state.stateName, address.ZIP
FROM dealership
INNER JOIN address ON dealership.addressID = address.addressID
INNER JOIN city ON address.cityID = city.cityID
INNER JOIN county ON city.countyID = county.countyID
INNER JOIN state ON county.stateID = state.stateID