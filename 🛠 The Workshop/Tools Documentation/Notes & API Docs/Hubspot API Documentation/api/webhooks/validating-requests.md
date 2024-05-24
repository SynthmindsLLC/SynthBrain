Validating requests from HubSpot
================================

To ensure that the requests that your integration is receiving from HubSpot are actually coming from HubSpot, several headers are populated in the request. You can use these headers, along with fields of the incoming request, to verify the signature of the request.

The method used to verify the signature depends on the version of the signature:

*   To validate a request using the latest version of the HubSpot signature, use the `X-HubSpot-Signature-V3` header and follow the [associated instructions for validating the v3 version of the signature](/docs/api/webhooks/validating-requests#validate-the-v3-request-signature).
*   For backwards compatibility, requests from HubSpot also include older versions of the signature. To validate an older version of the signature, check the `X-HubSpot-Signature-Version` header, then follow the associated instructions below based on whether the version is `v1` or `v2`.

In the instructions below, learn how to derive a hash value from your app's client secret and the fields of an incoming request. Once you compute the hash value, you'll compare it to the signature. If the two are equal, then the request has passed validation. Otherwise, the request may have been tampered with in transit or someone may be spoofing requests to your endpoint.

Validate requests using the v1 request signature[](https://developers.hubspot.com/docs/api/webhooks/validating-requests#validate-requests-using-the-v1-request-signature)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If your app is subscribed to [CRM object events via the webhooks API](/docs/api/webhooks), requests from HubSpot will be sent with the `X-HubSpot-Signature-Version` header set to `v1`. The `X-HubSpot-Signature` header will be an SHA-256 hash built using the client secret of your app combined with details of the request.

To verify this version of the signature, perform the following steps:

*   Create a string that concatenates together the following: `Client secret` + `request body` (if present)
*   Create a SHA-256 hash of the resulting string.
*   Compare the hash value to the value of the `X-HubSpot-Signature` header:
    *   If they're equal then this request has passed validation.
    *   If these values do not match, then this request may have been tampered with in-transit or someone may be spoofing requests to your endpoint.

**Example for a request with a body:**

//Client secret : yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy // Request body: \[ {"eventId":1,"subscriptionId":12345," portalId":62515", occurredAt":1564113600000", subscriptionType":"contact.creation", "attemptNumber":0, "objectId":123, "changeSource":"CRM", "changeFlag":"NEW", "appId":54321} \]

v1 request signature examples: 
------------------------------- 

NOTE: This is only an example for generating the expected hash. You will need to compare this expected hash with the actual hash in the X-HubSpot-Signature header. >>> import hashlib >>> client\_secret = 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy' >>> request\_body = '\[{"eventId":1,"subscriptionId":12345,"portalId":62515,"occurredAt":1564113600000,"subscriptionType":"contact.creation","attemptNumber":0,"objectId":123,"changeSource":"CRM","changeFlag":"NEW","appId":54321}\]' >>> source\_string = client\_secret + request\_body >>> source\_string 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy\[{"eventId":1,"subscriptionId":12345,"portalId":62515,"occurredAt":1564113600000,"subscriptionType":"contact.creation","attemptNumber":0,"objectId":123,"changeSource":"CRM","changeFlag":"NEW","appId":54321}\]' >>> hashlib.sha256(source\_string).hexdigest() '232db2615f3d666fe21a8ec971ac7b5402d33b9a925784df3ca654d05f4817de' NOTE: This is only an example for generating the expected hash. You will need to compare this expected hash with the actual hash in the X-HubSpot-Signature header. irb(main):003:0> require 'digest' => true irb(main):004:0> client\_secret = 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy' => "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy" irb(main):005:0> request\_body = '\[{"eventId":1,"subscriptionId":12345,"portalId":62515,"occurredAt":1564113600000,"subscriptionType":"contact.creation","attemptNumber":0,"objectId":123,"changeSource":"CRM","changeFlag":"NEW","appId":54321}\]' => "\[{\\"eventId\\":1,\\"subscriptionId\\":12345,\\"portalId\\":62515,\\"occurredAt\\":1564113600000,\\"subscriptionType\\":\\"contact.creation\\",\\"attemptNumber\\":0,\\"objectId\\":123,\\"changeSource\\":\\"CRM\\",\\"changeFlag\\":\\"NEW\\",\\"appId\\":54321}\]" irb(main):006:0> source\_string = client\_secret + request\_body => "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy\[{\\"eventId\\":1,\\"subscriptionId\\":12345,\\"portalId\\":62515,\\"occurredAt\\":1564113600000,\\"subscriptionType\\":\\"contact.creation\\",\\"attemptNumber\\":0,\\"objectId\\":123,\\"changeSource\\":\\"CRM\\",\\"changeFlag\\":\\"NEW\\",\\"appId\\":54321}\]" irb(main):007:0> Digest::SHA256.hexdigest source\_string => "232db2615f3d666fe21a8ec971ac7b5402d33b9a925784df3ca654d05f4817de" NOTE: This is only an example for generating the expected hash. You will need to compare this expected hash with the actual hash in the X-HubSpot-Signature header. > const crypto = require('crypto') undefined > client\_secret = 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy' 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy' > request\_body = '\[{"eventId":1,"subscriptionId":12345,"portalId":62515,"occurredAt":1564113600000,"subscriptionType":"contact.creation","attemptNumber":0,"objectId":123,"changeSource":"CRM","changeFlag":"NEW","appId":54321}\]' '\[{"eventId":1,"subscriptionId":12345,"portalId":62515,"occurredAt":1564113600000,"subscriptionType":"contact.creation","attemptNumber":0,"objectId":123,"changeSource":"CRM","changeFlag":"NEW","appId":54321}\]' > source\_string = client\_secret + request\_body 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy\[{"eventId":1,"subscriptionId":12345,"portalId":62515,"occurredAt":1564113600000,"subscriptionType":"contact.creation","attemptNumber":0,"objectId":123,"changeSource":"CRM","changeFlag":"NEW","appId":54321}\]' > hash = crypto.createHash('sha256').update(source\_string).digest('hex') '232db2615f3d666fe21a8ec971ac7b5402d33b9a925784df3ca654d05f4817de'

The resulting hash would be:  
`232db2615f3d666fe21a8ec971ac7b5402d33b9a925784df3ca654d05f4817de`

Validate requests using the v2 request signature[](https://developers.hubspot.com/docs/api/webhooks/validating-requests#validate-requests-using-the-v2-request-signature)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If your app is handling data from a [webhook action in a workflow](https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows), or if you're returning data for a [custom CRM card](/docs/api/crm/extensions/custom-cards), the request from HubSpot is sent with the `X-HubSpot-Signature-Version` header set to `v2`. The `X-HubSpot-Signature` header will be an SHA-256 hash built using the client secret of your app combined with details of the request.

To verify this signature, perform the following steps:

*   Create a string that concatenates together the following: `Client secret` + `http method` + `URI` + `request body` (if present)
*   Create a SHA-256 hash of the resulting string.
*   Compare the hash value to the signature.
    *   If they're equal then this request has passed validation.
    *   If these values do not match, then this request may have been tampered with in-transit or someone may be spoofing requests to your endpoint.

  
**Notes:**

*   The URI used to build the source string must exactly match the original request, including the protocol. If you're having trouble validating the signature, ensure that any query parameters are in the exact same order they were listed in the original request.
*   The source string should be UTF-8 encoded before calculating the SHA-256 hash.

  

**Example for a GET request:**

*   `Client secret` : yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
*   `HTTP Method`: GET
*   `URI`: [https://www.example.com/webhook\_uri](https://www.example.com/webhook_uri)

  

**Example for a request with a body:**

*   `Client secret` : yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
*   `HTTP Method:` POST
*   `URI`: [https://www.example.com/webhook\_uri](https://www.example.com/webhook_uri)
*   `Request body`: `{"example_field":"example_value"}`  

Validate the v3 request signature[](https://developers.hubspot.com/docs/api/webhooks/validating-requests#validate-the-v3-request-signature)
-------------------------------------------------------------------------------------------------------------------------------------------

The `X-HubSpot-Signature-v3` header will be an HMAC SHA-256 hash built using the client secret of your app combined with details of the request. It will also include a `X-HubSpot-Request-Timestamp` header.

When validating a request using the X-HubSpot-Signature-v3 header, you'll need to 

*   Reject the request if the timestamp is older than 5 minutes.
*   In the request URI, decode any of the URL-encoded characters listed in the table below. You do not need to decode the question mark that denotes the beginning of the query string.

| **Encoded value** | **Decoded value** |
| --- | --- |
| `%3A` | `:` |
| `%2F` | `/` |
| `%3F` | `?` |
| `%40` | `@` |
| `%21` | `!` |
| `%24` | `$` |
| `%27` | `'` |
| `%28` | `(` |
| `%29` | `)` |
| `%2A` | `*` |
| `%2C` | `,` |
| `%3B` | `;` |

*   Create a utf-8 encoded string that concatenates together the following: `requestMethod` + `requestUri` + `requestBody` + timestamp. The timestamp is provided by the `X-HubSpot-Request-Timestamp` header.
*   Create an HMAC SHA-256 hash of the resulting string using the application secret as the secret for the HMAC SHA-256 function.
*   Base64 encode the result of the HMAC function.
*   Compare the hash value to the signature. If they're equal then this request has been verified as originating from HubSpot. It's recommended that you use constant-time string comparison to guard against timing attacks.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/webhooks/validating-requests#page-feedback)
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