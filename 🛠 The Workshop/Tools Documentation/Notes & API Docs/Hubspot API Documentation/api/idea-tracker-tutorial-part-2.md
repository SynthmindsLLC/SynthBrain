Idea Tracker Tutorial Part 2
============================

Introduction
------------

This two-part tutorial will show you how to connect a custom app to the HubSpot CRM. The example app we’ll be using creates a simple customer idea forum with an interface where users can sign up, log in, and post ideas. 

This is Part 2 of the tutorial—as a reminder, in [Part 1](https://developers.hubspot.com/en/docs-beta/idea-tracker-tutorial-part-1) we connected the app to a HubSpot account via OAuth, created properties, and synced contacts and companies. 

Concepts
--------

Just like in Part 1, we’ll be introducing a few key concepts here:

*   Deploying your application so it can be reached outside of your local environment
*   Creating an using a task queue

Both of these are important for handling [webhooks](https://developers.hubspot.com/docs/api/webhooks) from HubSpot.

Technology
----------

Part 2 has a few additions to the technology used in Part 1. However, keep in mind that you can use any technology that fits your needs. Here’s what we recommend:

*   [Kafka](https://kafka.apache.org/) for the message queuing system
*   [Zookeeper](https://zookeeper.apache.org/) for managing the Kafka configuration 
*   [Google Compute Engine](https://cloud.google.com/compute) for hosting the app

The Tutorial
------------

Part 2 picks up right where Part 1 left off. The directory structure is the same. The biggest change is the introduction of two new services in the \`docker-compose.yml\` file, Kafka and Zookeeper. To help interact with these services, the \`.env.template\` file has been updated with new environment variables that you can use. 

### Extending the CRM

You can display rich information about app activity in the Hubspot CRM using the [Timeline API](https://developers.hubspot.com/docs/api/crm/extensions/timeline). Timeline events are structured data that describe things that happen at a particular point in time. Timeline events are immutable (cannot be changed) because once something has happened, you can never go back in time to change that event. In this particular use case, a user can add an idea. They can later go and update the idea or delete the idea but that doesn’t change the fact that at some point they created the idea. If you want to capture those updates and deletes, you create new timeline events.   Each timeline event must have its structure defined before you can tell HubSpot about it. To define an event template, log into your developer account (the same one you used to get your OAuth credentials). In your app settings, create a Timeline Event Type. Set the “Target Record Type” to Contact. In the Data tab, create two properties with the type \`String\` and named \`idea\_title\` and \`idea\_detail.\`  Finally, you can either set the Event header and detail templates to whatever you want, or use this example:

Idea Title: {{ idea\_title }}

With a body template of:

Idea Detail: {{ idea\_detail }} Submitted at: {{#formatDate timestamp format="full"}}{{/formatDate}}

Be sure to take note of the `eventTypeId` , which you’ll find at the end of the URL where you’re editing the templates.   

Now it’s time to actually start sending the events. First, you’ll need to trigger an API call from the `web_service` to the `hubspot_service` when a new idea is created. Do this by creating a function that takes the idea and sends it to the `hubspot_service`:

// ./web\_service/src/Ideas.API.js const createTimeLineEvent = async (idea) => { const accessToken = await getAccessToken(1); try { await axios.post( \`http://hubspot\_service:8080/api/timeline/${accessToken}\`, { idea, } ); } catch (err) { console.log(err); } };

Further down in the same file, modify the idea creation handler to actually call that function.

// ./web\_service/src/Ideas.API.js ideaRouter.post("/", async (req, res, next) => { const idea = req.body; console.log(idea); try { const dbResponse = await Idea.create(idea); const populatedIdea = await dbResponse.populate("author").execPopulate(); res.send(populatedIdea); createTimeLineEvent(populatedIdea); } catch (err) { next(err); } });

This code receives the idea from the `client`, saves it to the database, and uses it to populate information about the author of the post. This gives you the actual name of the author rather than just the ID. From there, you’re generating a new access token and then passing the populated idea over to the `hubspot_service`.

Next, you’ll need to handle this API call and send it over to HubSpot.

// ./hubspot\_service/src/server.js apiRouter.post("/timeline/:accessToken", async (req, res, next) => { const { idea } = req.body; const { accessToken } = req.params; hubspotClient.setAccessToken(accessToken); const timelineEvent = { eventTemplateId: "1003035", objectId: idea.author.hubspotContactId, tokens: { idea\_title: idea.title, idea\_detail: idea.detail, }, }; console.log("sending timeline event", timelineEvent); try { await hubspotClient.crm.timeline.eventsApi.create(timelineEvent); res.send("ok"); } catch (err) { console.log(err); next(err); } });

This code takes that populated idea and maps its author to the contact you want to associate with the timeline event. It also fills in information about the idea itself in the \`tokens\` object. These tokens will populate the template you created earlier. Your code should now look like [this](https://github.com/zman81988/idea-tracker/tree/timeline).

### Hosting

Up until this point, your app has only been available on your local machine. Now you need to start receiving webhooks from HubSpot and your app needs to be available to the larger Internet. You’ll need a couple of things in order to do this:

*   A hosting provider
*   A domain
*   A SSL certificate

For this tutorial, we chose Google Compute Engine as the hosting provider, as well as a domain and SSL certificate that work behind the HubSpot corporate firewall. It’s worth noting that the HubSpot platform uses both AWS and Google Compute. You can use the providers you feel most comfortable with. To host with Google Compute Engine, follow Google’s [instructions](https://cloud.google.com/compute/docs/quickstart-linux). The only adjustment we made was to use a container-optimized image, and we recommend you do the same. 

Once you have a compute instance running, you need to `ssh` into it using the tools provided in Google Console or your favorite CLI. Next, you’ll need to get your files up to this compute instance. If you’re pushing your code to a public Github repository, the easiest way to do this is to clone your Github repository while ssh’d into the instance. If you’re not doing that, you can use SCP (Secure Copy Protocol) from your terminal to transfer your files up to the compute instance. To optimize upload time, make sure you remove your `node_modules` folders before starting.

You’ll also need a SSL certificate for your domain. For now, you can place the certificate and private key in a folder in the `web_service` directory. We’ll cover how to use them later. 

### Deploying your app

Up until this point, your app has been using a development server to provide hot-reloading on the front-end of app. That set up is great for development because you don’t have to refresh the page to see changes to your code.  It’s not so great for production because it’s not optimized for speed. For production you will need to take some of the processes that used to be carried out by the `client` docker service and move them to the `web_service` and have Express serve the files instead of the development server from the `client` service. To do this, you will need to create two different files at the root of the project. First is the Dockerfile: 

\# ./Dockerfile # Setup and build the client FROM node:12.10.0-alpine as client WORKDIR /usr/app/client/ COPY client/package.json ./ COPY client/yarn.lock ./ RUN yarn install COPY client/ ./ RUN yarn build RUN echo "just ran build" # Setup the server FROM node:12.10.0-alpine WORKDIR /usr/app/ COPY --from=client /usr/app/client/build/ ./client/build/ WORKDIR /usr/app/server/ COPY web\_service/package.json ./ COPY web\_service/yarn.lock ./ RUN apk --no-cache add --virtual builds-deps build-base python RUN yarn install COPY web\_service/ ./ EXPOSE 8080

This is a new set of instructions that `docker-compose` will use to create a production-ready `web_service`. The second file you need to create is `docker-compose.prod.yml`:

\# ./docker-compose.prod.yml version: "3" services: zookeeper: image: zookeeper:3.5 expose: - "2181" logging: driver: none tmpfs: "/datalog" kafka: image: wurstmeister/kafka expose: - "9092" volumes: - /var/run/docker.sock:/var/run/docker.sock env\_file: ./.env logging: driver: none depends\_on: - zookeeper web\_service: build: . container\_name: web\_service #context: ./server/ command: /usr/app/server/node\_modules/.bin/nodemon src/server.js volumes: - ./web\_service:/usr/app/server - /usr/app/server/node\_modules ports: - "8080:8080" env\_file: ./.env depends\_on: - mongo hubspot\_service: build: ./hubspot\_service container\_name: hubspot\_service #context: ./server/ command: /usr/app/node\_modules/.bin/nodemon src/server.js volumes: - ./hubspot\_service:/usr/app - /usr/app/node\_modules ports: - "8080" env\_file: ./.env depends\_on: - mongo mongo: image: mongo container\_name: idea\_tracker\_database volumes: - ./mongo-volume:/data/db expose: - "27017" volumes: web\_service: hubspot\_service: mongo:

This tells `docker-compose` how all the different services fit together once they’re built according to the specifications in their Dockerfiles. You can now run `docker-compose -f docker-compose.prod.yml up --build` while `ssh`’d into your compute instance and view your application on a live URL. 

### Receiving your first webhook

To receive webhooks to your publicly inaccessible `hubspot_service`, you need to proxy requests through the `web_service`.

// ./web\_service/src/servers.js app.post("/webhook/platform", async (req, res, next) => { console.log(req.body); try { const proxyRequest = await axios.post( "http://hubspot\_service:8080/webhook/platform", req.body ); res.send(proxyRequest.status); } catch (err) { next(err); } });

To avoid repeating concepts you’ve already completed, the webhook router is already set up for you. The specifics of communicating with the Kafka service are also already set up in `./hubspot_service/src/webhook.js`. 

 Kafka is just a particular technology to accomplish your goal of queuing up webhooks to process the specifics weren’t important. Here’s a general idea of how Kafka works: The `hubspot_service` opens up a connection to Kafka based on information coming from the `.env` file. From there it sets up a topic, which can be subscribed to elsewhere in the app. If needed, this lets other services know about webhooks coming from HubSpot. You can now start receiving webhooks from HubSpot. 

The easiest way to see this in action is to go into your [developer account and set up a subscription for contact property change](https://developers.hubspot.com/docs/api/webhooks). Create subscriptions for `firstname`, `lastname`, `faction_rank`, and `email`. Go into any of these subscriptions and test them by entering the URL where you hosted the app plus the route `/webhook/platform`. When you click the “Test” button, you should see the “200 OK” response from `hubspot_service`.

### Processing webhooks

One of the keys to building a successful integration that uses webhooks is that you shouldn’t attempt to process them before sending the response back to HubSpot. In other words, the processing should be handled asynchronously. The only thing you need to do in the webhook handler is add the webhook payload to the Kafka queue. 

// ./hubspot\_service/src/webhooks.js webhookRouter.post("/platform", (req, res, next) => { // validate webhook signature const payloads = req.body.map((event) => { return { topic: event.subscriptionType, messages: JSON.stringify(event), }; }); producer.send(payloads, (err, data) => { if (err) { next(err); } console.log(data); }); res.send("Ok"); });

While the code above is fairly straightforward, one thing worth noting is that you need to map over the request body to get the actual events the webhook is sending you. This is because each webhook payload can contain multiple events to help conserve resources for you. 

Webhooks events don’t always come in the order they were generated. Because of this, you can’t blindly apply updates you get from HubSpot. You need to first check the timestamp that comes with the event against your own database. There are many ways to handle it, and the right answer depends on your exact setup. In this case, you’re going to use a new schema called UserHistory. This will track the history of properties you’ve set up webhook subscriptions for. 

In `web_service`, you can now consume the Kafka message.

// ./web\_service/src/server.js const userHandler = require("./Users.webhook"); // ... const client = new kafka.KafkaClient({ kafkaHost: KAFKA\_BROKER\_LIST }); const consumer = new kafka.Consumer(client, \[ { topic: "contact.propertyChange" } \]); consumer.on("message", message => { console.log(message); userHandler(message); }); consumer.on("error", err => { console.log(err); });

This sets up a very simple Kafka client which passes off each message to a `userHandler` function defined in `./web_service/src/Users.webhook.js`. This handler determines if the incoming message has new or stale information.

const { fieldMapping } = require("./utils"); const userHandler = async (message) => { const event = JSON.parse(message.value); const { propertyValue, propertyName, occurredAt, objectId, changeSource, } = event; if (changeSource === "API") return; try { const user = await Users.findOne({ hubspotContactId: objectId }); if (user) { console.log("propertyName", propertyName); const fieldToCheck = fieldMapping\[propertyName\]; console.log("fieldToCheck", fieldToCheck); if (fieldToCheck) { if (user\[fieldToCheck\] !== propertyValue) { //check history console.log( "whenmodifed", user.propertyHistory\[\`${fieldToCheck}History\`\]\[0\].whenModified ); console.log("occurredAt", occurredAt); const lastModifiedFromDB = Date.parse( user.propertyHistory\[\`${fieldToCheck}History\`\]\[0\].whenModified ); const lastModifiedFromHS = Date.parse(occurredAt); if (lastModifiedFromDB < lastModifiedFromHS) { user\[fieldToCheck\] = propertyValue; await user.save(); } else { console.log("field value is less current that what is saved"); } } else { console.log("field values already match"); } } else { console.log("Not a mapped property"); } } else { console.log("Does not exist in database, ignoring"); } } catch (err) { console.log(err); } // If they are different, check to see if this is more recent information, then apply }; module.exports = userHandler;

First, the basic logic is to check if the change source of the webhook is API. If so, it was probably triggered by this app and can be ignored. You may want to handle this differently depending on how you view your app’s interactions with other applications. 

Next, it checks if the property that came through the webhook is one that we actually care about. This prevents extra webhook subscriptions from being set up in the developer account. From there, it checks if the value has changed. If it has, the handler checks the timestamp of that change and only saves it if the webhook has more up-to-date information than the database. 

To help keep things manageable, you will want to refactor your app with a utility file.

// ./web\_service/src/utils.js const Account = require("./Accounts.model"); const hubspot = require("@hubspot/api-client"); const { CLIENT\_ID, CLIENT\_SECRET } = process.env; const hubspotClient = new hubspot.Client(); const getAccessToken = async accountId => { try { const account = await Account.findOne({ accountId }); const { expiresAt, accessToken } = account; if (Date(expiresAt) < Date.now()) { return accessToken; } else { const result = await hubspotClient.oauth.defaultApi.createToken( "refresh\_token", undefined, undefined, CLIENT\_ID, CLIENT\_SECRET, account.refreshToken ); console.log("result.body", result.body); const { accessToken, refreshToken, expiresIn } = result.body; console.log("expires\_in", expiresIn); const now = new Date(); const expiresAt = new Date(now.getTime() + expiresIn \* 1000); console.log("expiresAt", expiresAt); account.accessToken = accessToken; account.refreshToken = refreshToken; account.expiresAt = expiresIn; await account.save(); return accessToken; } } catch (err) { console.log(err); } }; const fieldMapping = { firstname: "firstName", lastname: "lastName", faction\_rank: "rank", email: "email" }; module.exports = { getAccessToken, hubspotClient, fieldMapping };

You now have a fully functioning app and source code that matches [this branch](https://github.com/zman81988/idea-tracker/tree/webhookHandling).

Conclusion
----------

You now have an app that uses several best practices when creating a two-way sync with HubSpot. You can use different languages and technologies, but the basic ideas should apply to any project. HubSpot has also created sample apps in other languages showing individual concepts in [PHP](https://github.com/HubSpot/hubspot-api-php/tree/master/sample-apps), [Node.js](https://github.com/HubSpot/hubspot-api-nodejs/tree/master/sample-apps), [Ruby](https://github.com/HubSpot/hubspot-api-ruby/tree/master/sample-apps) and [Python](https://github.com/HubSpot/hubspot-api-python).

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/idea-tracker-tutorial-part-2#page-feedback)
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