Idea Tracker Tutorial Part 1
============================

Introduction
------------

This tutorial will show you how to connect a custom app to the HubSpot CRM. The example app we’ll be using creates a simple customer idea forum with an interface where users can sign up, log in, and post ideas.

The Philosophy
--------------

To ensure that any failed API calls don’t impact the user experience, the app logic is totally separate from the integration logic. This is a general best practice for any integration.

While they may look similar, the logic for the initial sync and ongoing sync is also separated, which should help you with any troubleshooting that comes up later.

The Integration
---------------

By the end of this tutorial, you’ll have integrated an app with HubSpot contacts, companies, properties, timeline events, CRM cards, and webhooks. You’ll also learn how to create properties, set up a bi-directional sync, and extend the CRM.  Part 1 focuses on the initial installation of the app. Part 2 will focus on the ongoing sync.

The Technology
--------------

The lessons of this tutorial can be applied to any technology stack—the important takeaway should be the patterns used, not the specific technology or syntax. However, to build and integrate this app, you’ll need:

*   Node.js for the backend
*   Express for the web server
*   MongoDB as the database
*   React for the frontend
*   Docker and Docker Compose to manage dependencies and orchestrate microservices

The Tutorial
------------

### The Starting Point

Users can sign up for the idea tracker and leave ideas for your business to take into consideration. Those users and ideas are saved to a Mongo database with three top-level directories:

*   `client` was created from the [create-react-app](https://create-react-app.dev/) project and is responsible for the parts of the app users see and interact with. There’s no interaction needed for this tutorial, but it serves as an example of how to build an app’s frontend.
*   `web_service` contains the web server, database connection, and Express.js. This provides the app’s “plumbing.” When asked, it provides the saved ideas and users to the frontend and is where you’ll start the OAuth 2.0 flow. It also has the basic APIs you’ll need.
*   `hubspot_service` is another server using Express.js, but only to communicate with HubSpot’s APIs. Right now, it doesn't do anything. 

This state is preserved in the [start branch](https://github.com/zman81988/idea-tracker/tree/start). You should clone this to your local environment to follow along.

### Adding OAuth

Before you can start making API calls to HubSpot, you need permission to access HubSpot data. You can request that permission via the [OAuth 2.0 flow](https://developers.hubspot.com/docs-beta/working-with-oauth). You should use OAuth for three reasons. First is that it’s more secure than using API keys because they are scoped to only what they need and they expire regularly.  Second, you’ll need some APIs that will require OAuth for functionality you’ll add later. Finally, it’s required to be listed and certified in the HubSpot marketplace. 

Authentication starts with [creating an app](https://developers.hubspot.com/docs-beta/creating-an-app) in a [HubSpot developer account](https://app.hubspot.com/signup/developers/). You'll use the client ID and client secret from that app to initiate the OAuth handshake between HubSpot and your integration. To use those credentials in the idea tracker app, copy the `.env.template` file into an `.env` in the same location and put your client ID and client secret in the place of “your\_client\_id” and “your\_client\_secret.” Using an environment file is a good security practice and makes it easier to keep your credentials out of source control. You’ll be able to access these credentials in your code thanks to the configuration already set up in the `docker-compose.yml` file.

The first thing you want to do is `require` the HubSpot API client library by adding `const hubspot = require(“@hubspot/api-client”)` to the top of the `/web_service/src/server.js` file. For the tutorial, this module was already marked as a dependent in the `package.json` file, so you don’t need to `npm install` or `yarn add`.

The next thing you’ll want to do is bring in those environment variables from the previous step.

// ./web\_service/src/server.js const { CLIENT\_ID, BASE\_URL, SCOPES, CLIENT\_SECRET } = process.env; const REDIRECT\_URL = \`${BASE\_URL}/oauth/callback\`;

Next, you’ll send the user to the HubSpot interface, where they’ll grant the idea tracker permission to access their data. The client library has a helper method for this, so you’ll need to create an instance of `hubspot.Client()` and save it to a variable, which in this case is `hubspotClient`. Normally the frontend handles where to send users, but in this case `./client/src/setupProxy.js` lets you handle it from the server-side, keeping all your OAuth logic in one place. This pattern is copied from the [example app](https://github.com/HubSpot/hubspot-api-nodejs/tree/master/sample-apps/oauth-app) bundled with the client library.

// ./web\_services/src/server.js const hubspotClient = new hubspot.Client(); app.get("/oauth/connect", async (req, res) => { const authorizationUrl = hubspotClient.oauth.getAuthorizationUrl( CLIENT\_ID, REDIRECT\_URL, SCOPES ); res.redirect(authorizationUrl); });

If the user grants you permission to access their data, HubSpot directs them back to the idea tracker app to complete the flow.

// ./web\_services/src/server.js app.get("/oauth/callback", async (req, res, next) => { const { code } = req.query; try { const tokensResponse = await hubspotClient.oauth.defaultApi.createToken( "authorization\_code", code, REDIRECT\_URL, CLIENT\_ID, CLIENT\_SECRET ); const { accessToken, refreshToken, expiresIn } = tokensResponse.body; const expiresAt = new Date(Date.now() + expiresIn); const accountInfo = await Account.findOneAndUpdate( { accountId: 1 }, { accessToken, refreshToken, expiresAt }, { new: true, upsert: true } ); res.redirect("/"); } catch (err) { next(err); } });

The code above grabs the `code` from the query string, then makes a request to HubSpot using the `hubspotClient` to redeem the `code` for the `access_token` and the `refresh_token`. Next, it calculates when the `access_token` expires so you’ll know when to request a new one. After that, it saves the tokens and expiration date to the database. For this tutorial, the account ID is hardcorded in. In a real-world app, there would be an account sign-up flow before any users could log in and leave ideas. Finally, it redirects the user back to the home screen of the idea tracker.

You’re now ready to start making API calls to HubSpot. Your code should now look like [this branch](https://github.com/zman81988/idea-tracker/tree/oauth).

### Your first API call

All HubSpot API calls from the idea tracker will be coming from `hubspot_service`, so you need to create a function to make an internal API call from \``web_service` to `hubspot_service`.

// ./web\_services/src/server.js const getAndSaveHubSpotContacts = async accessToken => { console.log("Getting Contacts From HubSpot"); try { hubspotContacts = await axios.get( \`http://hubspot\_service:8080/api/contacts/${accessToken}\` ); } catch (err) { console.log(err); } for (const contact of hubspotContacts.data) { try { const user = await Users.findOneAndUpdate( { email: contact.properties.email }, { hubspotContactId: contact.id } ); } catch (err) { console.log(err); } } };

This is a function that takes the access token as an argument and makes a request to the `hubspot_service` to get all contacts from a HubSpot account. It then uses email addresses to match contacts to idea tracker users and update them with a HubSpot contact ID. Saving the HubSpot-defined ID in the idea tracker database is another best practice and makes future syncing easier.

Before you leave the `./web_service/src/server.js` file, add a call to this function after a successful authorization flow.

// ./web\_service/src/server.js app.get("/oauth/callback", async (req, res, next) => { //… await getAndSaveHubSpotContacts(accessToken); res.redirect("/"); } catch (err) { next(err); } });

Now you need to write the function to actually make the API call. Over in `./hubspot_service/src/server.js`, add: 

// ./hubspot\_service/src/server.js const hubspot = require("@hubspot/api-client"); //… const hubspotClient = new hubspot.Client();

This ensures you can use the client library in the route handler below.

// ./hubspot\_service/src/server.js apiRouter.get("/contacts/:accessToken", async (req, res, next) => { const { accessToken } = req.params; hubspotClient.setAccessToken(accessToken); try { const getAllContacts = async (offset, startingContacts) => { const pageOfContacts = await hubspotClient.crm.contacts.basicApi.getPage( 100, offset ); const endingContacts = startingContacts.concat( pageOfContacts.body.results ); if (pageOfContacts.body.paging) { return await getAllContacts( pageOfContacts.body.paging.next.after, endingContacts ); } else { return endingContacts; } }; const allContacts = await getAllContacts(0, \[\]); res.status(200).send(allContacts); } catch (err) { next(err); } });

This code receives that internal API call you just set up and adds the passed access token to the HubSpot client. Because HubSpot can hold far more contact information than can fit in a single API call, it then uses a recursive function to page through API calls. Once pagination is complete, you can return the results back to the \`web\_service\` to store the results in the database.

Your code should now look like [this branch](https://github.com/zman81988/idea-tracker/tree/firstAPICall).

### Setting up properties

Now that you’ve synced HubSpot contacts to your app, you’ll also want to send information about your app users back to HubSpot. That information will be stored in contact properties, which you’ll create. This will follow the same pattern as when you created a function in the `web_service` that called an endpoint in `hubspot_service`. However, before you do that, we’re\* going to refactor the OAuth handler. 

\*This is a personal preference of the tutorial author. There’s nothing you need to do for this step.

// ./web\_service/src/server.js const initialSyncWithHubSpot = async accessToken => { await getAndSaveHubSpotContacts(accessToken); }; //... app.get("/oauth/callback", async (req, res, next) => { //… initialSyncWithHubSpot(accessToken); res.redirect("/"); } catch (err) { next(err); } });

Next, create a function that calls the `hubspot_service` to ask it to set up the properties you’ll need.

// ./web\_service/src/server.js const setUpHubSpotProperties = async accessToken => { console.log("Setting Up Properties"); try { propertiesResponse = await axios.get( \`http://hubspot\_service:8080/api/properties/${accessToken}\` ); } catch (err) { console.log(err); } };

Don’t forget to add a call to this in your initial sync function.

// ./web\_service/src/server.js const initialSyncWithHubSpot = async accessToken => { await getAndSaveHubSpotContacts(accessToken); await setUpHubSpotProperties(accessToken); };

Finally, add the handler for setting up your properties.

// ./hubspot\_service/src/server.js apiRouter.get("/properties/:accessToken", async (req, res, next) => { const { accessToken } = req.params; const propertyGroupInfo = { name: "ideatrackergroup", displayOrder: -1, label: "Idea Tracker Group" }; const createProperty = async groupName => { const inputs = \[ { groupName, type: "number", label: "Number of Ideas Submitted", fieldType: "number", name: "num\_ideas\_submitted" }, { groupName, type: "string", label: "Faction Rank", fieldType: "string", name: "faction\_rank" } \]; try { return await hubspotClient.crm.properties.batchApi.createBatch( "contacts", { inputs } ); } catch (err) { next(err); } }; hubspotClient.setAccessToken(accessToken); const checkForPropInfo = async () => { const existingPropertyGroups = await hubspotClient.crm.properties.groupsApi.getAll( "contacts" ); const groupExists = existingPropertyGroups.body.results.find( group => group.name === propertyGroupInfo.name ); if (groupExists) { const getAllExistingProperties = async (startingProperties, offset) => { const pageOfProperties = await hubspotClient.crm.properties.coreApi.getAll( "contacts", false, { offset } ); const endingProperties = startingProperties.concat( pageOfProperties.body.results ); if (pageOfProperties.body.paging) { return await getAllExistingProperties( endingProperties, pageOfProperties.body.page.next.after ); } else return endingProperties; }; const allProperties = await getAllExistingProperties(\[\], 0); const existingProperties = allProperties.filter(property => { property.name === "faction\_rank" || property.name === "num\_ideas\_submitted"; }); console.log(existingProperties); if (existingProperties.length === 0) { await createProperty(propertyGroupInfo.name); res.send("Properties Created"); } else { res.send("Properties Already Existed"); } } else { try { const groupResponse = await hubspotClient.crm.properties.groupsApi.create( "contacts", propertyGroupInfo ); const propertiesResponse = await createProperty(propertyGroupInfo.name); res.send(propertiesResponse); } catch (err) { next(err); } } }; checkForPropInfo(); });

This function does a lot, and for good reason. Every property must belong to a property group. You could add the property to a default property group, but that can make it more difficult for a HubSpot user to manage their settings. Instead, it’s recommended that you create a specific group to hold all the properties your integration needs.

Before creating that group, you need to first check if it already exists. This is because it’s fairly common for users to install, uninstall, and then reinstall an app. If you don’t check for the existing property group upon reinstallation, you would get a 409 conflict in response. You should never rely on an error to determine your app logic.

After checking if a group exists, you can create one or move on to checking for the actual properties. You have to check for these for the same reasons you had to check for groups.

Note: You should paginate through responses to the properties’ API calls. HubSpot allows customers to create 1000 properties beyond the default properties, which is too large for a single API call. Once you determine if the properties exist, you can create them as needed.

Your code should now look like [this branch](https://github.com/zman81988/idea-tracker/tree/propertiesSetUp).

### Creating and Updating Contacts

The next step is to fill your newly created properties with information about your app users. To determine which contacts need to be created in HubSpot and which should just be updated, you can check which users have a HubSpot contact ID from the earlier sync.

// ./web\_service/src/server.js const updateExistingHubSpotContacts = async (accessToken, pageNumber) => { console.log("updating existing contacts"); const CONTACTS\_PER\_PAGE = 2; const skip = pageNumber \* CONTACTS\_PER\_PAGE; try { const pageOfContactsFromDB = await Users.find( { hubspotContactId: { $exists: true } }, null, { skip, limit: CONTACTS\_PER\_PAGE } ); await axios.post( \`http://hubspot\_service:8080/api/contacts/update/${accessToken}\`, pageOfContactsFromDB ); console.log(pageOfContactsFromDB); if (pageOfContactsFromDB.length > 0) { pageNumber++; return await updateExistingHubSpotContacts(accessToken, pageNumber); } else { console.log("Done updating contacts"); return; } } catch (err) { console.log(err); } }; const createExistingContacts = async (accessToken, pageNumber) => { console.log("create existing contacts"); const CONTACTS\_PER\_PAGE = 2; const skip = pageNumber \* CONTACTS\_PER\_PAGE; try { const pageOfContactsFromDB = await Users.find( { hubspotContactId: { $exists: false } }, null, { skip, limit: CONTACTS\_PER\_PAGE } ); const createResponse = await axios.post( \`http://hubspot\_service:8080/api/contacts/create/${accessToken}\`, pageOfContactsFromDB ); for (const contact of createResponse.data.results) { await Users.findOneAndUpdate( { email: contact.email }, { hubspotContactId: contact.id } ); } console.log(pageOfContactsFromDB); if (pageOfContactsFromDB.length > 0) { pageNumber++; return await createExistingContacts(accessToken, pageNumber); } else { console.log("Done creating contacts"); return; } } catch (err) { console.log(err); } }; //… const initialSyncWithHubSpot = async accessToken => { await getAndSaveHubSpotContacts(accessToken); await setUpHubSpotProperties(accessToken); await updateExistingHubSpotContacts(accessToken, 0); await createExistingContacts(accessToken, 0); };

// ./hubspot\_service/src/server.js apiRouter.post("/contacts/create/:accessToken", async (req, res, next) => { const { accessToken } = req.params; hubspotClient.setAccessToken(accessToken); const contactsToCreate = req.body; const inputs = contactsToCreate.map(contact => { return { properties: { num\_ideas\_submitted: contact.numIdeasSubmitted, faction\_rank: contact.rank, email: contact.email, firstname: contact.firstName, lastname: contact.lastName } }; }); try { const createResponse = await hubspotClient.crm.contacts.batchApi.createBatch( { inputs } ); console.log(createResponse.body); res.send(createResponse.body); } catch (err) { next(err); } }); apiRouter.post("/contacts/update/:accessToken", async (req, res, next) => { const { accessToken } = req.params; hubspotClient.setAccessToken(accessToken); const contactsToUpdate = req.body; const inputs = contactsToUpdate.map(contact => { return { id: contact.hubspotContactId, properties: { num\_ideas\_submitted: contact.numIdeasSubmitted, faction\_rank: contact.rank } }; }); try { const updateResponse = await hubspotClient.crm.contacts.batchApi.updateBatch( { inputs } ); console.log(updateResponse.body); res.send(updateResponse.body); } catch (err) { next(err); } });

Creating and updating both use batch APIs. This is a best practice—especially for an initial sync—that helps preserve API calls and speed up the process. Note: The tutorial shows using a page size of two contacts per API call. This is so you can see the pagination in action, even with a small database of users.  In practice, batches of 100 are generally recommended. 

Your code should now look like [this branch](https://github.com/zman81988/idea-tracker/tree/createAndUpdateContacts).

### Creating or updating companies

The final step of this tutorial will be to sync HubSpot companies idea tracker factions. This follows the same basic pattern of contact syncing with some key differences.  

// ./web\_service/src/server.js const createOrUpdateCompanies = async accessToken => { console.log("Creating or Updating Companies"); try { const allFactions = await Faction.find({}); for (const faction of allFactions) { const company = await axios.get( \`http://hubspot\_service:8080/api/companies/create-or-update/${faction.domain}/${accessToken}\` ); await new Promise(resolve => setTimeout(resolve, 1000)); console.log("company", company.data); } } catch (err) { console.log(err.message); } }; //… const initialSyncWithHubSpot = async accessToken => { //... await createOrUpdateCompanies(accessToken); };

// ./hubspot\_service/src/server.js apiRouter.get( "/companies/create-or-update/:faction/:accessToken", async (req, res, next) => { const { faction, accessToken } = req.params; hubspotClient.setAccessToken(accessToken); const searchCriteria = { filterGroups: \[ { filters: \[{ propertyName: "domain", operator: "EQ", value: faction }\] } \] }; try { const companiesByDomain = await hubspotClient.crm.companies.searchApi.doSearch( searchCriteria ); if (companiesByDomain.body.results.length > 0) { res.send(companiesByDomain.body.results\[0\]); } else { const newCompany = await hubspotClient.crm.companies.basicApi.create({ properties: { domain: faction } }); res.send(newCompany.body); } } catch (err) { console.log(err); next(err); } } );

Because companies don’t have a unique identifier (like a contact’s email address), you’ll have to search for them. Searching is a different type of operation for HubSpot, requiring a different rate limit. To account for this, you should add some time between each call. Normally, the client library takes care of rate limiting for you, but this case is an exception.

Your code should now look like [this branch](https://github.com/zman81988/idea-tracker/tree/createOrUpdateCompanies).

Conclusion
----------

You now have an app that bi-directionally syncs with HubSpot. The patterns demonstrated in this tutorial show how to use HubSpot’s APIs in a real world scenario. However, it’s important to note that the code you have now is not a production-ready app. It was not designed with UX, security, or scaling in mind. The next step is to take the patterns you learned here and apply them to your own apps.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/idea-tracker-tutorial-part-1#page-feedback)
---------------------------------------------------------------------------------------------------------

Was this article helpful? Yes No

Thanks for letting us know. How would you describe this article?

 Inaccurate: it doesn’t reflect what I see in the product

 Unclear: it’s difficult to understand

 Missing information: it’s not comprehensive enough

 Irrelevant: it doesn’t match what I searched for

Great! Is there anything we could change to make it even more helpful? Is there anything we could change to make this article helpful?

 Allow HubSpot to contact me about my documentation feedback.

Email address

Only used if we need clarification on your feedback.

 

Thank you for your feedback, it means a lot to us.

Sorry this feedback form requires JavaScript to function.

This form is used for documentation feedback only. Learn how to [get help with HubSpot](https://knowledge.hubspot.com/account/get-help-with-hubspot).