Currencies[](https://developers.hubspot.com/docs/api/settings/currencies#currencies)
------------------------------------------------------------------------------------

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

With the currencies API, you can manage the currencies used in your HubSpot account, including setting your account's company currency, creating additional currencies, and updating currency exchange rates. Learn more about [adding and editing currencies within HubSpot.](https://knowledge.hubspot.com/deals/add-and-edit-your-account-currencies)

Supported currencies[](https://developers.hubspot.com/docs/api/settings/currencies#supported-currencies)
--------------------------------------------------------------------------------------------------------

Only certain currencies are supported for use in HubSpot. To retrieve a list of HubSpot's supported currencies and their codes, make a `GET` request to `/settings/v3/currencies/codes`.

You can use any of the returned codes as values for the `currencyCode`, `fromCurrencyCode`, and `toCurrencyCode` properties.

Add account currencies and set exchange rates[](https://developers.hubspot.com/docs/api/settings/currencies#add-account-currencies-and-set-exchange-rates)
----------------------------------------------------------------------------------------------------------------------------------------------------------

Depending on your HubSpot subscription, you can add additional currencies for use in your account, and set their exchange rates compared to your company currency. Learn more about the number of currencies you can have in your account in the [HubSpot Product & Services Catalog.](https://legal.hubspot.com/hubspot-product-and-services-catalog)

To add a currency and set the exchange rate, or add a new exchange rate for an existing currency, make a `POST` request to `/settings/v3/currencies/exchange-rates`. In your request, the following fields are required:

*   `fromCurrencyCode`: the currency code of the currency you want to add to your account. This must be one of HubSpot's supported currency codes.
*   `conversionRate`: the exchange rate from the additional currency to your company currency. The value must be greater than 0 and can contain up to 6 decimal values (e.g., `1.36`). Any values with more than 6 decimal places will be rounded (e.g., `1.2345678` becomes `1.234568`).

You can also include a timestamp using the following field:

*   `effectiveAt`: the date and time the exchange rate takes effect. Values can be in either [long date](https://www.jarte.com/help_new/date_and_time_formats.html) or [ISO 8601](/docs/api/faq#timestamps) format.

For example, your request may look like:

///Example request { "fromCurrencyCode": "EUR", "conversionRate": "1.3", "effectiveAt": "2023-05-08T14:59:19.813Z" }

To add multiple currencies and set their exchange rates in bulk, make a `POST` request to `/settings/v3/currencies/exchange-rates​/batch​/create`. Your request must include the `fromCurrencyCode` and `conversionRate` properties for each currency.

For example, your request may look like:

///Example request body { "inputs": \[ { "fromCurrencyCode": "USD", "conversionRate": 2.7 }, { "fromCurrencyCode": "EUR", "conversionRate": 1.3 } \] }

Retrieve account currencies and exchange rates[](https://developers.hubspot.com/docs/api/settings/currencies#retrieve-account-currencies-and-exchange-rates)
------------------------------------------------------------------------------------------------------------------------------------------------------------

You can view your account's current and historical currencies and exchange rates.

To view your account's company currency, make a `GET` request to `/settings/v3/currencies/company-currency`. To view all of your account's current currencies and exchange rates, make a `GET` request to `/settings/v3/currencies/exchange-rates/current`. When you make a successful request, the response will include the IDs of the exchange rates set in your account. 

To view a specific currency and its exchange rate, make a `GET` request to `/settings/v3/currencies/exchange-rates/{exchangeRateId}`.

To view all of your account's currencies and exchange rates, including historical currencies, make a `GET` request to `/settings/v3/currencies/exchange-rates`. You can filter which currencies and exchange rates are returned using the `limit`, `after`, `fromCurrencyCode` and `toCurrencyCode` query parameters in your request.

Update your account's company currency[](https://developers.hubspot.com/docs/api/settings/currencies#update-your-account-s-company-currency)
--------------------------------------------------------------------------------------------------------------------------------------------

Your account's [company currency](https://knowledge.hubspot.com/deals/add-and-edit-your-account-currencies#company-currency) is the currency used in deal amount totals, deal reports, and when creating new deals in HubSpot.

To update your account's company currency, make a `PUT` request to `/settings/v3/currencies/company-currency`. In your request, include the `currencyCode` value for the currency you want to set as your company currency. For example, your request may look like:

///Example request body { "currencyCode": "AED" }

**Please note**: for accounts with multiple currencies, the company currency will have an automatically generated self-referencing rate (e.g., EUR/EUR=1.0). This rate is not modifiable via API.

Update currency exchange rates[](https://developers.hubspot.com/docs/api/settings/currencies#update-currency-exchange-rates)
----------------------------------------------------------------------------------------------------------------------------

Once currencies are set up in your HubSpot account, you can update their exchange rates. To update an individual exchange rate, make a `PATCH` request to `/settings/v3/currencies/exchange-rates/{exchangeRateId}`. In your request, include the new exchange rate in the `conversionRate` property. Your request may look like:

///Example request body { "conversionRate": 2 }

To update multiple currencies, make a `POST` request to `/settings/v3/currencies/exchange-rates/batch/update`. In your request, include the exchange rate IDs and the new `conversionRate` values. For example:

///Example request body { "inputs": \[ { "id": "string", "conversionRate": 1.3 }, { "id": "string", "conversionRate": 2 } \] }

Hide a currency[](https://developers.hubspot.com/docs/api/settings/currencies#hide-a-currency)
----------------------------------------------------------------------------------------------

You can hide a currency so that it's not visible in your HubSpot account. To hide an existing account currency, make a `POST` request to `/settings/v3/currencies/exchange-rates/update-visibility`. In your request, include the following:

*   `fromCurrencyCode`: the code of the currency you want to hide or show.
*   `toCurrencyCode`: the code of your company currency.
*   `visibleInUI`: whether or not the currency and its exchange rate are shown in your HubSpot account. To hide a currency, the value should be `false`. To show a previously hidden currency, set the value should be set to `true`.

To hide a currency, your request may look like:

///Example request body { "fromCurrencyCode": "USD", "toCurrencyCode": "AED", "visibleInUI": false }

Limits and scopes[](https://developers.hubspot.com/docs/api/settings/currencies#limits-and-scopes)
--------------------------------------------------------------------------------------------------

The daily limit for creating exchanges rates is 1000. This is a total limit which includes rates created both individually and in batches.

There are different scopes that a users needs in order to view or edit currency and exchange rate data:

*   `multi-currency-read`: required to retrieve and read currency data.
*   `multi-currency-write`: required to edit currency data.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/settings/currencies#page-feedback)
------------------------------------------------------------------------------------------------

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