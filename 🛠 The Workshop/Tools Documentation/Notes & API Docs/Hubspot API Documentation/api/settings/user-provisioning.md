User Provisioning
=================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the user provisioning API to create and manage users in the account, along with their permissions. You can also set user `firstName` and `lastName` properties through this API. 

To retrieve and update other user information, such as their job title and working hours, use the [users API](/docs/api/crm/users) instead.

Specifying a user
-----------------

When specifying a user with the `userId` path parameter, you can either use the user's ID or the user's email. Specifying based on the user's ID is the default behavior but if you want to use the user's email, you can use the query parameter `idProperty` to set that.

The following `GET` request is fetching a user with the email _myUser@gmail.com:_

`https://api.hubspot.com/settings/v3/users/myUser@gmail.com?idProperty=EMAIL`

You can set the `idProperty` query parameter in any endpoint that takes in `userId` as a path parameter.

Permission Sets
---------------

HubSpot accounts can define permission sets to easily manage multiple users' permissions at once. Once you've created a role and specified certain permissions for it, you can then assign new and existing users the role to grant them the same permissions. Permission sets that have paid seats attached to them can only be modified by applications that have the `billing-write` scope.

The following is an example of a role definition for a user:

// Example specification of a role definition { "id": "1234", "name": "a new role", "requiresBillingWrite": false }

Note that permission sets must be [created in the app](https://knowledge.hubspot.com/settings/create-roles) before attempting to assign them to users.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/settings/user-provisioning#page-feedback)
-------------------------------------------------------------------------------------------------------

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